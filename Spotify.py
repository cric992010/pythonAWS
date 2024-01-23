import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv(".env")


def obtener_canciones_populares(artist_name):
    """ client_id, client_secret = obtener_credenciales() """
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    resultados = sp.search(q='artist:' + artist_name, type='artist')
    artist_id = resultados['artists']['items'][0]['id']
    
    top_tracks = sp.artist_top_tracks(artist_id)
    
    return top_tracks['tracks']

def mostrar_canciones(canciones):
    print("\nLas 10 canciones más populares del artista son:")
    for i, cancion in enumerate(canciones, 1):
        print(f"{i}. {cancion['name']} - Popularidad: {cancion['popularity']}")

def main():
    artista = input("Ingrese el nombre del artista: ")
    canciones_populares = obtener_canciones_populares(artista)
    
    mostrar_canciones(canciones_populares)
    
    playlist = []
    
    while len(playlist) < 2:
        try:
            numero_cancion = int(input("\nSeleccione una canción (1-10) para agregar a la lista de reproducción: "))
            if 1 <= numero_cancion <= 10:
                cancion_seleccionada = canciones_populares[numero_cancion - 1]
                playlist.append(cancion_seleccionada)
                print(f"\nCanción agregada: {cancion_seleccionada['name']}")
            else:
                print("Por favor, ingrese un número válido (1-10).")
        except ValueError:
            print("Por favor, ingrese un número válido (1-10).")
    
    duracion_total = sum(cancion['duration_ms'] for cancion in playlist)
    duracion_total_minutos = duracion_total / 60000
    
    print("\nLista de reproducción:")
    for i, cancion in enumerate(playlist, 1):
        print(f"{i}. {cancion['name']} - Duración: {round(cancion['duration_ms'] / 60000, 2)} minutos")
    
    print(f"\nDuración total de la lista de reproducción: {round(duracion_total_minutos, 2)} minutos")


main()
