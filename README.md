# 🎮 Pipeline ETL com IA Generativa: GamesLauncher-BR

Este projeto faz parte de um desafio de **Engenharia de Dados (ETL)**, onde desenvolvi um pipeline automatizado para extração, transformação e carga de dados de usuários de uma loja de games. O diferencial deste projeto é a fase de **Transform**, que utiliza Inteligência Artificial (Google Gemini) para gerar campanhas de marketing altamente personalizadas.

## 🛠️ O Pipeline de Dados

O projeto segue o fluxo clássico de dados:

1.  **Extract (Extração):** Leitura de dados estruturados a partir de um arquivo JSON (`usuarios_gamelauncher.json`) contendo perfis de jogadores, níveis de experiência e histórico de jogos.
2.  **Transform (Transformação):** Processamento dos dados com a biblioteca **Pandas** e integração com a API do **Google IA Studio**. A IA atua como um agente de marketing especializado, recomendando 5 novos títulos com base nos gêneros favoritos de cada usuário.
3.  **Load (Carga):** Armazenamento das mensagens geradas em um dicionário estruturado para posterior envio ou exportação.

## 🚀 Tecnologias e Bibliotecas

*   **Python 3.11**
*   **Pandas**: Manipulação e análise de dados.
*   **Google GenAI**: Integração com o modelo Gemini 2.0 Flash.
*   **Python-dotenv**: Gerenciamento seguro de credenciais via variáveis de ambiente.

## 🔐 Configuração de Segurança (Atenção!)

Para rodar este projeto, você deve configurar suas próprias credenciais da API. **Nunca** exponha sua chave diretamente no código.

1.  Obtenha sua chave de API no [Google AI Studio](https://aistudio.google.com/).
2.  Na raiz do projeto, crie um arquivo chamado `.env`.
3.  Dentro do arquivo `.env`, adicione a seguinte linha:
    ```env
    API_KEY=SUA_CHAVE_AQUI
    ```
4.  O arquivo `.gitignore` já está configurado para não subir o seu `.env` para o GitHub, mantendo seus dados protegidos.

## 📦 Como Instalar e Rodar

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```

2.  **Instale as dependências:**
    ```bash
    pip install pandas google-genai python-dotenv
    ```

3.  **Execute o script principal:**
    ```bash
    python ETL_dio.py
    ```

## 📝 Exemplo de Saída

O script gera mensagens personalizadas como esta:
> *"Olá [Nome]! Como um jogador de nível Hardcore e fã de Terror, que tal encarar o novo Resident Evil ou Silent Hill? Temos ofertas exclusivas para você na GamesLauncher-BR!"*

---

### 👤 Autor
Desenvolvido por **Breno**