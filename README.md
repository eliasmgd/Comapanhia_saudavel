# Companhia Saudável

MVP da plataforma para conectar familiares de pacientes com cuidadores qualificados.

## Arquitetura

- **Back-end**: FastAPI + SQLAlchemy + PostgreSQL.
- **Front-end**: Next.js (App Router) com layout responsivo.
- **Autenticação**: endpoint de login social preparado para `google`, `facebook` e `instagram`.
- **Perfis**: solicitante, cuidador e administrador.
- **Governança**: logs de auditoria para ações relevantes.

## Estrutura

```
backend/
  app/
    main.py
    models.py
    schemas.py
    database.py
frontend/
  app/
    page.tsx
    solicitante/page.tsx
    cuidador/page.tsx
    admin/page.tsx
```

## Back-end

### Executar

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Variáveis

- `DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/companhia_saudavel`

### Principais endpoints

- `POST /auth/social`: cadastro/login social.
- `POST /caregivers`: cadastro de cuidador.
- `PATCH /admin/caregivers/{id}`: aprovação ou rejeição de cuidador.
- `POST /care-requests`: abertura de solicitação de cuidado.
- `PATCH /care-requests/{id}`: atualização de status.
- `GET /admin/dashboard`: visão consolidada do painel administrativo.

## Front-end

### Executar

```bash
cd frontend
npm install
npm run dev
```

Configure `NEXT_PUBLIC_API_URL` para o endereço da API FastAPI.

## Roadmap futuro

- Integração com pagamentos.
- Sistema de avaliações.
- Chat interno em tempo real.
