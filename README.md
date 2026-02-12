# Companhia Saudável

MVP full-stack da plataforma **Companhia Saudável**, conectando familiares, cuidadores e administradores com foco em segurança, UX e escalabilidade.

## Arquitetura

- **Back-end**: FastAPI + SQLAlchemy.
- **Front-end**: Next.js (App Router).
- **Banco**: PostgreSQL em produção (SQLite default para desenvolvimento local).
- **Autenticação**: login por e-mail/senha com endpoint preparado para provedores OAuth.

## Estrutura

```bash
backend/
  app/
    core/        # Configurações
    routers/     # Endpoints por domínio
    services/    # Segurança
    models.py    # Entidades principais
frontend/
  app/           # Rotas da aplicação web
  components/    # Componentes reutilizáveis
docs/
  deployment.md  # Plano local/produção com Docker
```

## Execução local rápida (Docker)

```bash
cp backend/.env.example backend/.env
docker compose up --build
```

- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- Health: http://localhost:8000/health

Para mais detalhes de ambiente local e produção, veja `docs/deployment.md`.

## Execução sem Docker

### Back-end

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Front-end

```bash
cd frontend
npm install
npm run dev
```

## Fluxos implementados

- Landing page com jornadas por perfil.
- Cadastro e login.
- Cadastro de perfil de cuidador.
- Criação e listagem de solicitações.
- Aprovação de cuidadores e atualização de status via admin.
- Health check e base de testes automatizados.

## Roadmap sugerido

1. OAuth completo com Google/Facebook/Instagram.
2. Módulo de pagamentos.
3. Avaliações e reputação.
4. Chat interno e notificações em tempo real.
