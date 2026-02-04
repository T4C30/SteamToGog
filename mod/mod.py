from io import open
from os.path import exists
from requests import get
from discord_webhook import DiscordWebhook
from rich.progress import track

# Pedir en Steam los juegos totales del jugador
def steam(api_key:str, steam_id:str):
    respuesta=get(f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steam_id}&format=json")
    json_respuesta=respuesta.json()
    juegos = json_respuesta["response"]["games"]
    nombres = []
    for juego in track(juegos, "Revisando juegos de Steam: "):
        id = juego["appid"]
        respuesta=get(f"https://store.steampowered.com/api/appdetails?appids={id}")
        json_respuesta=respuesta.json()
        try:
            nombres.append(json_respuesta[str(id)]["data"]["name"])
        except:
            pass
    return nombres

# Comprobar que no esten en el archivo de enviados
def abrir(nombres:list):
    archivo = open("juegos.txt","+r")
    lista_negra=archivo.readlines()
    archivo.close()
    lista_negra = [ln.rstrip("\n") for ln in lista_negra]
    return [n for n in nombres if n not in lista_negra]


# Pedir en gog los juegos totales de la pagina
def gog(juegos_steam:list):
    respuesta=get("https://catalog.gog.com/v1/catalog?limit=50&order=asc")
    json_respuesta=respuesta.json() 
    productos = []
    
    paginas=json_respuesta["pages"]
    for pagina in track(range(paginas), "Revisando juegos por pagina"):
        respuesta=get(f"https://catalog.gog.com/v1/catalog?limit=50&order=asc&page={pagina+1}")
        json_respuesta=respuesta.json()
        juegos = json_respuesta["products"]
        for juego in juegos:
            productos.append(juego["title"])
            
    return [p for p in productos if p in juegos_steam]


# Enviar a Discord
def discord(webhook:str, juegos:list):
    mensaje = "# Lista de juegos de Steam a GOG\n"
    for juego in juegos:
        mensaje += " - "+juego+"\n"
    discord = DiscordWebhook(url=webhook, content=mensaje)
    discord.execute()

# Guardar en el archivo
def guardar(juegos:list):
    archivo = open("juegos.txt","+a")
    for juego in juegos:
        archivo.write(juego + "\n")
    archivo.close()

def cli():
    api_key = input("Api key del desarrollador: ")
    steam_id = input("SteamID del jugador: ")
    webhook = input("Dime la webhook de discord: ")
    ejecucion(api_key,steam_id,webhook)
    
def ejecucion(api_key:str,steam_id:str,webhook:str):
    if not exists("juegos.txt"):
        with open("juegos.txt","+a"):
            pass
    nombres = steam(api_key,steam_id)
    juegos_steam = abrir(nombres)
    juegos = gog(juegos_steam)
    discord(webhook,juegos)
    guardar(juegos)
    
    