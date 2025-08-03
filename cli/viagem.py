import requests
from tabulate import tabulate
from .config import API, headers
import cli.config as config
from datetime import datetime

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

    print(tabulate(tabela, headers=["ID", "Título", "Local", "Início", "Fim", "Orçamento"], tablefmt="rounded_grid"))


def cadastrar_viagem():
    print("=== Cadastro de nova viagem ===")
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
    print(response)

    if response.status_code == 200:
        print("Viagem cadastrada com sucesso!")
    else:
        print("Erro ao cadastrar viagem.")
