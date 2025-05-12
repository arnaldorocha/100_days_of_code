# Importando bibliotecas necessárias
from bs4 import BeautifulSoup  # Usada para fazer parsing de HTML (Web Scraping)
import requests  # Usada para fazer requisições HTTP
import spotipy  # Biblioteca oficial para interagir com a API do Spotify
from spotipy.oauth2 import SpotifyOAuth  # Classe de autenticação OAuth do Spotipy

# === ETAPA 1: Coletando as músicas da Billboard ===

# Solicita ao usuário uma data no formato específico para buscar o ranking musical
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Define o cabeçalho para simular um navegador e evitar bloqueios de bot
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# Monta a URL da Billboard com base na data fornecida
billboard_url = "https://www.billboard.com/charts/hot-100/" + date

# Faz a requisição HTTP para obter o HTML da página
response = requests.get(url=billboard_url, headers=header)

# Usa BeautifulSoup para analisar o conteúdo HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Seleciona os títulos das músicas usando um seletor CSS que encontra os <h3> dentro de listas da Billboard
song_names_spans = soup.select("li ul li h3")

# Extrai os nomes das músicas e remove espaços extras
song_names = [song.getText().strip() for song in song_names_spans]

# === ETAPA 2: Autenticando no Spotify ===

# Cria uma instância do cliente do Spotify com autenticação OAuth
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",  # Escopo necessário para criar playlists privadas
        redirect_uri="http://example.com",  # URL de redirecionamento (precisa estar registrada no app do Spotify)
        client_id=YOUR-CLIENT-ID,  # SUBSTITUIR pelo seu client_id
        client_secret=YOUR-CLIENT-SECRET,  # SUBSTITUIR pelo seu client_secret
        show_dialog=True,  # Força a exibição do prompt de login do Spotify
        cache_path="token.txt"  # Caminho para salvar o token de acesso
    )
)

# Obtém o ID do usuário autenticado
user_id = sp.current_user()["id"]
print(user_id)  # Opcional: imprime o ID para fins de debug

# === ETAPA 3: Buscando músicas no Spotify ===

# Lista para armazenar os URIs das músicas encontradas
song_uris = []
year = date.split("-")[0]  # Extrai o ano da data fornecida

# Para cada música encontrada na Billboard
for song in song_names:
    # Pesquisa a música no Spotify com base no título e ano
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)  # Opcional: imprime o resultado da pesquisa para debug

    # Tenta extrair o URI da primeira música retornada
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)  # Adiciona o URI à lista
    except IndexError:
        # Caso a música não seja encontrada, exibe uma mensagem e continua
        print(f"{song} doesn't exist in Spotify. Skipped.")

# === ETAPA 4: Criando a playlist no Spotify ===

# Cria uma nova playlist privada com o nome baseado na data fornecida
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)  # Opcional: imprime os detalhes da playlist criada

# === ETAPA 5: Adicionando músicas à playlist ===

# Adiciona todas as músicas encontradas à playlist criada
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
