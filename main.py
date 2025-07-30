from typing import List, Annotated
from sqlmodel import SQLModel, Session, create_engine, select
from fastapi import FastAPI, Depends, HTTPException
from models import Usuario, Viagem, Despesa
from contextlib import asynccontextmanager
from datetime import datetime

# as senhas salvas estão codificadas
from auth import hash_senha, verificar_senha

# configuração do banco
url = "sqlite:///banco.db"
args = {"check_same_thread": False}
engine = create_engine(url, connect_args=args)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

def create_db():
    SQLModel.metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db()
    yield


app = FastAPI(lifespan=lifespan)


# precisei fazer a conversão de string para date manualmente
def converter_str_date(data):
    formatacao = "%Y-%m-%d"
    return datetime.strptime(data, formatacao).date()


@app.post("/usuarios")
def criar_usuario(usuario:Usuario, session:SessionDep) -> Usuario:
    usuario.senha = hash_senha(usuario.senha)
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario


@app.post("/login")
def login(email:str, senha:str, session:SessionDep):
    usuario = session.exec(select(Usuario).where(Usuario.email == email)).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="E-mail incorreto")

    if not verificar_senha(senha, usuario.senha):
        raise HTTPException(status_code=401, detail="Senha incorreta")

    return {
        "mensagem": "Login bem-sucedido",
        "usuario_id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email
    }


@app.post("/usuarios/{usuario_id}/viagens")
def criar_viagem(usuario_id:int, viagem:Viagem, session:SessionDep) -> Viagem:
    viagem.usuario_id = usuario_id
    viagem.data_inicio = converter_str_date(viagem.data_inicio)
    viagem.data_fim = converter_str_date(viagem.data_fim)

    session.add(viagem)
    session.commit()
    session.refresh(viagem)
    return viagem


@app.get("/usuarios/{usuario_id}/viagens", response_model=List[Viagem])
def listar_viagens(usuario_id:int, session:SessionDep):
    return session.exec(
        select(Viagem).where(Viagem.usuario_id == usuario_id)
    ).all()


@app.get("/viagens/{id}", response_model=Viagem)
def detalhar_viagem(id:int, session:SessionDep):
    viagem = session.exec(select(Viagem).where(Viagem.id == id)).first()
    if not viagem:
        raise HTTPException(status_code=404, detail="Viagem não encontrada")
    return viagem


@app.put("/viagens/{id}")
def atualizar_viagem(id: int, dados: Viagem, session: SessionDep) -> Viagem:
    dados.data_inicio = converter_str_date(dados.data_inicio)
    dados.data_fim = converter_str_date(dados.data_fim)

    viagem = session.exec(select(Viagem).where(Viagem.id == id)).one()
    for campo, valor in dados.dict(exclude_unset=True).items():
        setattr(viagem, campo, valor)
    session.commit()
    session.refresh(viagem)
    return viagem


@app.delete("/viagens/{id}")
def deletar_viagem(id: int, session: SessionDep):
    viagem = session.exec(select(Viagem).where(Viagem.id == id)).one()
    session.delete(viagem)
    session.commit()
    return {"msg": "Viagem deletada com sucesso."}


@app.post("/viagens/{viagem_id}/despesas")
def adicionar_despesa(viagem_id: int, despesa: Despesa, session: SessionDep) -> Despesa:
    despesa.data = converter_str_date(despesa.data)
    despesa.viagem_id = viagem_id
    session.add(despesa)
    session.commit()
    session.refresh(despesa)
    return despesa


@app.get("/viagens/{viagem_id}/despesas", response_model=List[Despesa])
def listar_despesas(viagem_id: int, session: SessionDep):
    return session.exec(select(Despesa).where(Despesa.viagem_id == viagem_id)).all()


@app.put("/despesas/{id}")
def atualizar_despesa(id: int, dados: Despesa, session: SessionDep) -> Despesa:
    dados.data = converter_str_date(dados.data)
    despesa = session.exec(select(Despesa).where(Despesa.id == id)).one()
    for campo, valor in dados.dict(exclude_unset=True).items():
        setattr(despesa, campo, valor)
    session.commit()
    session.refresh(despesa)
    return despesa


@app.delete("/despesas/{id}")
def deletar_despesa(id: int, session: SessionDep):
    despesa = session.exec(select(Despesa).where(Despesa.id == id)).one()
    session.delete(despesa)
    session.commit()
    return {"msg": "Despesa removida com sucesso."}


#RESUMO FINANCEIRO DA VIAGEM
@app.get("/viagens/{viagem_id}/resumo")
def resumo_viagem(viagem_id: int, session: SessionDep):
    viagem = session.exec(select(Viagem).where(Viagem.id == viagem_id)).first()
    despesas = session.exec(select(Despesa).where(Despesa.viagem_id == viagem_id)).all()
    total_gasto = sum(d.valor for d in despesas)
    saldo = viagem.orcamento_total - total_gasto
    alerta = saldo < 0
    return {
        "total_orcamento": viagem.orcamento_total,
        "total_gasto": total_gasto,
        "saldo_restante": saldo,
        "alerta_orcamento_estourado": alerta
    }
