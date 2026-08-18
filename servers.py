from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/servers", tags=["Servers"])

@router.post("/", response_model=schemas.Server, status_code=status.HTTP_201_CREATED)
def create_server(server: schemas.ServerCreate, db: Session = Depends(get_db)):
    db_server = crud.get_server_by_hostname(db, hostname=server.hostname)
    if db_server:
        raise HTTPException(status_code=400, detail="Hostname já registado")
    return crud.create_server(db=db, server=server)

@router.get("/", response_model=List[schemas.Server])
def read_servers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_servers(db, skip=skip, limit=limit)

@router.get("/{server_id}", response_model=schemas.Server)
def read_server(server_id: int, db: Session = Depends(get_db)):
    db_server = crud.get_server(db, server_id=server_id)
    if db_server is None:
        raise HTTPException(status_code=404, detail="Servidor não encontrado")
    return db_server

@router.put("/{server_id}", response_model=schemas.Server)
def update_server(server_id: int, server: schemas.ServerUpdate, db: Session = Depends(get_db)):
    db_server = crud.update_server(db, server_id=server_id, server=server)
    if db_server is None:
        raise HTTPException(status_code=404, detail="Servidor não encontrado")
    return db_server

@router.delete("/{server_id}", response_model=schemas.Server)
def delete_server(server_id: int, db: Session = Depends(get_db)):
    db_server = crud.delete_server(db, server_id=server_id)
    if db_server is None:
        raise HTTPException(status_code=404, detail="Servidor não encontrado")
    return db_server
