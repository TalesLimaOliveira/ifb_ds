import requests
# from bs4 import BeautifulSoup

# URL da página com os deputados distritais
url = "https://www.cl.df.gov.br/web/guest/deputados-2023-2026"

# Cabeçalhos para simular um navegador
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Faz a requisição HTTP
response = requests.get(url, headers=headers)

# Verifica se a requisição foi bem-sucedida
if response.status_code != 200:
    print(f"Erro ao acessar a página. Código de status: {response.status_code}")
    exit()

# Analisa o conteúdo HTML da página
soup = BeautifulSoup(response.text, "html.parser")

# Encontra todos os elementos que contêm os nomes dos deputados
# HTML está como: '<span class="card-title">Chico Vigilante</span>'
deputados = soup.find_all("span", class_="card-title")

# Lista para armazenar os nomes dos deputados
lista_deputados = []

# Itera sobre os elementos encontrados e extrai os nomes
for deputado in deputados:
    nome = deputado.get_text(strip=True)
    if nome:
        lista_deputados.append(nome)

# Exibe os nomes dos deputados
print("Deputados Distritais do DF (2023–2026):\n")
for idx, nome in enumerate(lista_deputados, start=1):
    print(f"{idx}. {nome}")

print(f"\nTotal de deputados encontrados: {len(lista_deputados)}")