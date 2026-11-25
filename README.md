# 🎬 Catálogo de Séries API

API RESTful desenvolvida em Python com **FastAPI** para cadastro e consulta de séries, evoluindo desde a persistência simples até a integração com banco de dados relacional.

## 🚀 Evolução do Projeto por Etapas

1. **Cadastro de Séries (`POST /series`)**: Criação do endpoint de entrada com validação rigorosa de dados utilizando **Pydantic** (garantindo ano de lançamento > 1900 e número de temporadas positivo) e arquitetura modularizada.
2. **Listagem do Catálogo (`GET /series`)**: Implementação da consulta completa de todas as séries registradas, retornando uma lista estruturada em JSON.
3. **Migração para SQLite e Busca Específica (`GET /series/{titulo}`)**: Substituição do armazenamento em arquivo JSON pelo banco de dados **SQLite (`sqlite3`)**, adicionando busca *case-insensitive* por título e tratamento de erros HTTP (`404 Not Found` e `400 Bad Request`).

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **FastAPI** (Framework web e documentação automática via Swagger)
* **Pydantic** (Validação e serialização de dados)
* **SQLite** (Banco de dados relacional leve)
* **Uvicorn** (Servidor ASGI)

## ⚙️ Como Executar Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com
   cd catalogo-series-api
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Acesse a documentação interativa no navegador:
   * **Swagger UI:** `http://127.0.0`
