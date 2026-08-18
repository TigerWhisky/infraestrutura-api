# Infraestrutura API

API REST desenvolvida em **FastAPI** para gestão de infraestrutura (servidores, redes e serviços), em **MySQL** e ambiente containerizado com **Docker**.

## Objetivos

- Criar uma API REST limpa- Utilizar FastAPI + SQLAlchemy + Pydantic
- Gerir entidades de infraestrutura (Servers, Networks, Services)
- Fornecer ambiente de desenvolvimento com Docker Compose
- Documentação automática (Swagger / ReDoc)

## Tecnologias

- **Python 3.11+**
- **FastAPI**
- **SQLAlchemy**
- **MySQL 8**
- **Docker & Docker Compose**
- **Pydantic**
- **Uvicorn**

## Estrutura

| Pasta / Ficheiro        | Descrição                          |
|-------------------------|------------------------------------|
| `app/`                  | Código da aplicação                |
| `app/routers/`          | Endpoints organizados por recurso  |
| `docs/`                 | Documentação adicional             |
| `docker-compose.yml`    | Organização dos serviços          |
| `Dockerfile`            | Imagem da API                      |

## Arranque Rápido (com Docker)

```bash
# 1. Clonar o repositório
git clone https://github.com/TigerWhisky/infraestrutura-api.git
cd infraestrutura-api

# 2. Copiar variáveis de ambiente
cp .env.example .env

# 3. Subir tudo (MySQL + API)
docker compose up --build

A API fica disponível em:

API: http://localhost:8000
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

Endpoints Principais
Servers

GET    /servers/
POST   /servers/
GET    /servers/{id}
PUT    /servers/{id}
DELETE /servers/{id}

Networks

GET    /networks/
POST   /networks/
GET    /networks/{id}
PUT    /networks/{id}
DELETE /networks/{id}

Services

GET    /services/
POST   /services/
GET    /services/{id}
PUT    /services/{id}
DELETE /services/{id}

Desenvolvimento local (sem Docker)
Bashpython -m venv venv
source venv/bin/activate   # ou venv\Scripts\activate no Windows
pip install -r requirements.txt

# Garantir que o MySQL está a correr e as variáveis no .env estão corretas
uvicorn app.main:app --reload
