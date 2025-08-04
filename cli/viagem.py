# funcionalidades
import requests
from .config import API, headers
import cli.config as config
from datetime import datetime

# estilização
from tabulate import tabulate
from time import sleep
from .terminal import animacao_carregamento


def exibir_viagens():
    response = requests.get(f"{API}/usuarios/{config.id_usuario}/viagens", headers=headers)

    if response.status_code != 200:
        print("Erro ao buscar viagens.")
        return
    
    viagens = response.json()
    if not viagens:
        print("Nenhuma viagem cadastrada.")
        return
    
    tabela = []
    for viagem in viagens:
        tabela.append([
            viagem["id"],
            viagem["nome"],
            viagem["destino"],
            viagem["data_inicio"],
            viagem["data_fim"],
            f"R$ {viagem['orcamento_total']:.2f}"
        ])

    print(tabulate(tabela, headers=["ID", "Título", "Local", "Início", "Fim", "Orçamento"], tablefmt="fancy_grid"))


def cadastrar_viagem():
    nome = input("Título da viagem: ")
    destino = input("Local da viagem: ")
    data_inicio = input("Data de início (YYYY-MM-DD): ")
    data_fim = input("Data de fim (YYYY-MM-DD): ")
    orcamento_total = input("Orçamento total: ")
    notas = input("Notas: ")

    try:
        datetime.strptime(data_inicio, "%Y-%m-%d")
        datetime.strptime(data_fim, "%Y-%m-%d")
        orcamento_total = float(orcamento_total)
    except Exception:
        print("Dados inválidos. Tente novamente.")
        return
    
    viagem = {
        "nome": nome,
        "destino": destino,
        "data_inicio": data_inicio,
        "data_fim": data_fim,
        "orcamento_total": orcamento_total,
        "notas": notas
    }

    response = requests.post(f"{API}/usuarios/{config.id_usuario}/viagens",json=viagem, headers=headers)

    if response.status_code == 200:
        animacao_carregamento()
        print("Viagem cadastrada com sucesso.")
        sleep(2)
    else:
        animacao_carregamento()
        print("Erro ao cadastrar viagem.")
        sleep(2)


def selecionar_viagem():
    exibir_viagens()
    try:
        viagem_id = int(input("Digite o ID da viagem que deseja gerenciar (ou 0 para cancelar): "))
        if viagem_id == 0:
            return None
        
        response = requests.get(f"{API}/viagens/{viagem_id}", headers=headers)
        if response.status_code == 200:
            return viagem_id
        else:
            print("Viagem não encontrada.")
            sleep(2)
            return None
    except ValueError:
        print("ID inválido. Digite um número.")
        sleep(2)
        return None


def editar_viagem(viagem_id):
    response = requests.get(f"{API}/viagens/{viagem_id}", headers=headers)
    
    if response.status_code != 200:
        print("Erro ao carregar dados da viagem.")
        sleep(2)
        return
    
    viagem = response.json()
    
    print("Deixe em branco para manter o valor atual")
    
    nome = input(f"Nome da viagem [{viagem['nome']}]: ") or viagem["nome"]
    destino = input(f"Destino [{viagem['destino']}]: ") or viagem["destino"]
    data_inicio = input(f"Data de início (YYYY-MM-DD) [{viagem['data_inicio']}]: ") or viagem["data_inicio"]
    data_fim = input(f"Data de fim (YYYY-MM-DD) [{viagem['data_fim']}]: ") or viagem["data_fim"]
    orcamento = input(f"Orçamento total [R$ {viagem['orcamento_total']}]: ") or viagem["orcamento_total"]
    notas = input(f"Notas [{viagem['notas']}]: ") or viagem["notas"]

    try:
        orcamento = float(orcamento) if isinstance(orcamento, str) else orcamento
        datetime.strptime(data_inicio, "%Y-%m-%d")
        datetime.strptime(data_fim, "%Y-%m-%d")
    except ValueError:
        animacao_carregamento()
        print("Dados inválidos. Verifique os valores informados.")
        sleep(2)
        return

    dados_atualizados = {
        "nome": nome,
        "destino": destino,
        "data_inicio": data_inicio,
        "data_fim": data_fim,
        "orcamento_total": orcamento,
        "notas": notas
    }

    response = requests.put(f"{API}/viagens/{viagem_id}", json=dados_atualizados, headers=headers)

    if response.status_code == 200:
        animacao_carregamento()
        print("Viagem atualizada com sucesso!")
        sleep(2)
    else:
        animacao_carregamento()
        print("Erro ao atualizar viagem:", response.text)
        sleep(2)


def excluir_viagem(viagem_id):
    response = requests.get(f"{API}/viagens/{viagem_id}", headers=headers)
    if response.status_code != 200:
        print("Viagem não encontrada.")
        sleep(2)
        return False
    
    viagem = response.json()
    
    tabela = [
        [viagem["id"], viagem["nome"], viagem["destino"], viagem["data_inicio"], viagem["data_fim"], f'{viagem["orcamento_total"]:.2f}', ]
    ]

    print(tabulate(tabela, headers=["ID", "Título", "Local", "Início", "Fim", "Orçamento"], tablefmt="fancy_grid"))
    
    confirmacao = input("\nTem certeza que deseja excluir esta viagem? (s/n): ").lower()
    while confirmacao not in ['s', 'n']:
        confirmacao = input("\nTem certeza que deseja excluir esta viagem? (s/n): ").lower()
    if confirmacao != 's':
        print("Operação cancelada.")
        sleep(2)
        return False
    
    response = requests.delete(f"{API}/viagens/{viagem_id}", headers=headers)
    
    if response.status_code == 200:
        animacao_carregamento()
        print("Viagem excluída com sucesso.")
        sleep(2)
        return True
    else:
        print(f"Erro ao excluir viagem: {response.text}")
        sleep(2)
        return False
    

def mostrar_resumo_orcamento(viagem_id):
    response_viagem = requests.get(f"{API}/viagens/{viagem_id}", headers=headers)
    if response_viagem.status_code != 200:
        print("Erro ao carregar dados da viagem.")
        sleep(2)
        return
    
    viagem = response_viagem.json()
    
    response = requests.get(f"{API}/viagens/{viagem_id}/despesas", headers=headers)
    if response.status_code == 200:
        despesas= response.json()
    else:
        despesas = []    

    total_despesas = sum(despesa['valor'] for despesa in despesas)
    saldo = viagem['orcamento_total'] - total_despesas
    
    tabela = [
        [viagem["orcamento_total"], total_despesas, saldo]
    ]

    print(tabulate(tabela, headers=["Orcamento", "Despesas", "Saldo"], tablefmt="fancy_grid"))

    if saldo < 0:
        print("ALERTA: Orçamento estourado!")