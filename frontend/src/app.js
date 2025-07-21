import React, { useState } from "react";
import { submitTransaction } from "./api";
import Receipt from "./components/Receipt";
import "./styles.css";

function App() {
  const [nama, setNama] = useState("");
  const [jumlah, setJumlah] = useState(1);
  const [nota, setNota] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await submitTransaction(nama, jumlah);
    setNota(res);
  };

  return (
    <div className="container">
      <h1>Coffeepoint</h1>
      <form onSubmit={handleSubmit}>
        <input value={nama} onChange={(e) => setNama(e.target.value)} placeholder="Nama pelanggan" required />
        <input type="number" value={jumlah} onChange={(e) => setJumlah(Number(e.target.value))} min="1" />
        <button type="submit">Kirim</button>
      </form>

      {nota && <Receipt nota={nota} />}
    </div>
  );
}

export default App;
