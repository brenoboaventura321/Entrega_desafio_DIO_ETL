# Importando Bibliotecas
from numpy import append
import pandas as pd
import time
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
from google import genai
from google.genai import types
from google.genai.errors import ClientError, ServerError


# Extração
# Define o caminho e carrega os dados dos usuários do arquivo JSON

caminho_arquivo_json ='usuarios_gamelauncher.json'
df_json = pd.read_json(caminho_arquivo_json)

# Transformação
# Transforma o conteúdo do arquivo JSON em um DataFrame do Pandas

usuarios = df_json.usuarios
print(usuarios)

# Inicializa o cliente da API do Google Gemini

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
        system_instruction=f'Você é um agente de marketing da loja GmesLauncher-BR de games on-line com um catalogo atualizado de jogos. Gere uma mensagem personalizada ofertando 5 games recentes dos generos {gen}, para o cliente de nivel {xp}, nome: {name}, jogos recentes: {games}'),
    contents=f'Gere um e-mail de até 200 caracteres para {name}'
    )
  return response.text

def listar_emails(usuario,mensagem):
  lista_emails[usuario] = mensagem
  return lista_emails

for cliente in usuarios:
    user_email = cliente.get('email')
    nome_cliente = cliente.get('nome')
    sucesso = False
    tentativas = 0
    max_tentativas = 3

    while not sucesso and tentativas < max_tentativas:
        try:
            # Tenta gerar a notícia
            news = generate_ai_news(cliente)
            
            # Se chegou aqui, deu certo! Adicionamos à lista
            lista_emails[user_email] = news
            print(f"✅ Sucesso: {nome_cliente} ({user_email})")
            
            sucesso = True
            # Intervalo padrão de 5 segundos para respeitar o limite de 15 RPM
            time.sleep(5) 

        except (ClientError, ServerError) as e:
            tentativas += 1
            erro_msg = str(e)
            
            if "429" in erro_msg:
                print(f"⚠️ Cota atingida (429) no usuário {nome_cliente}. Esperando 60s para retomar...")
                time.sleep(60) # Pausa longa para resetar o limite por minuto
            elif "503" in erro_msg:
                print(f"⚠️ Servidor instável (503). Tentativa {tentativas}/{max_tentativas}. Esperando 15s...")
                time.sleep(15)
            else:
                print(f"❌ Erro inesperado para {nome_cliente}: {e}")
                break # Sai do loop de tentativas para este usuário específico

    if not sucesso:
        print(f"🛑 Falha definitiva ao processar {nome_cliente} após {max_tentativas} tentativas.")

print("\n--- Processamento Concluído ---")
print(f"Total de e-mails gerados: {len(lista_emails)}")
print(lista_emails)

