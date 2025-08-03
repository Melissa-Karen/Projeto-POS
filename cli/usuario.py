import requests
from getpass import getpass
from .config import API, headers

def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = getpass("Digite sua senha: ")
    confirmacao = getpass("Confime a senha: ")

    while senha != confirmacao:
        print("As senhas não são iguais.")
        senha = getpass("Digite sua senha: ")
        confirmacao = getpass("Confime a senha: ")
    
    json = {
            "nome" : nome,
            "email" : email,
            "senha" : senha
            }

    response = requests.post(f"{API}/usuarios", json=json, headers=headers)
    return response


def logar_usuario():
    email = input("Digite seu e-mail: ")
    senha = getpass("Digite sua senha: ")

    json = {
            "email" : email,
            "senha" : senha
            }

    response = requests.post(f"{API}/login", json=json, headers=headers)
    return response

