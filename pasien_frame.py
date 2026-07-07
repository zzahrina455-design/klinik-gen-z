import tkinter as tk
from tkinter import ttk, messagebox
from models import AntrianModel, NotifikasiModel
from survey_frame import SurveyFrame


class PasienFrame(tk.Frame):

    def __init__(self, master, user):
        super().__init__(master, bg="#F8FAFC")
        self.pack(fill=tk.BOTH, expand=True)

        self.master = master
        self.user = user
        self.nama_pasien = user[1]

        self.antrian_model = AntrianModel()
        self.notifikasi_model = NotifikasiModel()
        self.nomor_antrian = "-"

        # Struktur Grid Utama: Kolom 0 (Sidebar), Kolom 1 (Konten Utama)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.buat_sidebar()
        self.buat_konten_antrian()
        self.load_notifikasi()

    # ======================================================
    # SIDEBAR NAVIGASI (Sisi Kiri)
    # ======================================================
    def buat_sidebar(self):
        sidebar = tk.Frame(
            self,
            bg="#FFFFFF",
            width=220,
            highlightbackground="#E2E8F0",
            highlightthickness=1,
        )
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_propagate(False)  # Kunci lebar agar tidak menciut

        # Nama Aplikasi di Atas Sidebar
        app_title = tk.Label(
            sidebar,
            text="Klinik Gen-Z",
            font=("Arial", 14, "bold"),
            fg="#0F172A",
            bg="#FFFFFF",
            anchor="w",
        )
        app_title.pack(fill=tk.X, padx=20, pady=25)

        # Tombol-tombol Navigasi Menu
        menus = [
            ("🎟️  Antrian", "active"),
            ("📝  Survei", self.buka_survey),
            ("🚪  Keluar", self.master.show_login),
        ]

        for text, command in menus:
            if command == "active":
                # Tombol Aktif (Warna Biru Utama)
                btn = tk.Button(
                    sidebar,
                    text=text,
                    font=("Arial", 10, "bold"),
                    bg="#1A5CFF",
                    fg="#FFFFFF",
                    activebackground="#1A5CFF",
                    activeforeground="#FFFFFF",
                    bd=0,
                    anchor="w",
                    padx=15,
                    cursor="hand2",
                )
            else:
                # Tombol Biasa (Warna Abu/Transparan)
                btn = tk.Button(
                    sidebar,
                    text=text,
                    font=("Arial", 10),
                    bg="#FFFFFF",
                    fg="#64748B",
                    activebackground="#F1F5F9",
                    activeforeground="#0F172A",
                    bd=0,
                    anchor="w",
                    padx=15,
                    cursor="hand2",
                    command=command if command else lambda: None,
                )
            btn.pack(fill=tk.X, padx=15, pady=4, ipady=8)

    # ======================================================
    # KONTEN UTAMA: PENDAFTARAN ANTRIAN (Sisi Kanan)
    # ======================================================
    def buat_konten_antrian(self):
        # Container utama sisi kanan
        main_content = tk.Frame(self, bg="#F8FAFC", padx=35, pady=25)
        main_content.grid(row=0, column=1, sticky="nsew")
        main_content.grid_columnconfigure(0, weight=1)
        main_content.grid_columnconfigure(1, weight=1)
        main_content.grid_rowconfigure(1, weight=1)

        # 1. Header Halaman
        header_title = tk.Label(
            main_content,
            text="Pendaftaran Antrian",
            font=("Arial", 18, "bold"),
            fg="#0F172A",
            bg="#F8FAFC",
        )
        header_title.grid(row=0, column=0,
                          columnspan=2, sticky="w",
                          pady=(0, 20))

        # 2. Sisi Kiri Konten: Form Input Isian
        form_frame = tk.Frame(main_content, bg="#F8FAFC")
        form_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 25))

        # Field Nama Pasien (Membaca nama user otomatis)
        tk.Label(
            form_frame,
            text="Nama Pasien",
            font=("Arial", 10, "bold"),
            fg="#334155",
            bg="#F8FAFC",
        ).pack(anchor="w", pady=(5, 2))
        name_wrapper = tk.Frame(
            form_frame,
            bg="#FFFFFF",
            highlightbackground="#E2E8F0",
            highlightthickness=1,
        )
        name_wrapper.pack(fill=tk.X, pady=(0, 15), ipady=4)
        lbl_nama = tk.Label(
            name_wrapper,
            text=self.nama_pasien,
            font=("Arial", 11),
            fg="#0F172A",
            bg="#FFFFFF",
            anchor="w",
        )
        lbl_nama.pack(fill=tk.X, padx=10, pady=4)

        # Field Pilihan Poli / Layanan
        tk.Label(
            form_frame,
            text="Poli / Layanan",
            font=("Arial", 10, "bold"),
            fg="#334155",
            bg="#F8FAFC",
        ).pack(anchor="w", pady=(5, 2))

        # Styling Combobox Tkinter agar lebih minimalis
        self.combo_poli = ttk.Combobox(
            form_frame, font=("Arial", 11), state="readonly")
        self.combo_poli["values"] = (
            "Poli Umum",
            "Poli Gigi",
            "Poli Anak",
            "Poli Kandungan",
            "Poli Mata",
        )
        self.combo_poli.current(0)
        self.combo_poli.pack(fill=tk.X, pady=(0, 15))

        # Field Tanggal Kunjungan (Dummy default hari ini)
        tk.Label(
            form_frame,
            text="Tanggal",
            font=("Arial", 10, "bold"),
            fg="#334155",
            bg="#F8FAFC",
        ).pack(anchor="w", pady=(5, 2))
        date_wrapper = tk.Frame(
            form_frame,
            bg="#FFFFFF",
            highlightbackground="#E2E8F0",
            highlightthickness=1,
        )
        date_wrapper.pack(fill=tk.X, pady=(0, 15), ipady=4)
        lbl_date = tk.Label(
            date_wrapper,
            text="06/07/2026",
            font=("Arial", 11),
            fg="#0F172A",
            bg="#FFFFFF",
            anchor="w",
        )
        lbl_date.pack(fill=tk.X, padx=10, pady=4)

        # Field Keluhan (Menggunakan Text widget tipis menggantikan entry lama)
        tk.Label(
            form_frame,
            text="Keluhan",
            font=("Arial", 10, "bold"),
            fg="#334155",
            bg="#F8FAFC",
        ).pack(anchor="w", pady=(5, 2))
        self.txt_keluhan = tk.Text(
            form_frame,
            font=("Arial", 11),
            height=4,
            bg="#FFFFFF",
            highlightbackground="#E2E8F0",
            highlightthickness=1,
            bd=0,
        )
        self.txt_keluhan.pack(fill=tk.X, pady=(0, 20), padx=1)

        # Tombol Submit Antrian
        btn_submit = tk.Button(
            form_frame,
            text="👤 Daftar Antrian",
            font=("Arial", 11, "bold"),
            bg="#1A5CFF",
            fg="#FFFFFF",
            activebackground="#0046E5",
            activeforeground="#FFFFFF",
            bd=0,
            cursor="hand2",
            command=self.ambil_antrian,
        )
        btn_submit.pack(fill=tk.X, ipady=6)

        # 3. Sisi Kanan Konten: Panel Realtime Antrian Hari Ini
        queue_panel = tk.Frame(
            main_content,
            bg="#FFFFFF",
            highlightbackground="#E2E8F0",
            highlightthickness=1,
            padx=20,
            pady=20,
        )
        queue_panel.grid(row=1, column=1, sticky="nsew")

        panel_title = tk.Label(
            queue_panel,
            text="Antrian Hari Ini",
            font=("Arial", 12, "bold"),
            fg="#0F172A",
            bg="#FFFFFF",
        )
        panel_title.pack(anchor="w", pady=(0, 15))

        self.lbl_nomor = tk.Label(
            queue_panel,
            text="Antrian Anda: -",
            font=("Arial", 11, "bold"),
            fg="#1A5CFF",
            bg="#EBF1FA",
            pady=8,
        )
        self.lbl_nomor.pack(fill=tk.X, side=tk.BOTTOM, pady=(10, 0))

        # Container list notifikasi / antrian (Pengganti listbox kaku)
        self.queue_container = tk.Frame(queue_panel, bg="#FFFFFF")
        self.queue_container.pack(fill=tk.BOTH, expand=True)

    # ======================================================
    # LOGIC & COMPONENT UPDATE FUNCTION
    # ======================================================
    def buka_survey(self):
        SurveyFrame(self.master, self.nama_pasien)

    def ambil_antrian(self):
        aktif = self.antrian_model.antrian_aktif(self.nama_pasien)
        if aktif:
            messagebox.showwarning(
                "Peringatan", "Anda masih memiliki antrian aktif.")
            return

        poli = self.combo_poli.get()
        nomor = self.antrian_model.ambil_nomor(self.nama_pasien, poli)
        self.nomor_antrian = nomor

        formatted_antrian = f"A{nomor:03}"
        self.lbl_nomor.config(
            text=f"Antrian Anda: {formatted_antrian} ({poli})")

        pesan = (
            f"Nomor antrian Anda {formatted_antrian} "
            f"untuk {poli}. "
            "Silakan menunggu panggilan."
        )
        self.notifikasi_model.tambah(self.nama_pasien, pesan)

        messagebox.showinfo("Berhasil", pesan)
        self.load_notifikasi()

    def load_notifikasi(self):
        # Bersihkan container lama
        for widget in self.queue_container.winfo_children():
            widget.destroy()

        data = self.notifikasi_model.semua(self.nama_pasien)

        if len(data) == 0:
            lbl_empty = tk.Label(
                self.queue_container,
                text="Belum ada antrian terdaftar.",
                font=("Arial", 10),
                fg="#94A3B8",
                bg="#FFFFFF",
            )
            lbl_empty.pack(pady=20)
            return

        for item in data[:3]:
            # Membuat Box Card komponen melengkung tipis
            card = tk.Frame(self.queue_container,
                            bg="#F1F5F9",
                            padx=12,
                            pady=10)
            card.pack(fill=tk.X, pady=5)

            # Badge Angka Antrian (Sisi Kiri Card)
            badge_num = tk.Label(
                card,
                text=f"A00{item[0]}",
                font=("Arial", 11, "bold"),
                fg="#1A5CFF",
                bg="#EBF1FA",
                width=6,
                pady=3,
            )
            badge_num.pack(side=tk.LEFT, padx=(0, 10))

            # Info Detail Teks (Sisi Kanan Card)
            text_frame = tk.Frame(card, bg="#F1F5F9")
            text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            lbl_user = tk.Label(
                text_frame,
                text=self.nama_pasien,
                font=("Arial", 10, "bold"),
                fg="#0F172A",
                bg="#F1F5F9",
                anchor="w",
            )
            lbl_user.pack(fill=tk.X)

            # Mengambil nama poli dari string pesan notifikasi
            poli_name = self.combo_poli.get()
            lbl_poli = tk.Label(
                text_frame,
                text=poli_name,
                font=("Arial", 9),
                fg="#64748B",
                bg="#F1F5F9",
                anchor="w",
            )
            lbl_poli.pack(fill=tk.X)
