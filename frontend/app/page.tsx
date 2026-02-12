import { Nav } from "../components/Nav";

export default function LandingPage() {
  return (
    <main className="container">
      <Nav />
      <section className="hero card">
        <h1>Companhia Saudável</h1>
        <p className="muted">
          Atendimento humanizado para famílias que precisam de suporte em internações e
          pós-operatórios.
        </p>
        <div>
          <a className="btn" href="/solicitante">
            Solicitar cuidador
          </a>
        </div>
      </section>

      <section className="grid">
        <article className="card">
          <h3>Login Social</h3>
          <p className="muted">Google, Facebook e Instagram para onboarding rápido.</p>
        </article>
        <article className="card">
          <h3>Segurança e LGPD</h3>
          <p className="muted">Controle de permissões, logs de auditoria e minimização de dados.</p>
        </article>
        <article className="card">
          <h3>Escalabilidade</h3>
          <p className="muted">Arquitetura preparada para AWS, Render e Vercel.</p>
        </article>
      </section>
    </main>
  );
}
