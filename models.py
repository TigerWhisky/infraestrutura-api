from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum

class ServerStatus(str, enum.Enum):
    online = "online"
    offline = "offline"
    maintenance = "maintenance"

class ServiceStatus(str, enum.Enum):
    running = "running"
    stopped = "stopped"
    error = "error"

class Server(Base):
    __tablename__ = "servers"

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String(100), unique=True, nullable=False, index=True)
    ip_address = Column(String(45), nullable=False)
    operating_system = Column(String(100))
    status = Column(Enum(ServerStatus), default=ServerStatus.offline)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    services = relationship("Service", back_populates="server", cascade="all, delete-orphan")

class Network(Base):
    __tablename__ = "networks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    cidr = Column(String(50), nullable=False)          # ex: 192.168.1.0/24
    gateway = Column(String(45), nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    port = Column(Integer, nullable=False)
    status = Column(Enum(ServiceStatus), default=ServiceStatus.stopped)
    server_id = Column(Integer, ForeignKey("servers.id"), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    server = relationship("Server", back_populates="services")
