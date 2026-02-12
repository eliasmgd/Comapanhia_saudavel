import Link from "next/link";

import { FeatureCard } from "@/components/FeatureCard";

const features = [
  {
    title: "Solicitação rápida",
    description: "Famílias podem abrir solicitações com detalhes clínicos em minutos.",
  },
  {
    title: "Cuidadores validados",
    description: "Perfis passam por aprovação administrativa e compliance LGPD.",
  },
  {
    title: "Gestão em tempo real",
    description: "Equipe administrativa acompanha status e logs de auditoria.",
  },
];

export default function HomePage() {
  return (
    <main className="container">
      <header className="hero">
        <p className="tag">Plataforma digital de cuidado humanizado</p>
        <h1>Companhia Saudável</h1>
        <p>Conectamos familiares e cuidadores qualificados com segurança e escala.</p>
        <nav>
          <Link href="/solicitante">Sou familiar</Link>
          <Link href="/cuidador">Sou cuidador</Link>
          <Link href="/admin">Painel admin</Link>
        </nav>
      </header>

      <section className="grid">
        {features.map((feature) => (
          <FeatureCard key={feature.title} title={feature.title} description={feature.description} />
        ))}
      </section>
    </main>
  );
}
