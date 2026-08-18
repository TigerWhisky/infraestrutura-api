from sqlalchemy.orm import Session
from app import models, schemas

# ==================== SERVERS ====================
def get_server(db: Session, server_id: int):
    return db.query(models.Server).filter(models.Server.id == server_id).first()

def get_server_by_hostname(db: Session, hostname: str):
    return db.query(models.Server).filter(models.Server.hostname == hostname).first()

def get_servers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Server).offset(skip).limit(limit).all()

def create_server(db: Session, server: schemas.ServerCreate):
    db_server = models.Server(**server.model_dump())
    db.add(db_server)
    db.commit()
    db.refresh(db_server)
    return db_server

def update_server(db: Session, server_id: int, server: schemas.ServerUpdate):
    db_server = get_server(db, server_id)
    if not db_server:
        return None
    update_data = server.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_server, key, value)
    db.commit()
    db.refresh(db_server)
    return db_server

def delete_server(db: Session, server_id: int):
    db_server = get_server(db, server_id)
    if not db_server:
        return None
    db.delete(db_server)
    db.commit()
    return db_server

# ==================== NETWORKS ====================
def get_network(db: Session, network_id: int):
    return db.query(models.Network).filter(models.Network.id == network_id).first()

def get_networks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Network).offset(skip).limit(limit).all()

def create_network(db: Session, network: schemas.NetworkCreate):
    db_network = models.Network(**network.model_dump())
    db.add(db_network)
    db.commit()
    db.refresh(db_network)
    return db_network

def update_network(db: Session, network_id: int, network: schemas.NetworkUpdate):
    db_network = get_network(db, network_id)
    if not db_network:
        return None
    update_data = network.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_network, key, value)
    db.commit()
    db.refresh(db_network)
    return db_network

def delete_network(db: Session, network_id: int):
    db_network = get_network(db, network_id)
    if not db_network:
        return None
    db.delete(db_network)
    db.commit()
    return db_network

# ==================== SERVICES ====================
def get_service(db: Session, service_id: int):
    return db.query(models.Service).filter(models.Service.id == service_id).first()

def get_services(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Service).offset(skip).limit(limit).all()

def get_services_by_server(db: Session, server_id: int):
    return db.query(models.Service).filter(models.Service.server_id == server_id).all()

def create_service(db: Session, service: schemas.ServiceCreate):
    db_service = models.Service(**service.model_dump())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

def update_service(db: Session, service_id: int, service: schemas.ServiceUpdate):
    db_service = get_service(db, service_id)
    if not db_service:
        return None
    update_data = service.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_service, key, value)
    db.commit()
    db.refresh(db_service)
    return db_service

def delete_service(db: Session, service_id: int):
    db_service = get_service(db, service_id)
    if not db_service:
        return None
    db.delete(db_service)
    db.commit()
    return db_service
