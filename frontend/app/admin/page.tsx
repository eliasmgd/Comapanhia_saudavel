import { Nav } from "../../components/Nav";

async function getDashboard() {
  const baseUrl = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

  try {
    const response = await fetch(`${baseUrl}/admin/dashboard`, { cache: "no-store" });
    if (!response.ok) {
      return null;
    }
    return response.json();
  } catch {
    return null;
  }
}

export default async function AdminPage() {
  const dashboard = await getDashboard();

  return (
    <main className="container">
      <Nav />
      <div className="card">
        <h2>Painel Administrativo</h2>
        <p className="muted">Gestão de perfis, aprovações e solicitações.</p>
        {dashboard ? (
          <ul>
            <li>Usuários cadastrados: {dashboard.users}</li>
            <li>Cuidadores: {dashboard.caregivers}</li>
            <li>Solicitações em aberto: {dashboard.open_requests}</li>
            <li>Registros de auditoria: {dashboard.audit_logs}</li>
          </ul>
        ) : (
          <p>API indisponível no momento.</p>
        )}
      </div>
    </main>
  );
}
