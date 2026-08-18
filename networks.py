from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/networks", tags=["Networks"])

@router.post("/", response_model=schemas.Network, status_code=status.HTTP_201_CREATED)
def create_network(network: schemas.NetworkCreate, db: Session = Depends(get_db)):
    return crud.create_network(db=db, network=network)

@router.get("/", response_model=List[schemas.Network])
def read_networks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_networks(db, skip=skip, limit=limit)

@router.get("/{network_id}", response_model=schemas.Network)
def read_network(network_id: int, db: Session = Depends(get_db)):
    db_network = crud.get_network(db, network_id=network_id)
    if db_network is None:
        raise HTTPException(status_code=404, detail="Rede não encontrada")
    return db_network

@router.put("/{network_id}", response_model=schemas.Network)
def update_network(network_id: int, network: schemas.NetworkUpdate, db: Session = Depends(get_db)):
    db_network = crud.update_network(db, network_id=network_id, network=network)
    if db_network is None:
        raise HTTPException(status_code=404, detail="Rede não encontrada")
    return db_network

@router.delete("/{network_id}", response_model=schemas.Network)
def delete_network(network_id: int, db: Session = Depends(get_db)):
    db_network = crud.delete_network(db, network_id=network_id)
    if db_network is None:
        raise HTTPException(status_code=404, detail="Rede não encontrada")
    return db_network
