# Agregador de Cidade — API em Python

API REST feita com **FastAPI** que recebe o nome de uma cidade e devolve, num único JSON, o clima atual e as últimas notícias relacionadas a ela — agregando dados de duas APIs externas em paralelo.

## Tecnologias utilizadas

| Tecnologia | Função no projeto |
|---|---|
| **Python 3.11** | Linguagem principal |
| **FastAPI** | Framework web para criar a API e gerar documentação automática |
| **Uvicorn** | Servidor ASGI que roda a aplicação |
| **httpx** | Cliente HTTP assíncrono para chamar as APIs externas |
| **python-dotenv** | Carrega variáveis de ambiente (chaves de API) do arquivo `.env` |
| **asyncio** | Executa as chamadas de clima e notícias em paralelo |
| **OpenWeatherMap API** | Fonte externa de dados de clima |
| **NewsAPI** | Fonte externa de dados de notícias |

## Estrutura do projeto

```
API - agregador/
├── main.py              # Ponto de entrada da API, define a rota /resumo/{cidade}
├── services/
│   ├── climate.py        # Busca dados de clima na OpenWeatherMap
│   └── news.py            # Busca notícias na NewsAPI
├── requeriments.txt       # Dependências do projeto
└── .env                   # Chaves de API
```

## Como rodar o projeto

### 1. Criar um ambiente virtual (recomendado)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Instalar as dependências

```powershell
pip install -r requeriments.txt
```

### 3. Configurar as chaves de API

Crie um arquivo `.env` na raiz da pasta `API - agregador` com:

```
OPENWEATHER_KEY=sua_chave_openweathermap
NEWSAPI_KEY=sua_chave_newsapi
```

- Chave da OpenWeatherMap: https://openweathermap.org/api (gratuita, pode levar até 2h para ativar)
- Chave da NewsAPI: https://newsapi.org/ (gratuita, ativa na hora)

### 4. Rodar o servidor

```powershell
python -m uvicorn main:app --reload
```

O servidor sobe em `http://127.0.0.1:8000`.

## Como usar a API

### Documentação interativa (Swagger)

Acesse `http://127.0.0.1:8000/docs` para testar a API diretamente pelo navegador, sem precisar montar a URL manualmente.

### Endpoint principal

```
GET /resumo/{cidade}
```

**Exemplo de requisição:**
```
GET http://127.0.0.1:8000/resumo/SaoPaulo
```

**Exemplo de resposta:**
```json
{
  "cidade": "SaoPaulo",
  "clima": {
    "temperatura": 24.5,
    "sensacao": 25.1,
    "descricao": "céu limpo"
  },
  "noticias": [
    {
      "titulo": "Título da notícia",
      "fonte": "Nome da fonte",
      "url": "https://..."
    }
  ]
}
```

### Códigos de resposta

| Código | Significado |
|---|---|
| 200 | Sucesso — dados de clima e notícias retornados |
| 404 | Cidade não encontrada no serviço de clima |

## Próximos passos (melhorias planejadas)

- [ ] Cache de resultados para evitar estourar limite de requisições gratuitas
- [ ] Retornar clima mesmo se a busca de notícias falhar (tolerância a falhas parciais)
- [ ] Testes automatizados com pytest
- [ ] Deploy em serviço gratuito (Render/Railway)
