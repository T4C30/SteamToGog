from os import open
from requests import get

# Pedir en Steam los juegos totales del jugador
def steam(api_key:str, steam_id:str):
    respuesta=get(f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steam_id}&format=json")
    json_respuesta=respuesta.json()
    juegos = json_respuesta["response"]["games"]
    nombres = []
    for juego in juegos:
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
    pass

# Pedir en gog los juegos totales de la pagina
def gog(juegos_steam:list):
    respuesta=get("https://catalog.gog.com/v1/catalog?limit=50&order=asc")
    json_respuesta=respuesta.json() 
    productos = []
    
    paginas=json_respuesta["pages"]
    for pagina in range(paginas):
        respuesta=get(f"https://catalog.gog.com/v1/catalog?limit=50&order=asc&page={pagina+1}")
        json_respuesta=respuesta.json()
        juegos = json_respuesta["products"]
        for juego in juegos:
            productos.append(juego["title"])
            
    return productos


# Enviar a Discord
def discord(webhook:str, juegos:list):
    pass

# Guardar en el archivo
def guardar(juegos:list):
    pass

def cli():
    api_key = input("Api key del desarrollador: ")
    steam_id = input("SteamID del jugador: ")
    webhook = input("Dime la webhook de discord: ")
    ejecucion(api_key,steam_id,webhook)
    
def ejecucion(api_key:str,steam_id:str,webhook:str):
    nombres = steam(api_key,steam_id)
    juegos_steam = abrir(nombres)
    juegos = gog(juegos_steam)
    discord(webhook,juegos)
    guardar(juegos)
    
    