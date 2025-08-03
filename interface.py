from cli.menus import menu_inicial, menu_viagens
import cli.config as config

print("Bem-Vindo ao Viagem+")

while not config.id_usuario:
    menu_inicial()

menu_viagens()