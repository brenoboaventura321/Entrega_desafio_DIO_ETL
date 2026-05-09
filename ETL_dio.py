# Importando Bibliotecas
from numpy import append
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")

# Extração
# Define o caminho e carrega os dados dos usuários do arquivo JSON

caminho_arquivo_json ='usuarios_gamelauncher.json'
df_json = pd.read_json(caminho_arquivo_json)

# Transformação
# Transforma o conteúdo do arquivo JSON em um DataFrame do Pandas

usuarios = df_json.usuarios
print(usuarios)

# Inicializa o cliente da API do Google Gemini

from google import genai
from google.genai import types

client = genai.Client(api_key=api_key)

lista_emails = {}

def generate_ai_news(user):
  name = user.get('nome')
  gen = user.get('generos_interesse')
  games = user.get('jogos_recentes')
  xp = user.get('nivel_experiencia')
  response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    config=types.GenerateContentConfig(
        system_instruction=f'Você é um agente de marketing da loja GmesLauncher-BR de games on-line com um catalogo atualizado de jogos. Gere uma mensagem personalizada ofertando 5 games recentes dos generos {gen[0]}e {gen[1]}, para o cliente de nivel {xp}, nome: {name}, jogos recentes: {games}'),
    contents=f'Gere um e-mail de até 200 caracteres para {name}'
    )
  return response.text

def listar_emails(usuario,mensagem):
  lista_emails[usuario] = mensagem
  return lista_emails

for cliente in usuarios:
  user_email = cliente.get('email')
  news = generate_ai_news(cliente)
  print(news)
  exibir_email_lista =   listar_emails(user_email,news)

print(exibir_email_lista)

