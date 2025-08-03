from tabulate import tabulate
from .usuario import cadastrar_usuario, logar_usuario
import cli.config as config
from .viagem import cadastrar_viagem, exibir_viagens

def menu_inicial():

    opcoes = [
        [1, "Fazer cadastro"],
        [2, "Fazer Login"]
    ]

    print(tabulate(opcoes, tablefmt="rounded_grid", headers=["Opção", "Ação"]))
    opcao = input("Escolha uma opção acima: ")

    match opcao:
        case "1":
            retorno_cadastro = cadastrar_usuario()
            if retorno_cadastro.status_code == 200:
                retorno_cadastro = retorno_cadastro.json()
                config.id_usuario = retorno_cadastro.get("id")
                print("Cadastro Realizado com sucesso!")

        case "2":
            retorno_login = logar_usuario()

            while retorno_login.status_code != 200:
                retorno_login = retorno_login.json()
                print(f"{retorno_login.get("detail")}.")
                retorno_login = logar_usuario()

            retorno_login = retorno_login.json()
            config.id_usuario = retorno_login.get("id")
            print(f"Login realizado como {retorno_login.get('nome')}")
        case _:
            print("Opção inválida.")


def menu_viagens():
    while True:
        opcoes = [
            [1, "Exibir viagens"],
            [2, "Cadastrar nova viagem"],
            [3, "Sair"]
        ]

        print(tabulate(opcoes, tablefmt="rounded_grid", headers=["Opção", "Ação"]))
        escolha = input("Escolha uma opção: ")

        match escolha:
            case "1":
                exibir_viagens()
            case "2":
                cadastrar_viagem()
            case "3":
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Tente novamente.")









