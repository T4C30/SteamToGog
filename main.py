from argparse import ArgumentParser
from mod.mod import cli
from mod.mod import ejecucion

parseador = ArgumentParser(
    prog="SteamToGog",
    description="Busqueda de juegos disponible de Steam a GOG"
)

parseador.add_argument("-t","--tui",action="store_true", help="Entra en modo TUI/CLI")
parseador.add_argument("-g","--gui",action="store_true", help="Entra en modo GUI")
parseador.add_argument("-a", help="API Key de desarrollador de Steam")
parseador.add_argument("-s", help="Steam id del usuario")
parseador.add_argument("-w", help="Webhook para enviar informacion")

argumentos = parseador.parse_args()

def main():
    if argumentos.tui:
        api_key = argumentos.a
        steam_id = argumentos.s
        webhook = argumentos.w
        ejecucion(api_key, steam_id, webhook)
    elif argumentos.gui:
        # Abrir una ventana con Tkinter
        pass
    else:
        cli() 

if "__main__" == __name__:
    main()