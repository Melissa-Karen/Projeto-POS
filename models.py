from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date


class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    nome: str
    email: str
    senha: str


class Viagem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    usuario_id: int = Field(foreign_key="usuario.id")
    nome: str
    destino: str
    data_inicio: date
    data_fim: date
    orcamento_total: float
    notas: Optional[str] = None


class Despesa(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    viagem_id: int = Field(foreign_key="viagem.id")
    descricao: str
    valor: float
    data: date
    categoria: str


class Login(SQLModel):
    email: str
    senha: str
