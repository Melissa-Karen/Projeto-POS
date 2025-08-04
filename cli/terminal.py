import os
import platform
import time
from tabulate import tabulate
import sys

def limpar_terminal():
    system_name = platform.system()
    if system_name == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def mostrar_titulo(titulo):
    limpar_terminal()
    print(tabulate([[f"{titulo.upper()}"]], tablefmt="fancy_grid"))


def animacao_carregamento(duracao=4):
    print("Carregando", end="")
    for _ in range(3):
        time.sleep(duracao/6)
        print(".", end="", flush=True)

    time.sleep(duracao/6)
    sys.stdout.write("\r" + " " * 20 + "\r")
    sys.stdout.flush()