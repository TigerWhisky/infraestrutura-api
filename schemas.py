from pydantic import BaseModel, Field, IPvAnyAddress
from typing import Optional, List
from datetime import datetime
from enum import Enum

class ServerStatus(str, Enum):
    online = "online"
    offline = "offline"
    maintenance = "maintenance"

class ServiceStatus(str, Enum):
    running = "running"
    stopped = "stopped"
    error = "error"

# ========== Server ==========
class ServerBase(BaseModel):
    hostname: str = Field(..., min_length=1, max_length=100)
    ip_address: str
    operating_system: Optional[str] = None
    status: ServerStatus = ServerStatus.offline
    description: Optional[str] = None

class ServerCreate(ServerBase):
    pass

class ServerUpdate(BaseModel):
    hostname: Optional[str] = None
    ip_address: Optional[str] = None
    operating_system: Optional[str] = None
    status: Optional[ServerStatus] = None
    description: Optional[str] = None

class Server(ServerBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# ========== Network ==========
class NetworkBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    cidr: str
    gateway: Optional[str] = None
    description: Optional[str] = None

class NetworkCreate(NetworkBase):
    pass

class NetworkUpdate(BaseModel):
    name: Optional[str] = None
    cidr: Optional[str] = None
    gateway: Optional[str] = None
    description: Optional[str] = None

class Network(NetworkBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# ========== Service ==========
class ServiceBase(BaseModel):
    name: str
    port: int = Field(..., ge=1, le=65535)
    status: ServiceStatus = ServiceStatus.stopped
    server_id: int
    description: Optional[str] = None

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    port: Optional[int] = Field(None, ge=1, le=65535)
    status: Optional[ServiceStatus] = None
    server_id: Optional[int] = None
    description: Optional[str] = None

class Service(ServiceBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
