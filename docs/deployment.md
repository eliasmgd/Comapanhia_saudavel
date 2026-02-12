# Plano de execução local e produção

## 1) Pré-requisitos

- Docker + Docker Compose plugin
- Git
- Porta livre: `3000`, `8000`, `5432`

## 2) Execução local com Docker

### Passo a passo

1. Copiar variáveis do backend:

```bash
cp backend/.env.example backend/.env
```

2. Subir a stack:

```bash
docker compose up --build
```

3. Validar serviços:

- Frontend: `http://localhost:3000`
- Backend health: `http://localhost:8000/health`
- Banco: `localhost:5432`

4. Derrubar stack:

```bash
docker compose down
```

5. Derrubar stack e volumes (reset completo do banco):

```bash
docker compose down -v
```

## 3) Variáveis de ambiente (produção)

### Backend

- `APP_NAME`: nome da API.
- `ENVIRONMENT`: `production`.
- `SECRET_KEY`: chave forte para JWT.
- `DATABASE_URL`: URL PostgreSQL.
- `ACCESS_TOKEN_EXPIRE_MINUTES`: tempo de expiração do token.
- `FRONTEND_URL`: URL pública do frontend (CORS).

### Frontend

- `NEXT_PUBLIC_API_URL`: URL pública da API.

## 4) Estratégia de produção recomendada

### Opção A (mais simples): Render + Vercel

- **Backend (Render Web Service):**
  - Build: `pip install -r requirements.txt`
  - Start: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
  - Root Dir: `backend`
  - Variáveis: todas do backend
- **Banco (Render Postgres):**
  - usar `Internal Database URL` como `DATABASE_URL`
- **Frontend (Vercel):**
  - Root Dir: `frontend`
  - Env: `NEXT_PUBLIC_API_URL=https://api.seudominio.com`

### Opção B: AWS ECS Fargate (frontend e backend em containers)

- Criar imagens no ECR para `backend` e `frontend`.
- Subir API em ECS Service + ALB.
- Subir frontend em ECS Service (ou manter em Vercel para simplificar).
- Banco em RDS PostgreSQL.
- Segredos em AWS Secrets Manager/SSM.

## 5) Checklist de hardening antes de ir para produção

- Trocar `SECRET_KEY` por valor forte e único.
- Configurar domínio e HTTPS (certificado TLS).
- Configurar CORS apenas para domínio real (`FRONTEND_URL`).
- Habilitar backups e retenção do PostgreSQL.
- Adicionar observabilidade (logs estruturados e alertas).
- Planejar migrações com Alembic (evitar `create_all` em produção).

## 6) Troubleshooting rápido

- Erro de conexão no backend com banco:
  - conferir `DATABASE_URL` e saúde do serviço `db`.
- Frontend não chama API:
  - verificar `NEXT_PUBLIC_API_URL` e CORS (`FRONTEND_URL`).
- Falha no build Docker:
  - validar acesso à internet/registry para baixar dependências.
