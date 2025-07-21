import React from "react";
import QRCode from "qrcode.react";

export default function Receipt({ nota }) {
  return (
    <div className="receipt">
      <h2>Nota Pembelian</h2>
      <p>Nama: {nota.nama}</p>
      <p>Jumlah: {nota.jumlah_pembelian}</p>
      <p>Poin: {nota.poin}</p>
      <p>Voucher: {nota.voucher ? "✅ Dapat" : "❌ Belum"}</p>
      <QRCode value={JSON.stringify(nota)} />
    </div>
  );
}
