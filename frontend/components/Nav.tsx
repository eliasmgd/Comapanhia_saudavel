import Link from "next/link";

export function Nav() {
  return (
    <nav className="nav">
      <Link href="/">Landing</Link>
      <Link href="/solicitante">Solicitante</Link>
      <Link href="/cuidador">Cuidador</Link>
      <Link href="/admin">Admin</Link>
    </nav>
  );
}
