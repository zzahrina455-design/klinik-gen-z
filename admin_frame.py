import tkinter as tk
from tkinter import ttk, messagebox
from models import AntrianModel, SurveyModel


class AdminFrame(tk.Frame):

    def __init__(self, master, user):
        # Menginisialisasi induk frame utama
        super().__init__(master, bg="#F8FAFC")

        self.master = master
        self.user = user

        self.antrian_model = AntrianModel()
        self.survey_model = SurveyModel()

        self.selected_id = None

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(
            1, weight=1
        )  # Konten Utama melebar menghabiskan sisa layar
        self.grid_rowconfigure(0, weight=1)  # Mengisi penuh secara vertikal

        # Panggil fungsi perakitan komponen GUI
        self.buat_sidebar()
        self.buat_konten_admin()

        # Load data awal
        self.load_antrian()
        self.load_survey()

    # ======================================================
    # SIDEBAR NAVIGASI (Sisi Kiri)
    # ======================================================
    def buat_sidebar(self):
        # Frame Sidebar diletakkan di Kolom 0
        sidebar = tk.Frame(
            self, bg="#FFFFFF",
            highlightbackground="#E2E8F0",
            highlightthickness=1
        )
        sidebar.grid(row=0, column=0, sticky="nsew")

        # Nama Aplikasi di Atas Sidebar
        app_title = tk.Label(
            sidebar,
            text="Klinik Gen-Z",
            font=("Arial", 14, "bold"),
            fg="#0F172A",
            bg="#FFFFFF",
            anchor="w",
        )
        app_title.pack(fill=tk.X, padx=25, pady=25)

        # Daftar Menu Admin
        menus = [
            ("⚙️  Riwayat Pengguna", "active"),  # Status menu aktif
            ("🚪  Keluar", self.master.show_login),
        ]

        for text, command in menus:
            if command == "active":
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
                    padx=20,
                    cursor="hand2",
                )
            else:
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
                    padx=20,
                    cursor="hand2",
                    command=command if command else lambda: None,
                )
            btn.pack(fill=tk.X, padx=15, pady=4, ipady=10)

    # ======================================================
    # KONTEN UTAMA ADMIN (Sisi Kanan)
    # ======================================================
    def buat_konten_admin(self):
        # Frame Konten Utama diletakkan di Kolom 1
        main_content = tk.Frame(self, bg="#F8FAFC", padx=35, pady=25)
        main_content.grid(row=0, column=1, sticky="nsew")

        main_content.grid_columnconfigure(0, weight=1)
        main_content.grid_rowconfigure(
            1, weight=1
        )  # Panel Antrian dapat jatah membesar
        main_content.grid_rowconfigure(2, weight=1)

        # 1. Header Welcome Admin
        header_frame = tk.Frame(main_content, bg="#F8FAFC")
        header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 15))

        tk.Label(
            header_frame,
            text=f"Panel Kontrol Admin — {self.user[1]}",
            font=("Arial", 16, "bold"),
            fg="#0F172A",
            bg="#F8FAFC",
        ).pack(side=tk.LEFT)

        # Styling Global Treeview Table (Modern Theme)
        style_tree = ttk.Style()
        style_tree.theme_use("clam")
        style_tree.configure(
            "Treeview",
            background="#FFFFFF",
            foreground="#334155",
            rowheight=28,
            fieldbackground="#FFFFFF",
            font=("Arial", 9),
        )
        style_tree.configure(
            "Treeview.Heading",
            background="#F1F5F9",
            foreground="#0F172A",
            font=("Arial", 9, "bold"),
            borderwidth=0,
        )
        style_tree.map(
            "Treeview",
            background=[("selected", "#EBF1FA")],
            foreground=[("selected", "#1A5CFF")],
        )

        # ==================================================
        # 2. PANEL DATA ANTRIAN (Atas)
        # ==================================================
        antrian_panel = tk.Frame(
            main_content,
            bg="#FFFFFF",
            highlightbackground="#E2E8F0",
            highlightthickness=1,
            padx=20,
            pady=15,
        )
        antrian_panel.grid(row=1, column=0, sticky="nsew", pady=(0, 20))

        # Sub-Header Panel Antrian
        antrian_header = tk.Frame(antrian_panel, bg="#FFFFFF")
        antrian_header.pack(fill=tk.X, pady=(0, 10))

        tk.Label(
            antrian_header,
            text="Manajemen Antrian Pasien",
            font=("Arial", 11, "bold"),
            fg="#0F172A",
            bg="#FFFFFF",
        ).pack(side=tk.LEFT)

        # Kelompok Tombol Aksi Kontrol (Kanan Atas Tabel)
        btn_action_frame = tk.Frame(antrian_header, bg="#FFFFFF")
        btn_action_frame.pack(side=tk.RIGHT)

        tk.Button(
            btn_action_frame,
            text="🔔 Panggil",
            font=("Arial", 9, "bold"),
            bg="#F59E0B",
            fg="#FFFFFF",
            bd=0,
            padx=12,
            pady=5,
            cursor="hand2",
            command=self.panggil,
        ).pack(side=tk.LEFT, padx=3)
        tk.Button(
            btn_action_frame,
            text="✅ Selesai",
            font=("Arial", 9, "bold"),
            bg="#10B981",
            fg="#FFFFFF",
            bd=0,
            padx=12,
            pady=5,
            cursor="hand2",
            command=self.selesai,
        ).pack(side=tk.LEFT, padx=3)
        tk.Button(
            btn_action_frame,
            text="🗑️ Hapus",
            font=("Arial", 9, "bold"),
            bg="#EF4444",
            fg="#FFFFFF",
            bd=0,
            padx=12,
            pady=5,
            cursor="hand2",
            command=self.hapus,
        ).pack(side=tk.LEFT, padx=3)
        tk.Button(
            btn_action_frame,
            text="🔄 Refresh",
            font=("Arial", 9, "bold"),
            bg="#64748B",
            fg="#FFFFFF",
            bd=0,
            padx=12,
            pady=5,
            cursor="hand2",
            command=self.load_antrian,
        ).pack(side=tk.LEFT, padx=3)

        # Tabel Antrian
        kolom = ("ID", "Pasien", "Poli", "Nomor", "Status", "Tanggal")
        self.tree = ttk.Treeview(
            antrian_panel, columns=kolom, show="headings", height=5
        )

        lebar_kolom = {
            "ID": 50,
            "Pasien": 160,
            "Poli": 120,
            "Nomor": 70,
            "Status": 95,
            "Tanggal": 120,
        }
        for k in kolom:
            self.tree.heading(k, text=k, anchor="w")
            self.tree.column(
                k, width=lebar_kolom[k],
                anchor="w" if k != "Nomor" else "center"
            )

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.pilih_data)

        # ==================================================
        # 3. PANEL HASIL SURVEY (Bawah)
        # ==================================================
        survey_panel = tk.Frame(
            main_content,
            bg="#FFFFFF",
            highlightbackground="#E2E8F0",
            highlightthickness=1,
            padx=20,
            pady=15,
        )
        survey_panel.grid(row=2, column=0, sticky="nsew")

        tk.Label(
            survey_panel,
            text="Hasil Survey Kepuasan",
            font=("Arial", 11, "bold"),
            fg="#0F172A",
            bg="#FFFFFF",
        ).pack(anchor="w", pady=(0, 10))

        # Tabel Survey
        kolom2 = ("ID", "Pasien", "Pelayanan",
                  "Kebersihan", "Keramahan", "Saran")
        self.tree2 = ttk.Treeview(
            survey_panel, columns=kolom2, show="headings", height=4
        )

        lebar_kolom2 = {
            "ID": 50,
            "Pasien": 160,
            "Pelayanan": 95,
            "Kebersihan": 95,
            "Keramahan": 95,
            "Saran": 250,
        }
        for k in kolom2:
            self.tree2.heading(k, text=k, anchor="w")
            self.tree2.column(
                k,
                width=lebar_kolom2[k],
                anchor="w" if k == "Pasien" or k == "Saran" else "center",
            )

        self.tree2.pack(fill=tk.BOTH, expand=True)

    # ======================================================
    # DATA LOGIC & METHODS
    # ======================================================
    def load_antrian(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        data = self.antrian_model.semua_antrian()
        for row in data:
            self.tree.insert("", tk.END, values=row)
        self.selected_id = None

    def load_survey(self):
        for item in self.tree2.get_children():
            self.tree2.delete(item)

        data = self.survey_model.semua()
        for row in data:
            self.tree2.insert("", tk.END, values=row)

    def pilih_data(self, event):
        pilih = self.tree.selection()
        if not pilih:
            return

        data = self.tree.item(pilih[0])["values"]
        self.selected_id = data[0]

    def panggil(self):
        if self.selected_id is None:
            messagebox.showwarning(
                "Peringatan", "Pilih data antrian terlebih dahulu dari tabel."
            )
            return

        self.antrian_model.update_status_dan_notifikasi(
            self.selected_id, "Dipanggil")
        self.load_antrian()

    def selesai(self):
        if self.selected_id is None:
            messagebox.showwarning(
                "Peringatan", "Pilih data antrian terlebih dahulu dari tabel."
            )
            return

        self.antrian_model.update_status_dan_notifikasi(
            self.selected_id, "Selesai")
        self.load_antrian()

    def hapus(self):
        if self.selected_id is None:
            messagebox.showwarning(
                "Peringatan", "Pilih data antrian terlebih dahulu dari tabel."
            )
            return

        jawab = messagebox.askyesno(
            "Konfirmasi", "Hapus data antrian ini secara permanen?"
        )
        if jawab:
            self.antrian_model.hapus(self.selected_id)
            self.selected_id = None
            self.load_antrian()
