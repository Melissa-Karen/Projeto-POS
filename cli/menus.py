# funcionalidades
from .usuario import cadastrar_usuario, logar_usuario
from .viagem import cadastrar_viagem, exibir_viagens, selecionar_viagem, editar_viagem, excluir_viagem, mostrar_resumo_orcamento
from .despesa import cadastrar_despesa, listar_despesas, editar_despesa, excluir_despesa
import cli.config as config

# estilização
from tabulate import tabulate
from .terminal import limpar_terminal, mostrar_titulo, animacao_carregamento
from time import sleep


def menu_inicial():
    while True:
        mostrar_titulo("Viagem+ - Controle Financeiro de Viagens")
        opcoes = [
            [1, "Fazer cadastro"],
            [2, "Fazer Login"],
            [3, "Sair do sistema"]
        ]

        print(tabulate(opcoes, tablefmt="fancy_grid", headers=["Opção", "Ação"]))
        opcao = input("Escolha uma opção acima: ")

        match opcao:
            case "1":
                mostrar_titulo("Cadastro de novo usuário")

                retorno_cadastro = cadastrar_usuario()
                if retorno_cadastro.status_code == 200:
                    animacao_carregamento()
                    retorno_cadastro = retorno_cadastro.json()
                    config.id_usuario = retorno_cadastro.get("id")
                    print("Cadastro Realizado com sucesso.")
                    sleep(2)
                else:
                    print("Erro no cadastro. Tente novamente.")
                    sleep(2)

            case "2":
                mostrar_titulo("Login do usuário")
                retorno_login = logar_usuario()

                while retorno_login.status_code != 200:
                    mostrar_titulo("Login do usuário")
                    retorno_login = retorno_login.json()
                    print(f"{retorno_login.get("detail")}")
                    sleep(2)
                    mostrar_titulo("Login do usuário")    
                    retorno_login = logar_usuario()

                animacao_carregamento()
                retorno_login = retorno_login.json()
                config.id_usuario = retorno_login.get("id")
                print(f"Login realizado como {retorno_login.get('nome')}.")
                sleep(2)
                menu_viagens()

            case "3":
                animacao_carregamento()
                print("Obrigado por usar o Viagem+")
                exit()

            case _:
                print("Opção inválida. Tente novamente.")
                sleep(1)


def menu_viagens():
    while True:
        mostrar_titulo("Minhas Viagens")
        opcoes = [
            [1, "Exibir viagens"],
            [2, "Cadastrar nova viagem"],
            [3, "Gerenciar viagem existente"],
            [4, "Voltar ao menu anterior"]
        ]

        print(tabulate(opcoes, tablefmt="fancy_grid", headers=["Opção", "Ação"]))
        escolha = input("Escolha uma opção: ")

        match escolha:
            case "1":
                mostrar_titulo("Minhas Viagens")
                exibir_viagens()
                input("Pressione Enter para continuar")

            case "2":
                mostrar_titulo("Cadastrar Nova Viagem")
                cadastrar_viagem()

            case "3":
                mostrar_titulo("Gerenciar Viagem")
                viagem_id = selecionar_viagem()
                if viagem_id:
                    menu_gerenciar_viagem(viagem_id)

            case "4":
                return

            case _:
                print("Opção inválida. Tente novamente.")
                sleep(1)


def menu_gerenciar_viagem(viagem_id):
    while True:
        mostrar_titulo(f"Gerenciando Viagem ID: {viagem_id}")
        opcoes = [
            [1, "Editar dados da viagem"],
            [2, "Gerenciar despesas"],
            [3, "Ver resumo financeiro"],
            [4, "Excluir viagem"],
            [5, "Voltar"]
        ]

        print(tabulate(opcoes, tablefmt="fancy_grid", headers=["Opção", "Ação"]))
        escolha = input("Escolha uma opção: ")

        match escolha:
            case "1":
                mostrar_titulo(f"Editar Viagem ID: {viagem_id}")
                editar_viagem(viagem_id)

            case "2":
                mostrar_titulo(f"Despesas da Viagem ID: {viagem_id}")
                menu_despesas(viagem_id)

            case "3":
                mostrar_titulo(f"Resumo Financeiro - Viagem ID: {viagem_id}")
                mostrar_resumo_orcamento(viagem_id)
                input("Pressione Enter para continuar")

            case "4":
                mostrar_titulo(f"Excluir Viagem ID: {viagem_id}")
                if excluir_viagem(viagem_id):
                    return

            case "5":
                return

            case _:
                print("Opção inválida. Tente novamente.")
                sleep(1)


def menu_despesas(viagem_id):
    while True:
        limpar_terminal()
        mostrar_titulo(f"Gerenciar Despesas - Viagem {viagem_id}")
      
        opcoes = [
            [1, "Listar despesas"],
            [2, "Adicionar despesa"],
            [3, "Editar despesa"],
            [4, "Excluir despesa"],
            [5, "Voltar"]
        ]

        print(tabulate(opcoes, tablefmt="fancy_grid", headers=["Opção", "Ação"]))
        escolha = input("Escolha uma opção: ")

        match escolha:
            case "1":
                mostrar_titulo(f"Despesas da Viagem {viagem_id}")
                listar_despesas(viagem_id)
                input("Pressione Enter para voltar")

            case "2":
                mostrar_titulo(f"Nova Despesa - Viagem {viagem_id}")
                cadastrar_despesa(viagem_id)

            case "3":
                mostrar_titulo(f"Editar Despesa - Viagem {viagem_id}")
                editar_despesa(viagem_id)

            case "4":
                mostrar_titulo(f"Excluir Despesa - Viagem {viagem_id}")         
                excluir_despesa(viagem_id)

            case "5":
                return

            case _:
                print("Opção inválida. Tente novamente.")
