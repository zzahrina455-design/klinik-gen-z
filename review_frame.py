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
            text="Survei Kepuasan Pasien",
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
            text="Form Survei Kepuasan",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 16, "bold"),
        ).grid(row=0, column=0, columnspan=2, sticky="w", padx=25, pady=(20, 5))

        Label(
            form,
            text="Silakan isi penilaian Anda terhadap pelayanan klinik.",
            bg=WHITE,
            fg=TEXT_SECONDARY,
            font=("Segoe UI", 10),
        ).grid(row=1, column=0, columnspan=2, sticky="w", padx=25, pady=(0, 20))

        # ==========================================
        # NAMA
        # ==========================================

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

        nilai = ["Sangat Baik", "Baik", "Cukup", "Kurang", "Sangat Kurang"]

        # ==========================================
        # PELAYANAN PETUGAS
        # ==========================================

        Label(
            form,
            text="Pelayanan Petugas",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=3, column=0, sticky="w", padx=25, pady=8)

        self.pelayanan = ttk.Combobox(
            form,
            values=nilai,
            state="readonly",
            width=32,
        )

        self.pelayanan.grid(row=3, column=1, padx=25, pady=8)

        # ==========================================
        # KEBERSIHAN
        # ==========================================

        Label(
            form,
            text="Kebersihan Klinik",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=4, column=0, sticky="w", padx=25, pady=8)

        self.kebersihan = ttk.Combobox(
            form,
            values=nilai,
            state="readonly",
            width=32,
        )

        self.kebersihan.grid(row=4, column=1, padx=25, pady=8)

        # ==========================================
        # KENYAMANAN
        # ==========================================

        Label(
            form,
            text="Kenyamanan",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=5, column=0, sticky="w", padx=25, pady=8)

        self.kenyamanan = ttk.Combobox(
            form,
            values=nilai,
            state="readonly",
            width=32,
        )

        self.kenyamanan.grid(row=5, column=1, padx=25, pady=8)

        # ==========================================
        # KECEPATAN
        # ==========================================

        Label(
            form,
            text="Kecepatan Pelayanan",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=6, column=0, sticky="w", padx=25, pady=8)

        self.kecepatan = ttk.Combobox(
            form,
            values=nilai,
            state="readonly",
            width=32,
        )

        self.kecepatan.grid(row=6, column=1, padx=25, pady=8)

        # ==========================================
        # BERSEDIA KEMBALI
        # ==========================================

        Label(
            form,
            text="Akan Berobat Kembali?",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=7, column=0, sticky="w", padx=25, pady=8)

        self.kembali = StringVar()

        radio = Frame(form, bg=WHITE)
        radio.grid(row=7, column=1, sticky="w", padx=25, pady=8)

        Radiobutton(
            radio,
            text="Ya",
            variable=self.kembali,
            value="Ya",
            bg=WHITE,
        ).pack(side=LEFT)

        Radiobutton(
            radio,
            text="Tidak",
            variable=self.kembali,
            value="Tidak",
            bg=WHITE,
        ).pack(side=LEFT, padx=15)

        # ==========================================
        # SARAN
        # ==========================================

        Label(
            form,
            text="Saran & Masukan",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=8, column=0, sticky="nw", padx=25, pady=8)

        self.saran = Text(
            form,
            width=28,
            height=5,
            font=("Segoe UI", 10),
        )

        self.saran.grid(row=8, column=1, padx=25, pady=8)

        # ==========================================
        # BUTTON
        # ==========================================

        Button(
            form,
            text="Kirim Survei",
            bg=PRIMARY,
            fg="white",
            relief="flat",
            font=("Segoe UI", 10, "bold"),
            width=22,
            command=self.simpan,
        ).grid(row=9, column=0, columnspan=2, pady=25)

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
            text="😊",
            bg=WHITE,
            font=("Segoe UI Emoji", 70),
        ).pack(pady=(25, 10))

        Label(
            right,
            text="Survei Kepuasan",
            bg=WHITE,
            fg=PRIMARY,
            font=("Segoe UI", 16, "bold"),
        ).pack()

        Label(
            right,
            text="Masukan Anda sangat\nmembantu kami meningkatkan\nkualitas pelayanan klinik.",
            bg=WHITE,
            fg=TEXT_SECONDARY,
            justify="center",
            font=("Segoe UI", 10),
        ).pack(pady=10)

        Label(
            right,
            text="✔ Mudah\n✔ Cepat\n✔ Rahasia",
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
        pelayanan = self.pelayanan.get().strip()
        kebersihan = self.kebersihan.get().strip()
        kenyamanan = self.kenyamanan.get().strip()
        kecepatan = self.kecepatan.get().strip()
        kembali = self.kembali.get().strip()
        saran = self.saran.get("1.0", END).strip()

        if (
            nama == ""
            or pelayanan == ""
            or kebersihan == ""
            or kenyamanan == ""
            or kecepatan == ""
            or kembali == ""
        ):
            messagebox.showwarning("Peringatan", "Semua data harus diisi!")
            return

        try:

            self.db.execute(
                """
                INSERT INTO review
                (
                    nama,
                    pelayanan_petugas,
                    kebersihan,
                    kenyamanan,
                    kecepatan,
                    akan_kembali,
                    saran
                )
                VALUES
                (?,?,?,?,?,?,?)
                """,
                (
                    nama,
                    pelayanan,
                    kebersihan,
                    kenyamanan,
                    kecepatan,
                    kembali,
                    saran,
                ),
            )

            messagebox.showinfo(
                "Berhasil", "Terima kasih atas survei yang telah Anda isi."
            )

            self.reset_form()

        except Exception as e:

            messagebox.showerror("Error", str(e))

    # =====================================================
    # RESET FORM
    # =====================================================

    def reset_form(self):

        self.nama.delete(0, END)

        self.pelayanan.set("")

        self.kebersihan.set("")

        self.kenyamanan.set("")

        self.kecepatan.set("")

        self.kembali.set("")

        self.saran.delete("1.0", END)

    # =====================================================
    # KEMBALI
    # =====================================================

    def kembali_dashboard(self):

        self.master.clear_frame()

        from dashboard_frame import DashboardFrame

        DashboardFrame(self.master)
