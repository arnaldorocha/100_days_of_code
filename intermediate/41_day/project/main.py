# Importa o módulo `requests`, que permite fazer requisições HTTP pela internet.
import requests

# Importa a classe `BeautifulSoup` da biblioteca `bs4` para fazer o parsing (análise) do HTML.
from bs4 import BeautifulSoup

# Define a URL de uma versão arquivada da página da Empire com a lista dos melhores filmes.
# Essa versão antiga é usada porque o site atual foi modificado e o código original não funcionaria mais.
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Faz uma requisição GET para a URL fornecida e armazena a resposta.
response = requests.get(URL)

# Acessa o conteúdo da resposta como texto HTML bruto.
website_html = response.text

# Cria um objeto BeautifulSoup, passando o HTML e o parser "html.parser" para permitir a análise da estrutura da página.
soup = BeautifulSoup(website_html, "html.parser")

# Encontra todos os elementos <h3> com a classe "title", que contêm os títulos dos filmes.
all_movies = soup.find_all(name="h3", class_="title")

# Cria uma lista com os textos dos títulos dos filmes, extraindo o texto de cada elemento <h3>.
movie_titles = [movie.getText() for movie in all_movies]

# Inverte a lista, porque os filmes estavam listados do 100 ao 1, e queremos do 1 ao 100.
movies = movie_titles[::-1]

# Abre (ou cria) um arquivo chamado "movies.txt" no modo escrita ("w").
# O bloco `with` garante que o arquivo será fechado automaticamente ao final.
with open("movies.txt", mode="w", encoding="utf-8") as file:
    # Para cada filme na lista invertida, escreve uma linha no arquivo com o nome do filme.
    for movie in movies:
        file.write(f"{movie}\n")  # Adiciona uma quebra de linha após cada título.

