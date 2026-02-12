"use client";

import { useState } from "react";
import { Nav } from "../../components/Nav";
import { post } from "../../lib/api";

export default function SolicitantePage() {
  const [message, setMessage] = useState("");

  async function onSubmit(formData: FormData) {
    setMessage("");
    const payload = {
      requester_id: Number(formData.get("requester_id")),
      patient_name: String(formData.get("patient_name")),
      location: String(formData.get("location")),
      details: String(formData.get("details"))
    };

    try {
      await post("/care-requests", payload);
      setMessage("Solicitação enviada com sucesso.");
    } catch {
      setMessage("Não foi possível enviar. Verifique o cadastro social.");
    }
  }

  return (
    <main className="container">
      <Nav />
      <div className="card">
        <h2>Fluxo do Solicitante</h2>
        <p className="muted">Landing → Login → Solicitar cuidador → Confirmação</p>
        <form action={onSubmit}>
          <label>
            ID do solicitante
            <input className="input" name="requester_id" required />
          </label>
          <label>
            Nome do paciente
            <input className="input" name="patient_name" required />
          </label>
          <label>
            Localização
            <input className="input" name="location" required />
          </label>
          <label>
            Detalhes do cuidado
            <textarea className="input" name="details" rows={5} required />
          </label>
          <button className="btn" type="submit">
            Enviar solicitação
          </button>
        </form>
        {message && <p>{message}</p>}
      </div>
    </main>
  );
}
