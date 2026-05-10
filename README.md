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
## 📥 Exemplo de Entrada (Dataset)
O arquivo usuarios_gamelauncher.json serve como a fonte de dados (Extract). Cada objeto representa um perfil de cliente com seus gostos específicos:
```bash
{
  "nome": "Lucas Oliveira",
  "email": "lucas.oliveira@email.com",
  "generos_interesse": ["terror", "acao"],
  "nivel_experiencia": "Hardcore",
  "jogos_recentes": ["Resident Evil Village", "Doom Eternal"]
}
```
## ⚙️ Limitações do Modelo e Resiliência
Devido às restrições do Free Tier da API do Google Gemini, o projeto implementa estratégias de Data Engineering para garantir a estabilidade:

RPM (Requests Per Minute): Limite de 15 requisições por minuto. O script utiliza um intervalo de segurança (time.sleep(5)) para evitar bloqueios.

Gestão de Erros (429 e 503): O pipeline conta com lógica de retentativa e pausa automática (Exponential Backoff) caso os limites de taxa sejam atingidos ou o servidor apresente instabilidade por alta demanda.

## 📤 Saída Esperada (JSON de E-mails)
Ao final da execução (Load), o script consolida todas as transformações em um dicionário Python (convertível para JSON), onde a chave é o e-mail do usuário e o valor é o conteúdo gerado pela IA:
```bash
{
  "lucas.oliveira@email.com": "Olá Lucas! Como um veterano Hardcore de Resident Evil, a GamesLauncher-BR separou 5 novos títulos de terror e ação de arrepiar para você. Confira no nosso catálogo!",
  "bia.souza@provedor.net": "Oi Beatriz! Notamos seu nível Casual em estratégia. Que tal exercitar a mente com 5 novos puzzles e jogos de lógica que acabaram de chegar? Aproveite!",
  "gabriel.games99@email.com": "Gabriel, o terror te espera! Com base em Dead Space, selecionamos 5 games de ação e horror para desafiar suas habilidades de nível Intermediário."
}
```
---

### 👤 Autor
Desenvolvido por **Breno**
