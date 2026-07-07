import tkinter as tk
from tkinter import messagebox
from models import UserModel


class RegisterFrame(tk.Frame):

    def __init__(self, master):
        # Menggunakan warna background utama yang sama dengan login
        super().__init__(master, bg="#B8D3FC")
        self.pack(fill=tk.BOTH, expand=True)

        self.user_model = UserModel()

        # Konfigurasi grid utama agar SAMA PERSIS dengan login
        self.grid_columnconfigure(0, weight=1)  # Sisi Kiri (Logo & Judul)
        self.grid_columnconfigure(1, weight=1)  # Sisi Kanan (Form Card)
        self.grid_rowconfigure(0, weight=1)

        # ==========================================
        # SISI KIRI: LOGO & JUDUL KLINIK (Sama dengan Login)
        # ==========================================
        left_container = tk.Frame(self, bg="#B8D3FC")
        left_container.grid(row=0, column=0, sticky="nsew", padx=50)
        left_container.grid_rowconfigure((0, 1, 2, 3), weight=1)
        left_container.grid_columnconfigure(0, weight=1)

        # Logo Besar
        logo_label = tk.Label(
            left_container,
            text="✚",
            font=("Arial", 64, "bold"),
            fg="#1A5CFF",
            bg="#B8D3FC",
        )
        logo_label.grid(row=1, column=0, sticky="s", pady=10)

        # Judul Utama
        title_label = tk.Label(
            left_container,
            text="KLINIK GEN-Z",
            font=("Arial", 28, "bold"),
            fg="#0F172A",
            bg="#B8D3FC",
        )
        title_label.grid(row=2, column=0, sticky="n")

        # Subtitle
        subtitle_label = tk.Label(
            left_container,
            text="Sistem Manajemen\nData Pasien",
            font=("Arial", 14),
            fg="#64748B",
            bg="#B8D3FC",
            justify="center",
        )
        subtitle_label.grid(row=2, column=0, sticky="n", pady=60)

        # ==========================================
        # SISI KANAN: CARD CONTAINER (FORM REGISTER)
        # ==========================================
        card_form = tk.Frame(self, bg="#F9F9F9", padx=40, pady=30, width=420)
        card_form.grid(row=0, column=1, padx=20, pady=120, sticky="nsew")
        card_form.grid_propagate(False)

        # Header di dalam Card
        register_title = tk.Label(
            card_form,
            text="Register",
            font=("Arial", 22, "bold"),
            fg="#0F172A",
            bg="#F9F9F9",
        )
        register_title.pack(pady=(10, 5))

        register_subtitle = tk.Label(
            card_form,
            text="Buat akun baru",
            font=("Arial", 10),
            fg="#000000",
            bg="#F9F9F9",
        )
        register_subtitle.pack(pady=(0, 20))

        # ---- Input Nama Lengkap ----
        nama_frame = tk.Frame(
            card_form, bg="#F9F9F9",
            highlightbackground="#000000",
            highlightthickness=1
        )
        nama_frame.pack(fill=tk.X, pady=6, ipady=4)

        self.nama = tk.Entry(
            nama_frame,
            font=("Arial", 11),
            bg="#F9F9F9",
            bd=0,
            fg="#0F172A",
            insertbackground="#0F172A",
        )
        self.nama.pack(fill=tk.X, padx=10, pady=5)
        self.set_placeholder(self.nama, "Nama Lengkap")

        # ---- Input Username ----
        username_frame = tk.Frame(
            card_form, bg="#F9F9F9",
            highlightbackground="#000000",
            highlightthickness=1
        )
        username_frame.pack(fill=tk.X, pady=6, ipady=4)

        self.username = tk.Entry(
            username_frame,
            font=("Arial", 11),
            bg="#F9F9F9",
            bd=0,
            fg="#0F172A",
            insertbackground="#0F172A",
        )
        self.username.pack(fill=tk.X, padx=10, pady=5)
        self.set_placeholder(self.username, "Username")

        # ---- Input Password ----
        password_frame = tk.Frame(
            card_form, bg="#F9F9F9",
            highlightbackground="#000000",
            highlightthickness=1
        )
        password_frame.pack(fill=tk.X, pady=6, ipady=4)

        self.password = tk.Entry(
            password_frame,
            font=("Arial", 11),
            bg="#F9F9F9",
            bd=0,
            fg="#0F172A",
            insertbackground="#0F172A",
        )
        self.password.pack(fill=tk.X, padx=10, pady=5)
        self.set_placeholder(self.password, "Password", is_password=True)

        # ---- Tombol Register ----
        register_btn = tk.Button(
            card_form,
            text="Register",
            font=("Arial", 11, "bold"),
            bg="#1A5CFF",
            fg="#FFFFFF",
            activebackground="#0046E5",
            activeforeground="#FFFFFF",
            bd=0,
            cursor="hand2",
            command=self.register,
        )
        register_btn.pack(fill=tk.X, pady=(20, 15), ipady=6)

        # ---- Navigasi Kembali ke Login ----
        login_container = tk.Frame(card_form, bg="#FFFFFF")
        login_container.pack(pady=5)

        has_account_label = tk.Label(
            login_container,
            text="Sudah punya akun? ",
            font=("Arial", 10),
            fg="#64748B",
            bg="#F9F9F9",
        )
        has_account_label.pack(side=tk.LEFT)

        login_link = tk.Label(
            login_container,
            text="Login",
            font=("Arial", 10, "bold"),
            fg="#1A5CFF",
            bg="#F9F9F9",
            cursor="hand2",
        )
        login_link.pack(side=tk.LEFT)
        login_link.bind("<Button-1>", lambda e: master.show_login())

    # ==========================================
    # LOGIC & PLACEHOLDER HELPER
    # ==========================================
    def set_placeholder(self, entry, text, is_password=False):
        entry.insert(0, text)
        entry.config(fg="#525252")

        def on_focus_in(event):
            if entry.get() == text:
                entry.delete(0, tk.END)
                entry.config(fg="#0F172A")
                if is_password:
                    entry.config(show="*")

        def on_focus_out(event):
            if not entry.get():
                entry.insert(0, text)
                entry.config(fg="#000000")
                if is_password:
                    entry.config(show="")

        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)

    def register(self):
        nama = self.nama.get().strip()
        username = self.username.get().strip()
        password = self.password.get().strip()

        # Validasi input
        if (
            nama == "Nama Lengkap"
            or username == "Username"
            or password == "Password"
            or not nama
            or not username
            or not password
        ):
            messagebox.showwarning(
                "Peringatan",
                "Semua data harus diisi!"
            )
            return

        # Simpan data ke database
        sukses = self.user_model.register(
            nama,
            username,
            password,
            "pasien"
        )

        if sukses:
            messagebox.showinfo(
                "Berhasil",
                "Registrasi berhasil."
            )
            self.master.show_login()
        else:
            messagebox.showerror("Error", "Username sudah digunakan!")
