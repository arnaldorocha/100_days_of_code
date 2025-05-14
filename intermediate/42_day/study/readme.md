# 🎵 Criando uma Playlist no Spotify com as Top 100 da Billboard de uma Data Específica

Este script automatiza a criação de uma playlist privada no Spotify com as 100 músicas mais populares da Billboard em uma data específica.

---

## 🧰 Etapa 0: Importando bibliotecas necessárias

```python
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth




BeautifulSoup: Analisa o HTML para extrair dados da página da Billboard.

requests: Faz a requisição HTTP para pegar o conteúdo da página.

spotipy: Biblioteca oficial para usar a API do Spotify.

SpotifyOAuth: Garante a autenticação segura do usuário no Spotify via OAuth 2.0.

🗓️ Etapa 1: Coletando músicas da Billboard
O usuário informa a data desejada (no formato YYYY-MM-DD), e o código acessa o site da Billboard para pegar as músicas daquele dia.


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
billboard_url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=billboard_url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
O código usa o seletor CSS li ul li h3 para localizar os títulos das músicas:


song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
🔍 Resultado: Lista song_names com as 100 músicas da Billboard daquele dia.

🔐 Etapa 2: Autenticando no Spotify
Autentica o usuário do Spotify para permitir criação de playlists privadas.


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=YOUR-CLIENT-ID,
        client_secret=YOUR-CLIENT-SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
O escopo playlist-modify-private permite criar playlists privadas.

A URL de redirecionamento e credenciais devem estar configuradas no Spotify Developer Dashboard.

🔍 Etapa 3: Buscando músicas no Spotify
Para cada título da Billboard, o código faz uma busca no Spotify para encontrar o URI da faixa.


for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    uri = result["tracks"]["items"][0]["uri"]
    song_uris.append(uri)
As buscas incluem o nome da música e o ano para aumentar a precisão.

Se uma música não for encontrada, ela é ignorada com um aviso.


🎧 Etapa 4: Criando a playlist
Cria uma playlist privada no perfil do usuário autenticado.



playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
➕ Etapa 5: Adicionando músicas à playlist
Com a playlist criada e os URIs das faixas em mãos, o código as adiciona de uma só vez:


sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
✅ Resumo Final
Etapa	Ação
🎯 Entrada	Usuário informa a data desejada
🌐 Web Scraping	Código extrai as músicas da Billboard
🔐 Login	Autenticação no Spotify
🔎 Busca	Código busca as músicas no Spotify
🧾 Criação	Playlist privada criada com nome baseado na data
➕ Adição	Músicas adicionadas à playlist

📦 Requisitos
Conta Spotify (Premium ou Free)

App Spotify registrado em: Spotify Developer Dashboard

Variáveis client_id e client_secret

Dependências Python:


pip install spotipy beautifulsoup4 requests python-dotenv
💡 Dica extra
Você pode automatizar isso para criar playlists semanais, mensais ou com outras listas além da Billboard.

👨‍💻 Crie sua playlist nostálgica agora!
Rode o script, insira sua data favorita e deixe a mágica acontecer. ✨








