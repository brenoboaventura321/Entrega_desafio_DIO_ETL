# 🎮 Pipeline de ETL com IA: Marketing para GamesLauncher-BR

Projeto desenvolvido como desafio para a trilha de Ciência de Dados/ETL, com o objetivo de criar um pipeline que extrai dados de usuários, utiliza IA Generativa para criar mensagens personalizadas e organiza essas informações.

## 🚀 Tecnologias Utilizadas

*   **Python 3.11**
*   **Pandas**: Para manipulação e leitura dos dados JSON.
*   **Google Gemini API (SDK `google-genai`)**: Para geração de conteúdo via IA.
*   **Python-dotenv**: Para gerenciamento de variáveis de ambiente e segurança.

## 📋 Pré-requisitos

Antes de rodar o projeto, você precisará instalar as dependências necessárias:

```bash
pip install pandas google-genai python-dotenv

```

## 🔐 Configuração da API (Importante)

Para proteger as credenciais, este projeto utiliza um arquivo de ambiente.

1. Crie um arquivo na raiz do projeto chamado `.env`.
2. Adicione a sua chave de API do **Google IA Studio** no seguinte formato:

```env
API_KEY=COLOQUE_SUA_CHAVE_AQUI

```

> **Atenção:** Nunca suba o seu arquivo `.env` para repositórios públicos. O arquivo `.gitignore` deste projeto já está configurado para ignorá-lo.

## 🛠️ Como funciona o Pipeline

1. **Extract**: O script lê o arquivo `usuarios_gamelauncher.json` contendo perfis de jogadores, seus gêneros de interesse (terror, ação, etc.) e nível de experiência.
2. **Transform**: Para cada usuário, o sistema envia um prompt personalizado para o modelo **Gemini 2.0 Flash**, que atua como um agente de marketing criando ofertas de 5 jogos baseados no histórico do cliente.
3. **Load**: As mensagens geradas são armazenadas em um dicionário e exibidas ao final do processo, simulando uma fila de disparos de e-mail.

## 👤 Autor

**Breno**

*Estudante de Engenharia de Dados / Ciência de Dados*

```

---

### Dica para a entrega:
Ao subir para o GitHub, certifique-se de que os arquivos `usuarios_gamelauncher.json`, `ETL_dio.py`, `README.md` e `.gitignore` estão lá. O `.env` **deve ficar de fora** para garantir sua nota máxima em segurança de dados!

```