import axios from "axios";

const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8000";

export const submitTransaction = async (user, jumlah) => {
  const res = await axios.post(`${API_BASE}/transaksi`, {
    nama: user,
    jumlah_pembelian: jumlah,
  });
  return res.data;
};
