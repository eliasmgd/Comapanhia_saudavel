import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Companhia Saudável",
  description: "Plataforma para conectar familiares e cuidadores qualificados."
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}
