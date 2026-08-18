from fastapi import FastAPI
from app.database import engine, Base
from app.routers import servers, networks, services

# Criar as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Infraestrutura API",
    description="API REST para Gestão de Infraestrutura (Servers, Networks, Services)",
    version="1.0.0",
    contact={
        "name": "Engenharia Informática",
    },
)

app.include_router(servers.router)
app.include_router(networks.router)
app.include_router(services.router)

@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Infraestrutura API está a funcionar",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
