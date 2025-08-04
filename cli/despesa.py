# funcionalidades
import requests
from .config import API, headers
from datetime import datetime

# estilização
from tabulate import tabulate
from .terminal import animacao_carregamento
from time import sleep


def listar_despesas(viagem_id):

    response = requests.get(f"{API}/viagens/{viagem_id}/despesas", headers=headers)
    if response.status_code != 200:
        print("Erro ao buscar despesas.")
        return
    
    despesas = response.json()
    if not despesas:
        print("Nenhuma despesa cadastrada para esta viagem.")
        return
    
    tabela = []
    for despesa in despesas:
        tabela.append([
            despesa["id"],
            despesa["descricao"],
            f"R$ {despesa['valor']:.2f}",
            despesa["data"],
            despesa["categoria"]
        ])


    print(tabulate(tabela, headers=["ID", "Descrição", "Valor", "Data", "Categoria"], tablefmt="fancy_grid"))


def cadastrar_despesa(viagem_id):

    descricao = input("Descrição: ")
    valor = input("Valor: R$ ")
    data = input("Data (YYYY-MM-DD): ")
    categoria = input("Categoria: ")

    try:
        valor = float(valor)
        datetime.strptime(data, "%Y-%m-%d")
    except ValueError:
        print("Valor ou data inválidos. Tente novamente.")
        sleep(2)
        return

    despesa = {
        "descricao": descricao,
        "valor": valor,
        "data": data,
        "categoria": categoria
    }

    animacao_carregamento()
    response = requests.post(f"{API}/viagens/{viagem_id}/despesas", json=despesa, headers=headers)

    if response.status_code == 200:
        print("Despesa cadastrada com sucesso.")
    else:
        print("Erro ao cadastrar despesa: ", response.text)


def selecionar_despesa(viagem_id):

    listar_despesas(viagem_id)
    try:
        despesa_id = int(input("Digite o ID da despesa que deseja editar/excluir (ou 0 para cancelar): "))
    except ValueError:
        print("ID inválido. Digite um número.")
        sleep(2)
        return None

    if despesa_id == 0:
        return None
    
    response = requests.get(f"{API}/despesas/{despesa_id}", headers=headers)
    
    if response.status_code == 200:
        despesa = response.json()
        if despesa["viagem_id"] == viagem_id:
            return despesa_id
        else:
            print("Esta despesa não pertence à viagem selecionada.")
            sleep(2)
    elif response.status_code == 404:
        print("Despesa não encontrada.")
        sleep(2)
    else:
        print(f"Erro ao verificar despesa: {response.status_code}")
        sleep(2)
    
    return None


def editar_despesa(viagem_id):
    
    despesa_id = selecionar_despesa(viagem_id)
    if not despesa_id:
        return
    
    response = requests.get(f"{API}/despesas/{despesa_id}", headers=headers)
    if response.status_code != 200:
        animacao_carregamento()
        print("Erro ao carregar despesa.")
        sleep(2)
        return
    
    despesa = response.json()
    
    print("Deixe em branco para manter o valor atual")
    
    descricao = input(f"Descrição [{despesa['descricao']}]: ") or despesa["descricao"]
    
    while True:
        valor = input(f"Valor (R$) [{despesa['valor']}]: ") or despesa["valor"]
        try:
            valor = float(valor)
            if valor <= 0:
                print("O valor deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Valor inválido. Digite um número (ex: 100.50).")
            continue
    
    while True:
        data = input(f"Data (YYYY-MM-DD) [{despesa['data']}]: ") or  despesa["data"]
        try:
            datetime.strptime(data, "%Y-%m-%d")
            break
        except ValueError:
            print("Formato de data inválido. Use YYYY-MM-DD.")
            continue
    
    categoria = input(f"Categoria [{despesa['categoria']}]: ")

    dados_atualizados = {
        "descricao": descricao,
        "valor": valor,
        "data": data,
        "categoria": categoria,
        "viagem_id": viagem_id
    }

    response = requests.put(f"{API}/despesas/{despesa_id}", json=dados_atualizados, headers=headers)

    if response.status_code == 200:
        animacao_carregamento()
        print("Despesa atualizada com sucesso!")
        sleep(2)
    else:
        animacao_carregamento()
        print("Erro ao atualizar despesa:", response.text)


def excluir_despesa(viagem_id):

    despesa_id = selecionar_despesa(viagem_id)
    if not despesa_id:
        return
    
    confirmacao = input(f"Tem certeza que deseja excluir a despesa ID {despesa_id}? (s/n): ").lower()
    while confirmacao not in ['s', 'n']:
        confirmacao = input(f"Tem certeza que deseja excluir a despesa ID {despesa_id}? (s/n): ").lower()

    if confirmacao == 's':
        animacao_carregamento()
        response = requests.delete(f"{API}/despesas/{despesa_id}", headers=headers)
        if response.status_code == 200:
            animacao_carregamento()
            print("Despesa excluída com sucesso!")
            sleep(2)
        else:
            animacao_carregamento()
            print("Erro ao excluir despesa: ", response.text)
            sleep(2)
    else:
        print("Operação cancelada.")
        sleep(2)