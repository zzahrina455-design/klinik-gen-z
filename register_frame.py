import json
import os
from tkinter import *
from tkinter import messagebox

from database import Database
from style import *


class RegisterFrame(Frame):

    def __init__(self, master):
        super().__init__(master, bg=BACKGROUND)
        self.pack(fill="both", expand=True)

        # ========= LEFT ==========
        left = Frame(self, bg=PRIMARY_DARK, width=350)
        left.pack(side=LEFT, fill=Y)
        left.pack_propagate(False)

        Label(
            left, text="🩺", font=("Segoe UI Emoji", 60), bg=PRIMARY_DARK, fg="white"
        ).pack(pady=(90, 10))

        Label(
            left,
            text="KLINIK GEN-Z",
            font=("Segoe UI", 22, "bold"),
            bg=PRIMARY_DARK,
            fg="white",
        ).pack()

        Label(
            left,
            text="Daftarkan akun\nuntuk mulai menggunakan\nSistem Klinik",
            justify="center",
            font=("Segoe UI", 11),
            bg=PRIMARY_DARK,
            fg="white",
        ).pack(pady=20)

        # ========= RIGHT =========

        right = Frame(self, bg=BACKGROUND)
        right.pack(side=RIGHT, fill=BOTH, expand=True)

        card = Frame(right, bg="white", bd=1, relief="solid")
        card.place(relx=0.5, rely=0.5, anchor="center", width=420, height=450)

        Label(
            card,
            text="REGISTER",
            font=("Segoe UI", 22, "bold"),
            bg="white",
            fg=PRIMARY_DARK,
        ).pack(pady=25)

        # ==========================
        # Username
        # ==========================

        Label(
            card, text="Username", bg="white", font=("Segoe UI", 10, "bold"), anchor="w"
        ).pack(fill="x", padx=40)

        self.username = Entry(card, font=("Segoe UI", 11))

        self.username.pack(fill="x", padx=40, ipady=8, pady=(5, 20))

        # ==========================
        # Password
        # ==========================

        Label(
            card, text="Password", bg="white", font=("Segoe UI", 10, "bold"), anchor="w"
        ).pack(fill="x", padx=40)

        password_frame = Frame(card, bg="white")
        password_frame.pack(fill="x", padx=40, pady=(5, 25))

        self.password = Entry(password_frame, show="*", font=("Segoe UI", 11))

        self.password.pack(side=LEFT, fill="x", expand=True, ipady=8)

        # Status password
        self.show_password = False

        # Tombol mata
        self.toggle_btn = Button(
            password_frame,
            text="👁",
            font=("Segoe UI Emoji", 11),
            bg="white",
            bd=0,
            cursor="hand2",
            activebackground="white",
            command=self.toggle_password,
        )

        self.toggle_btn.pack(side=RIGHT, padx=(8, 0))

        # ==========================
        # Button Register
        # ==========================

        Button(
            card,
            text="DAFTAR",
            bg=PRIMARY,
            fg="white",
            relief="flat",
            cursor="hand2",
            font=("Segoe UI", 11, "bold"),
            command=self.register,
        ).pack(fill="x", padx=40, ipady=8)

        Button(
            card,
            text="Sudah punya akun? Login",
            bg="white",
            fg=PRIMARY,
            relief="flat",
            cursor="hand2",
            font=("Segoe UI", 10),
            command=self.master.show_login,
        ).pack(pady=15)

    # ==========================
    # Toggle Password
    # ==========================

    def toggle_password(self):

        if self.show_password:
            self.password.config(show="*")
            self.toggle_btn.config(text="👁")
            self.show_password = False
        else:
            self.password.config(show="")
            self.toggle_btn.config(text="🙈")
            self.show_password = True

    # ==========================
    # Register
    # ==========================

    def register(self):

        username = self.username.get().strip()
        password = self.password.get().strip()

        if not username or not password:
            messagebox.showwarning("Peringatan", "Semua data harus diisi!")
            return

        filename = "users.json"

        # Jika file belum ada, buat file kosong
        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as file:
                json.dump([], file)

        # Membaca data user
        try:
            with open(filename, "r", encoding="utf-8") as file:
                users = json.load(file)
        except json.JSONDecodeError:
            users = []

        # Cek username sudah ada atau belum
        for user in users:
            if user.get("username") == username:
                messagebox.showerror("Gagal", "Username sudah digunakan!")
                return

        # Tambahkan user baru
        users.append({"username": username, "password": password})

        # Simpan kembali ke file JSON
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(users, file, indent=4, ensure_ascii=False)

        messagebox.showinfo("Berhasil", "Registrasi berhasil.")

        self.master.show_login()
