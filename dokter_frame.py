import tkinter as tk
from tkinter import ttk, messagebox
from models import AntrianModel, RekamMedisModel


class DokterFrame(tk.Frame):

    def __init__(self, master, user):
        # Menginisialisasi frame dengan warna latar belakang modern yang bersih
        super().__init__(master, bg="#F8FAFC")

        self.master = master
        self.user = user
        self.nama_dokter = user[1]

        self.antrian_model = AntrianModel()
        self.rekam_model = RekamMedisModel()

        self.selected_pasien = None

        # Grid Utama: Membagi layar Kiri (Sidebar) dan Kanan (Konten Utama)
        self.grid_columnconfigure(0, weight=0)  # Lebar tetap untuk sidebar
        self.grid_columnconfigure(1, weight=1)  # Area konten melebar dinamis
        self.grid_rowconfigure(0, weight=1)

        self.buat_sidebar()
        self.buat_konten_dokter()
        self.load_data()

    # ======================================================
    # SIDEBAR NAVIGASI (Sisi Kiri)
    # ======================================================
    def buat_sidebar(self):
        sidebar = tk.Frame(
            self,
            bg="#FFFFFF",
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

        # Daftar Menu Dokter
        menus = [
            ("👨‍⚕️  Antrian & Periksa", "active"),  # Menu aktif dokter
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
    # KONTEN UTAMA DOKTER (Sisi Kanan)
    # ======================================================
    def buat_konten_dokter(self):
        main_content = tk.Frame(self, bg="#F8FAFC", padx=35, pady=25)
        main_content.grid(row=0, column=1, sticky="nsew")

        main_content.grid_columnconfigure(
            0, weight=3
        )  # Proporsi area tabel (lebih lebar)
        main_content.grid_columnconfigure(1, weight=2)
        main_content.grid_rowconfigure(1, weight=1)

        # 1. Header Welcome Dokter
        header_frame = tk.Frame(main_content, bg="#F8FAFC")
        header_frame.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(0, 20))

        tk.Label(
            header_frame,
            text=f"Selamat Datang, dr. {self.nama_dokter}",
            font=("Arial", 16, "bold"),
            fg="#0F172A",
            bg="#F8FAFC",
        ).pack(side=tk.LEFT)

        # Tombol Refresh diletakkan di pojok kanan atas header
        tk.Button(
            header_frame,
            text="🔄 Refresh Data",
            font=("Arial", 9, "bold"),
            bg="#64748B",
            fg="#FFFFFF",
            bd=0,
            padx=12,
            pady=6,
            cursor="hand2",
            command=self.load_data,
        ).pack(side=tk.RIGHT)

        # Styling Global Treeview Table
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
        # 2. PANEL DATA ANTRIAN (Bagian Kiri Konten)
        # ==================================================
        antrian_panel = tk.Frame(
            main_content,
            bg="#FFFFFF",
            highlightbackground="#E2E8F0",
            highlightthickness=1,
            padx=20,
            pady=20,
        )
        antrian_panel.grid(row=1, column=0, sticky="nsew", padx=(0, 15))

        tk.Label(
            antrian_panel,
            text="Daftar Antrian Pasien Hari Ini",
            font=("Arial", 11, "bold"),
            fg="#0F172A",
            bg="#FFFFFF",
        ).pack(anchor="w", pady=(0, 12))

        kolom = ("ID", "Pasien", "Poli", "Nomor", "Status")
        self.tree = ttk.Treeview(antrian_panel, columns=kolom, show="headings")

        lebar_kolom = {"ID": 45,
                       "Pasien": 150,
                       "Poli": 110,
                       "Nomor": 65,
                       "Status": 90}
        for k in kolom:
            self.tree.heading(k, text=k, anchor="w")
            self.tree.column(
                k, width=lebar_kolom[k],
                anchor="w" if k != "Nomor" else "center"
            )

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.pilih_pasien)

        # ==================================================
        # 3. PANEL FORM REKAM MEDIS (Bagian Kanan Konten)
        # ==================================================
        form_panel = tk.Frame(
            main_content,
            bg="#FFFFFF",
            highlightbackground="#E2E8F0",
            highlightthickness=1,
            padx=20,
            pady=20,
        )
        form_panel.grid(row=1, column=1, sticky="nsew", padx=(15, 0))

        tk.Label(
            form_panel,
            text="Input Rekam Medis Pasien",
            font=("Arial", 11, "bold"),
            fg="#0F172A",
            bg="#FFFFFF",
        ).pack(anchor="w", pady=(0, 15))

        # Container ber-grid untuk isian form data agar lurus rapi
        fields_container = tk.Frame(form_panel, bg="#FFFFFF")
        fields_container.pack(fill=tk.X, expand=True)
        fields_container.grid_columnconfigure(1, weight=1)

        # --- Baris Pasien Terpilih ---
        tk.Label(
            fields_container,
            text="Nama Pasien",
            font=("Arial", 10),
            fg="#475569",
            bg="#FFFFFF",
        ).grid(row=0, column=0, sticky="w", pady=6)
        self.lbl_pasien = tk.Label(
            fields_container,
            text="Silakan pilih dari tabel",
            font=("Arial", 10, "bold"),
            fg="#1A5CFF",
            bg="#F1F5F9",
            anchor="w",
            padx=10,
            pady=4,
        )
        self.lbl_pasien.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=(15, 0),
            pady=6)

        # Helper untuk membuat Entry modern yang seragam
        def buat_field_entry(row_idx, label_text):
            tk.Label(
                fields_container,
                text=label_text,
                font=("Arial", 10),
                fg="#475569",
                bg="#FFFFFF",
            ).grid(row=row_idx, column=0, sticky="w", pady=8)
            entry = tk.Entry(
                fields_container,
                font=("Arial", 10),
                bg="#FFFFFF",
                fg="#0F172A",
                highlightbackground="#CBD5E1",
                highlightthickness=1,
                bd=0,
            )
            entry.grid(
                row=row_idx,
                column=1,
                sticky="ew",
                padx=(15, 0),
                pady=8,
                ipady=6
            )
            return entry

        # --- Baris Inputs ---
        self.keluhan = buat_field_entry(1, "Keluhan")
        self.diagnosa = buat_field_entry(2, "Diagnosa")
        self.obat = buat_field_entry(3, "Resep Obat")

        # Tombol Simpan Rekam Medis
        btn_simpan = tk.Button(
            form_panel,
            text="💾 Simpan Hasil Pemeriksaan",
            font=("Arial", 10, "bold"),
            bg="#10B981",
            fg="#FFFFFF",
            activebackground="#059669",
            activeforeground="#FFFFFF",
            bd=0,
            cursor="hand2",
            command=self.simpan,
        )
        btn_simpan.pack(fill=tk.X, pady=(20, 0), ipady=10)

    # ======================================================
    # DATA LOGIC & METHODS
    # ======================================================
    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        data = self.antrian_model.semua_antrian()
        for row in data:
            self.tree.insert("", tk.END, values=row[:5])

    def pilih_pasien(self, event):
        pilih = self.tree.selection()
        if not pilih:
            return

        data = self.tree.item(pilih[0])["values"]
        self.selected_pasien = data[1]
        self.lbl_pasien.config(text=self.selected_pasien, bg="#EBF1FA")

    def simpan(self):
        if self.selected_pasien is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih pasien terlebih dahulu dari tabel antrian."
            )
            return

        if not self.keluhan.get().strip() or not self.diagnosa.get().strip():
            messagebox.showwarning(
                "Peringatan", "Data keluhan dan diagnosa wajib diisi."
            )
            return

        self.rekam_model.simpan(
            self.selected_pasien,
            self.nama_dokter,
            self.keluhan.get(),
            self.diagnosa.get(),
            self.obat.get(),
        )

        messagebox.showinfo(
            "Berhasil",
            f"Rekam medis untuk {self.selected_pasien} berhasil disimpan."
        )

        # Reset Form
        self.keluhan.delete(0, tk.END)
        self.diagnosa.delete(0, tk.END)
        self.obat.delete(0, tk.END)
        self.selected_pasien = None
        self.lbl_pasien.config(text="Silakan pilih dari tabel", bg="#F1F5F9")
