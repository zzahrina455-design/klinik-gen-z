from tkinter import *
from tkinter import ttk, messagebox

from style import *
from components import Sidebar
from database import Database


class ReviewFrame(Frame):

    def __init__(self, master):
        super().__init__(master, bg=BACKGROUND)
        self.pack(fill="both", expand=True)

        self.db = Database()

        # ======================================================
        # SIDEBAR
        # ======================================================

        Sidebar(self, master, "review").pack(side=LEFT, fill=Y)

        # ======================================================
        # CONTENT
        # ======================================================

        content = Frame(self, bg=BACKGROUND)
        content.pack(side=LEFT, fill=BOTH, expand=True)

        # ======================================================
        # HEADER
        # ======================================================

        header = Frame(
            content,
            bg=WHITE,
            height=80,
            highlightbackground=BORDER,
            highlightthickness=1,
        )

        header.pack(fill=X)
        header.pack_propagate(False)

        Label(
            header,
            text="Survei Pemeriksaan Pasien",
            bg=WHITE,
            fg=TEXT,
            font=TITLE_FONT,
        ).pack(anchor="w", padx=25, pady=(15, 0))

        # ======================================================
        # BODY
        # ======================================================

        body = Frame(content, bg=BACKGROUND)
        body.pack(fill=BOTH, expand=True, padx=20, pady=20)

        top = Frame(body, bg=BACKGROUND)
        top.pack(fill=BOTH, expand=True)

        # ======================================================
        # FORM CARD
        # ======================================================

        form = Frame(
            top,
            bg=WHITE,
            highlightbackground=BORDER,
            highlightthickness=1,
        )

        form.pack(side=LEFT, fill=BOTH, expand=True)

        Label(
            form,
            text="Form Survei Pasien",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 16, "bold"),
        ).grid(row=0, column=0, columnspan=2, sticky="w", padx=25, pady=(20, 5))

        Label(
            form,
            text="Isi data pemeriksaan awal pasien.",
            bg=WHITE,
            fg=TEXT_SECONDARY,
            font=("Segoe UI", 10),
        ).grid(row=1, column=0, columnspan=2, sticky="w", padx=25, pady=(0, 20))

        # ======================================================
        # NAMA PASIEN
        # ======================================================

        Label(
            form,
            text="Nama Pasien",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=2, column=0, sticky="w", padx=25, pady=8)

        self.nama = Entry(
            form,
            width=35,
            font=("Segoe UI", 10),
        )

        self.nama.grid(row=2, column=1, padx=25, pady=8)

        # ======================================================
        # KELUHAN
        # ======================================================

        Label(
            form,
            text="Keluhan Utama",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=3, column=0, sticky="nw", padx=25, pady=8)

        self.keluhan = Text(
            form,
            width=28,
            height=3,
            font=("Segoe UI", 10),
        )

        self.keluhan.grid(row=3, column=1, padx=25, pady=8)

        # ======================================================
        # RIWAYAT PENYAKIT
        # ======================================================

        Label(
            form,
            text="Riwayat Penyakit",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=4, column=0, sticky="nw", padx=25, pady=8)

        self.riwayat = Text(
            form,
            width=28,
            height=3,
            font=("Segoe UI", 10),
        )

        self.riwayat.grid(row=4, column=1, padx=25, pady=8)

        # ======================================================
        # ALERGI
        # ======================================================

        Label(
            form,
            text="Alergi",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=5, column=0, sticky="w", padx=25, pady=8)

        self.alergi = Entry(
            form,
            width=35,
            font=("Segoe UI", 10),
        )

        self.alergi.grid(row=5, column=1, padx=25, pady=8)

        # ======================================================
        # SUHU
        # ======================================================

        Label(
            form,
            text="Suhu Tubuh",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=6, column=0, sticky="w", padx=25, pady=8)

        self.suhu = Entry(
            form,
            width=35,
            font=("Segoe UI", 10),
        )

        self.suhu.grid(row=6, column=1, padx=25, pady=8)

        # ======================================================
        # TEKANAN DARAH
        # ======================================================

        Label(
            form,
            text="Tekanan Darah",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=7, column=0, sticky="w", padx=25, pady=8)

        self.tekanan = Entry(
            form,
            width=35,
            font=("Segoe UI", 10),
        )

        self.tekanan.grid(row=7, column=1, padx=25, pady=8)

        # ======================================================
        # BERAT BADAN
        # ======================================================

        Label(
            form,
            text="Berat Badan (Kg)",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=8, column=0, sticky="w", padx=25, pady=8)

        self.berat = Entry(
            form,
            width=35,
            font=("Segoe UI", 10),
        )

        self.berat.grid(row=8, column=1, padx=25, pady=8)

        # ======================================================
        # TINGGI BADAN
        # ======================================================

        Label(
            form,
            text="Tinggi Badan (Cm)",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=9, column=0, sticky="w", padx=25, pady=8)

        self.tinggi = Entry(
            form,
            width=35,
            font=("Segoe UI", 10),
        )

        self.tinggi.grid(row=9, column=1, padx=25, pady=8)

        # ======================================================
        # BUTTON
        # ======================================================

        Button(
            form,
            text="Simpan Survei",
            bg=PRIMARY,
            fg="white",
            relief="flat",
            width=22,
            font=("Segoe UI", 10, "bold"),
            command=self.simpan,
        ).grid(
            row=10,
            column=0,
            columnspan=2,
            pady=25,
        )

        # ======================================================
        # PANEL KANAN
        # ======================================================

        right = Frame(
            top,
            bg=WHITE,
            width=280,
            highlightbackground=BORDER,
            highlightthickness=1,
        )

        right.pack(side=LEFT, fill=Y, padx=(20, 0))

        right.pack_propagate(False)

        Label(
            right,
            text="🩺",
            bg=WHITE,
            font=("Segoe UI Emoji", 70),
        ).pack(pady=(25, 10))

        Label(
            right,
            text="Pemeriksaan Awal",
            bg=WHITE,
            fg=PRIMARY,
            font=("Segoe UI", 16, "bold"),
        ).pack()

        Label(
            right,
            text="Lengkapi data kesehatan\npasien sebelum diperiksa dokter.",
            bg=WHITE,
            fg=TEXT_SECONDARY,
            justify="center",
            font=("Segoe UI", 10),
        ).pack(pady=10)

        Label(
            right,
            text="✔ Lengkap\n✔ Cepat\n✔ Akurat",
            bg=WHITE,
            fg=SUCCESS,
            justify="left",
            font=("Segoe UI", 11),
        ).pack(pady=20)

    # =====================================================
    # SIMPAN SURVEI
    # =====================================================

    def simpan(self):

        nama = self.nama.get().strip()
        keluhan = self.keluhan.get("1.0", END).strip()
        riwayat = self.riwayat.get("1.0", END).strip()
        alergi = self.alergi.get().strip()
        suhu = self.suhu.get().strip()
        tekanan = self.tekanan.get().strip()
        berat = self.berat.get().strip()
        tinggi = self.tinggi.get().strip()

        if (
            nama == ""
            or keluhan == ""
            or riwayat == ""
            or alergi == ""
            or suhu == ""
            or tekanan == ""
            or berat == ""
            or tinggi == ""
        ):
            messagebox.showwarning("Peringatan", "Semua data harus diisi!")
            return

        try:

            self.db.execute(
                """
                INSERT INTO review
                (
                    nama,
                    keluhan,
                    riwayat,
                    alergi,
                    suhu,
                    tekanan_darah,
                    berat_badan,
                    tinggi_badan
                )
                VALUES
                (?,?,?,?,?,?,?,?)
                """,
                (nama, keluhan, riwayat, alergi, suhu, tekanan, berat, tinggi),
            )

            messagebox.showinfo("Berhasil", "Data survei berhasil disimpan.")

            self.reset_form()

        except Exception as e:

            messagebox.showerror("Error", str(e))

    # =====================================================
    # RESET FORM
    # =====================================================

    def reset_form(self):

        self.nama.delete(0, END)

        self.keluhan.delete("1.0", END)

        self.riwayat.delete("1.0", END)

        self.alergi.delete(0, END)

        self.suhu.delete(0, END)

        self.tekanan.delete(0, END)

        self.berat.delete(0, END)

        self.tinggi.delete(0, END)

    # =====================================================
    # KEMBALI
    # =====================================================

    def kembali(self):

        self.master.clear_frame()

        from dashboard_frame import DashboardFrame

        DashboardFrame(self.master)
