from tkinter import *
from tkinter import ttk, messagebox

from style import *
from components import Sidebar
from database import Database


class AntrianFrame(Frame):

    def __init__(self, master):
        super().__init__(master, bg=BACKGROUND)
        self.pack(fill="both", expand=True)

        self.db = Database()

        # ======================================================
        # SIDEBAR
        # ======================================================

        Sidebar(self, master, "antrian").pack(side=LEFT, fill=Y)

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
            text="Form Data Pasien",
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
            text="Data Pasien",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 16, "bold"),
        ).grid(row=0, column=0, columnspan=2, sticky="w", padx=25, pady=(20, 5))

        Label(
            form,
            text="Isi seluruh data pasien dengan benar.",
            bg=WHITE,
            fg=TEXT_SECONDARY,
            font=("Segoe UI", 10),
        ).grid(row=1, column=0, columnspan=2, sticky="w", padx=25, pady=(0, 20))

        # ======================================================
        # NAMA
        # ======================================================

        Label(
            form,
            text="Nama Lengkap",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=2, column=0, sticky="w", padx=25, pady=8)

        self.nama = Entry(
            form,
            font=("Segoe UI", 10),
            width=35,
        )

        self.nama.grid(row=2, column=1, padx=25, pady=8)

        # ======================================================
        # NIK
        # ======================================================

        Label(
            form,
            text="NIK",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=3, column=0, sticky="w", padx=25, pady=8)

        self.nik = Entry(
            form,
            font=("Segoe UI", 10),
            width=35,
        )

        self.nik.grid(row=3, column=1, padx=25, pady=8)

        # ======================================================
        # UMUR
        # ======================================================

        Label(
            form,
            text="Umur",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=4, column=0, sticky="w", padx=25, pady=8)

        self.umur = Entry(
            form,
            font=("Segoe UI", 10),
            width=35,
        )

        self.umur.grid(row=4, column=1, padx=25, pady=8)

        # ======================================================
        # JENIS KELAMIN
        # ======================================================

        Label(
            form,
            text="Jenis Kelamin",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=5, column=0, sticky="w", padx=25, pady=8)

        self.jk = StringVar()

        jk_frame = Frame(form, bg=WHITE)
        jk_frame.grid(row=5, column=1, sticky="w", padx=25, pady=8)

        Radiobutton(
            jk_frame,
            text="Laki-laki",
            variable=self.jk,
            value="Laki-laki",
            bg=WHITE,
        ).pack(side=LEFT)

        Radiobutton(
            jk_frame,
            text="Perempuan",
            variable=self.jk,
            value="Perempuan",
            bg=WHITE,
        ).pack(side=LEFT, padx=15)

        # ======================================================
        # ALAMAT
        # ======================================================

        Label(
            form,
            text="Alamat",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=6, column=0, sticky="nw", padx=25, pady=8)

        self.alamat = Text(
            form,
            width=28,
            height=4,
            font=("Segoe UI", 10),
        )

        self.alamat.grid(row=6, column=1, padx=25, pady=8)

        # ======================================================
        # NO HP
        # ======================================================

        Label(
            form,
            text="No. HP",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=7, column=0, sticky="w", padx=25, pady=8)

        self.nohp = Entry(
            form,
            width=35,
            font=("Segoe UI", 10),
        )

        self.nohp.grid(row=7, column=1, padx=25, pady=8)

        # ======================================================
        # POLI
        # ======================================================

        Label(
            form,
            text="Poli Tujuan",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=8, column=0, sticky="w", padx=25, pady=8)

        self.poli = ttk.Combobox(
            form,
            state="readonly",
            width=32,
            values=[
                "Poli Umum",
                "Poli Gigi",
                "Poli Anak",
                "Poli Kandungan",
            ],
        )

        self.poli.grid(row=8, column=1, padx=25, pady=8)

        # ======================================================
        # DOKTER
        # ======================================================

        Label(
            form,
            text="Dokter",
            bg=WHITE,
            font=TEXT_FONT,
        ).grid(row=9, column=0, sticky="w", padx=25, pady=8)

        self.dokter = ttk.Combobox(
            form,
            state="readonly",
            width=32,
            values=[
                "dr. Andi",
                "dr. Budi",
                "dr. Sinta",
            ],
        )

        self.dokter.grid(row=9, column=1, padx=25, pady=8)

        # ======================================================
        # BUTTON
        # ======================================================

        Button(
            form,
            text="Simpan Data",
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
            text="👤",
            bg=WHITE,
            font=("Segoe UI Emoji", 70),
        ).pack(pady=(25, 10))

        Label(
            right,
            text="Data Pasien",
            bg=WHITE,
            fg=PRIMARY,
            font=("Segoe UI", 16, "bold"),
        ).pack()

        Label(
            right,
            text="Lengkapi identitas pasien\nsebelum dilakukan pemeriksaan.",
            bg=WHITE,
            fg=TEXT_SECONDARY,
            justify="center",
            font=("Segoe UI", 10),
        ).pack(pady=10)

        Label(
            right,
            text="✔ Data Lengkap\n✔ Mudah Digunakan\n✔ Proses Cepat",
            bg=WHITE,
            fg=SUCCESS,
            justify="left",
            font=("Segoe UI", 11),
        ).pack(pady=20)

    # =====================================================
    # SIMPAN DATA PASIEN
    # =====================================================

    def simpan(self):

        nama = self.nama.get().strip()
        nik = self.nik.get().strip()
        umur = self.umur.get().strip()
        jk = self.jk.get().strip()
        alamat = self.alamat.get("1.0", END).strip()
        nohp = self.nohp.get().strip()
        poli = self.poli.get().strip()
        dokter = self.dokter.get().strip()

        if (
            nama == ""
            or nik == ""
            or umur == ""
            or jk == ""
            or alamat == ""
            or nohp == ""
            or poli == ""
            or dokter == ""
        ):
            messagebox.showwarning("Peringatan", "Semua data pasien harus diisi!")
            return

        try:

            self.db.execute(
                """
                INSERT INTO pasien
                (
                    nama,
                    nik,
                    umur,
                    jk,
                    alamat,
                    nohp,
                    poli,
                    dokter
                )
                VALUES
                (?,?,?,?,?,?,?,?)
                """,
                (
                    nama,
                    nik,
                    umur,
                    jk,
                    alamat,
                    nohp,
                    poli,
                    dokter,
                ),
            )

            messagebox.showinfo("Berhasil", "Data pasien berhasil disimpan.")

            self.reset_form()

            # =====================================================
            # NANTI BISA DIBUKA JIKA MAU LANGSUNG KE SURVEI
            # =====================================================

            # self.master.clear_frame()
            # from survei_frame import SurveiFrame
            # SurveiFrame(self.master)

        except Exception as e:

            messagebox.showerror("Error", str(e))

    # =====================================================
    # RESET FORM
    # =====================================================

    def reset_form(self):

        self.nama.delete(0, END)

        self.nik.delete(0, END)

        self.umur.delete(0, END)

        self.jk.set("")

        self.alamat.delete("1.0", END)

        self.nohp.delete(0, END)

        self.poli.set("")

        self.dokter.set("")

    # =====================================================
    # KEMBALI
    # =====================================================

    def kembali(self):

        self.master.clear_frame()

        from dashboard_frame import DashboardFrame

        DashboardFrame(self.master)
