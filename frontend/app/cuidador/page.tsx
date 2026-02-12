"use client";

import { useState } from "react";
import { Nav } from "../../components/Nav";
import { post } from "../../lib/api";

export default function CuidadorPage() {
  const [feedback, setFeedback] = useState("");

  async function onSubmit(formData: FormData) {
    setFeedback("");

    try {
      await post("/caregivers", {
        user_id: Number(formData.get("user_id")),
        specialties: String(formData.get("specialties")),
        bio: String(formData.get("bio")),
        city: String(formData.get("city"))
      });
      setFeedback("Cadastro realizado. Aguarde aprovação do administrador.");
    } catch {
      setFeedback("Erro ao cadastrar. Faça login social como cuidador antes.");
    }
  }

  return (
    <main className="container">
      <Nav />
      <div className="card">
        <h2>Fluxo do Cuidador</h2>
        <p className="muted">Landing → Login → Cadastro → Aprovação → Receber solicitações</p>
        <form action={onSubmit}>
          <label>
            ID do usuário cuidador
            <input className="input" name="user_id" required />
          </label>
          <label>
            Especialidades
            <input className="input" name="specialties" required />
          </label>
          <label>
            Cidade
            <input className="input" name="city" required />
          </label>
          <label>
            Biografia
            <textarea className="input" name="bio" rows={5} required />
          </label>
          <button className="btn" type="submit">
            Enviar cadastro
          </button>
        </form>
        {feedback && <p>{feedback}</p>}
      </div>
    </main>
  );
}
