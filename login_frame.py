import tkinter as tk
from tkinter import messagebox
from models import UserModel


class LoginFrame(tk.Frame):

    def __init__(self, master):
        super().__init__(master, bg="#B8D3FC")
        self.pack(fill=tk.BOTH, expand=True)

        self.user_model = UserModel()

        # Konfigurasi grid utama agar seimbang kiri dan kanan
        self.grid_columnconfigure(0, weight=1)  # Sisi Kiri (Logo & Judul)
        self.grid_columnconfigure(1, weight=1)  # Sisi Kanan (Form Card)
        self.grid_rowconfigure(0, weight=1)

        # ==========================================
        # SISI KIRI: LOGO & JUDUL KLINIK
        # ==========================================
        left_container = tk.Frame(self, bg="#B8D3FC")
        left_container.grid(row=0, column=0, sticky="nsew", padx=50)
        left_container.grid_rowconfigure((0, 1, 2, 3), weight=1)
        left_container.grid_columnconfigure(0, weight=1)

        # Placeholder Simbol Plus/Logo Besar
        # Catatan: Jika ada gambar asli, gunakan tk.PhotoImage
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
        # SISI KANAN: CARD CONTAINER (FORM LOGIN)
        # ==========================================
        # Frame putih sebagai wadah form (Card background)
        card_form = tk.Frame(self, bg="#F9F9F9", padx=40, pady=40)
        card_form.grid(row=0, column=1, padx=60, pady=110, sticky="nsew")
        card_form.grid_columnconfigure(0, weight=1)

        # Header di dalam Card
        login_title = tk.Label(
            card_form,
            text="Login",
            font=("Arial", 22, "bold"),
            fg="#0F172A",
            bg="#F9F9F9",
        )
        login_title.pack(pady=(10, 5))

        login_subtitle = tk.Label(
            card_form,
            text="Silakan masuk ke akun Anda",
            font=("Arial", 10),
            fg="#000000",
            bg="#F9F9F9",
        )
        login_subtitle.pack(pady=(0, 25))

        # ---- Input Username ----
        # Frame pembungkus entry agar bisa diberi border/padding custom
        username_frame = tk.Frame(
            card_form, bg="#F8FAFC",
            highlightbackground="#000000",
            highlightthickness=1
        )
        username_frame.pack(fill=tk.X, pady=5, ipady=5)

        # Icon/Label teks mini di dalam Entry (atau pakai placeholder)
        self.username = tk.Entry(
            username_frame,
            font=("Arial", 11),
            bg="#F8FAFC",
            bd=0,
            fg="#0F172A",
            insertbackground="#0F172A",
        )
        self.username.pack(fill=tk.X, padx=8, pady=5)
        self.set_placeholder(self.username, "Username")

        # ---- Input Password ----
        password_frame = tk.Frame(
            card_form, bg="#F8FAFC",
            highlightbackground="#E2E8F0",
            highlightthickness=1
        )
        password_frame.pack(fill=tk.X, pady=5, ipady=5)

        self.password = tk.Entry(
            password_frame,
            font=("Arial", 11),
            bg="#F8FAFC",
            bd=0,
            fg="#0F172A",
            insertbackground="#0F172A",
        )
        self.password.pack(fill=tk.X, padx=8, pady=5)
        self.set_placeholder(self.password, "Password", is_password=True)

        # ---- Tombol Login ----
        login_btn = tk.Button(
            card_form,
            text="Login",
            font=("Arial", 11, "bold"),
            bg="#1A5CFF",  # Biru menyesuaikan mockup
            fg="#FFFFFF",
            activebackground="#0046E5",
            activeforeground="#FFFFFF",
            bd=0,
            cursor="hand2",
            command=self.login,
        )
        login_btn.pack(fill=tk.X, pady=(15, 15), ipady=6)

        # ---- Navigasi Register (Teks Bawah) ----
        register_container = tk.Frame(card_form, bg="#FFFFFF")
        register_container.pack(pady=10)

        no_account_label = tk.Label(
            register_container,
            text="Belum punya akun? ",
            font=("Arial", 10),
            fg="#64748B",
            bg="#F9F9F9",
        )
        no_account_label.pack(side=tk.LEFT)

        register_link = tk.Label(
            register_container,
            text="Register",
            font=("Arial", 10, "bold"),
            fg="#1A5CFF",
            bg="#FFFFFF",
            cursor="hand2",
        )
        register_link.pack(side=tk.LEFT)
        register_link.bind("<Button-1>", lambda e: master.show_register())

    # ==========================================
    # LOGIC & PLACEHOLDER HELPER
    # ==========================================
    def set_placeholder(self, entry, text, is_password=False):
        """Fungsi pembantu untuk membuat efek placeholder tulisan samar"""
        entry.insert(0, text)
        entry.config(fg="#94A3B8")

        def on_focus_in(event):
            if entry.get() == text:
                entry.delete(0, tk.END)
                entry.config(fg="#0F172A")
                if is_password:
                    entry.config(show="*")

        def on_focus_out(event):
            if not entry.get():
                entry.insert(0, text)
                entry.config(fg="#94A3B8")
                if is_password:
                    entry.config(show="")

        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)

    def login(self):
        username = self.username.get().strip()
        password = self.password.get()

        if (
            username == "Username"
            or password == "Password"
            or not username
            or not password
        ):
            messagebox.showwarning(
                "Peringatan", "Username dan Password harus diisi!"
                )
            return

        user = self.user_model.login(username, password)

        if user is None:
            messagebox.showerror("Error", "Username atau Password salah!")
            return

        role = user[4]
        if role == "admin":
            self.master.show_admin(user)
        elif role == "dokter":
            self.master.show_dokter(user)
        else:
            self.master.show_pasien(user)
