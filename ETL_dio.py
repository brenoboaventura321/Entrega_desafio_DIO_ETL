# Importando Bibliotecas
from numpy import append
import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")

# Importando os dados

caminho_arquivo_json ='usuarios_gamelauncher.json'

df_json = pd.read_json(caminho_arquivo_json)
usuarios = df_json.usuarios


