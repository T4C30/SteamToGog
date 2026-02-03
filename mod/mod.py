from os import open
from requests import get

# Pedir en Steam los juegos totales del jugador
def steam(api_key, steam_id):
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
def abrir():
    pass

# Pedir en gog los juegos totales de la pagina
def gog():
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
def discord():
    pass

# Guardar en el archivo
def guardar():
    pass