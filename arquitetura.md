# Arquitetura
## Visão Geral

A app segue uma arquitetura em camadas:

1. **Routers** → recebem os pedidos HTTP
2. **Schemas (Pydantic)** → validação e serialização
3. **CRUD** → lógica de acesso à base de dados
4. **Models (SQLAlchemy)** → mapeamento objeto-relacional
5. **Database** → ligação ao MySQL

## Diagrama de Entidades

- **Server** 1 ── * **Service**
- **Network** (entidade independente)
