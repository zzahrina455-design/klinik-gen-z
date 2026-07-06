import tkinter as tk
from tkinter import ttk, messagebox
from models import SurveyModel


class SurveyFrame(tk.Toplevel):

    def __init__(self, master, pasien):
        super().__init__(master)

        self.title("Survey Kepuasan")
        self.geometry("460x580")
        self.resizable(False, False)
        self.configure(bg="#EBF1FA")

        self.model = SurveyModel()
        self.pasien = pasien

        # Membuat jendela pop-up muncul di tengah-tengah layar utama
        self.transient(master)
        self.grab_set()

        # ==========================================
        # CARD CONTAINER
        # ==========================================
        card_content = tk.Frame(
            self,
            bg="#FFFFFF",
            padx=30,
            pady=25,
            highlightbackground="#E2E8F0",
            highlightthickness=1,
        )
        card_content.pack(fill=tk.BOTH, expand=True, padx=25, pady=25)

        # Header Title
        tk.Label(
            card_content,
            text="Survey Kepuasan",
            font=("Arial", 18, "bold"),
            fg="#0F172A",
            bg="#FFFFFF",
        ).pack(pady=(0, 5))

        tk.Label(
            card_content,
            text="Penilaian Anda membantu kami meningkatkan layanan",
            font=("Arial", 9),
            fg="#94A3B8",
            bg="#FFFFFF",
        ).pack(pady=(0, 20))

        # ==========================================
        # INPUT FORM CRITERIA
        # ==========================================

        # 1. Pelayanan
        tk.Label(
            card_content,
            text="Pelayanan Klinik",
            font=("Arial", 10, "bold"),
            fg="#334155",
            bg="#FFFFFF",
        ).pack(anchor="w", pady=(5, 2))
        self.pelayanan = ttk.Combobox(
            card_content,
            values=[1, 2, 3, 4, 5],
            state="readonly",
            font=("Arial", 10)
        )
        self.pelayanan.current(4)
        self.pelayanan.pack(fill=tk.X, pady=(0, 12))

        # 2. Kebersihan
        tk.Label(
            card_content,
            text="Kebersihan Fasilitas",
            font=("Arial", 10, "bold"),
            fg="#334155",
            bg="#FFFFFF",
        ).pack(anchor="w", pady=(5, 2))
        self.kebersihan = ttk.Combobox(
            card_content,
            values=[1, 2, 3, 4, 5],
            state="readonly",
            font=("Arial", 10)
        )
        self.kebersihan.current(4)
        self.kebersihan.pack(fill=tk.X, pady=(0, 12))

        # 3. Keramahan
        tk.Label(
            card_content,
            text="Keramahan Staf & Dokter",
            font=("Arial", 10, "bold"),
            fg="#334155",
            bg="#FFFFFF",
        ).pack(anchor="w", pady=(5, 2))
        self.keramahan = ttk.Combobox(
            card_content,
            values=[1, 2, 3, 4, 5],
            state="readonly",
            font=("Arial", 10)
        )
        self.keramahan.current(4)
        self.keramahan.pack(fill=tk.X, pady=(0, 12))

        # 4. Kotak Saran
        tk.Label(
            card_content,
            text="Saran / Masukan Tambahan",
            font=("Arial", 10, "bold"),
            fg="#334155",
            bg="#FFFFFF",
        ).pack(anchor="w", pady=(5, 2))

        # Memberikan wrapper border abu-abu tipis untuk komponen Text
        saran_wrapper = tk.Frame(
            card_content,
            bg="#FFFFFF",
            highlightbackground="#E2E8F0",
            highlightthickness=1,
        )
        saran_wrapper.pack(fill=tk.BOTH, expand=True, pady=(0, 20))

        self.saran = tk.Text(
            saran_wrapper,
            font=("Arial", 10),
            bg="#FFFFFF",
            bd=0,
            fg="#0F172A",
            height=4,
            insertbackground="#0F172A",
        )
        self.saran.pack(fill=tk.BOTH, expand=True, padx=8, pady=6)

        # ==========================================
        # TOMBOL AKSI
        # ==========================================
        btn_kirim = tk.Button(
            card_content,
            text="🚀 Kirim Survey",
            font=("Arial", 11, "bold"),
            bg="#1A5CFF",  # Menggunakan warna biru utama agar serasi
            fg="#FFFFFF",
            activebackground="#0046E5",
            activeforeground="#FFFFFF",
            bd=0,
            cursor="hand2",
            command=self.kirim,
        )
        btn_kirim.pack(fill=tk.X, ipady=6)

    # ==========================================
    # LOGIC METHODS
    # ==========================================
    def kirim(self):
        self.model.simpan(
            self.pasien,
            int(self.pelayanan.get()),
            int(self.kebersihan.get()),
            int(self.keramahan.get()),
            self.saran.get("1.0", tk.END).strip(),
        )

        messagebox.showinfo(
            "Berhasil",
            "Terima kasih atas penilaian Anda.",
        )

        self.destroy()
