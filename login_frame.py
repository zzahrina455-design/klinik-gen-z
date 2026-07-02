import json
import os
from tkinter import *
from tkinter import messagebox

from database import Database
from style import *


class LoginFrame(Frame):

    def __init__(self, master):
        super().__init__(master, bg=BACKGROUND)
        self.pack(fill="both", expand=True)

        self.db = Database()

        # =========================
        # LEFT PANEL
        # =========================

        left = Frame(
            self,
            bg=PRIMARY_DARK,
            width=350
        )

        left.pack(side=LEFT, fill=Y)
        left.pack_propagate(False)

        Label(
            left,
            text="🩺",
            font=("Segoe UI Emoji", 60),
            bg=PRIMARY_DARK,
            fg="white"
        ).pack(pady=(50, 10))

        Label(
            left,
            text="KLINIK GEN-Z",
            font=("Segoe UI", 22, "bold"),
            bg=PRIMARY_DARK,
            fg="white"
        ).pack()

        Label(
            left,
            text="Sistem Manajemen\nData Pasien",
            font=("Segoe UI", 12),
            justify="center",
            bg=PRIMARY_DARK,
            fg="white"
        ).pack(pady=20)

        Label(
            left,
            text="Cepat • Aman • Modern",
            font=("Segoe UI", 10),
            bg=PRIMARY_DARK,
            fg="#BBDEFB"
        ).pack()

        # =========================
        # RIGHT PANEL
        # =========================

        right = Frame(
            self,
            bg=BACKGROUND
        )

        right.pack(side=RIGHT, fill=BOTH, expand=True)

        card = Frame(
            right,
            bg="white",
            bd=1,
            relief="solid"
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=420,
            height=420
        )

        Label(
            card,
            text="LOGIN",
            font=("Segoe UI", 22, "bold"),
            bg="white",
            fg=PRIMARY_DARK
        ).pack(pady=(30, 25))

        # =========================
        # Username
        # =========================

        Label(
            card,
            text="Username",
            font=("Segoe UI", 10, "bold"),
            bg="white",
            anchor="w"
        ).pack(fill="x", padx=40)

        self.username = Entry(
            card,
            font=("Segoe UI", 11),
            relief="solid",
            bd=1
        )

        self.username.pack(
            padx=40,
            fill="x",
            ipady=8,
            pady=(5, 20)
        )

        # =========================
        # Password
        # =========================

        Label(
            card,
            text="Password",
            font=("Segoe UI", 10, "bold"),
            bg="white",
            anchor="w"
        ).pack(fill="x", padx=40)

        # Frame agar Entry dan tombol mata sejajar
        password_frame = Frame(card, bg="white")
        password_frame.pack(
            padx=40,
            fill="x",
            pady=(5, 25)
        )

        self.password = Entry(
            password_frame,
            show="*",
            font=("Segoe UI", 11),
            relief="solid",
            bd=1
        )

        self.password.pack(
            side=LEFT,
            fill="x",
            expand=True,
            ipady=8
        )

        # Status password
        self.show_password = False

        # Tombol Toggle Mata
        self.toggle_btn = Button(
            password_frame,
            text="👁",
            font=("Segoe UI Emoji", 11),
            bg="white",
            bd=0,
            cursor="hand2",
            activebackground="white",
            command=self.toggle_password
        )

        self.toggle_btn.pack(side=RIGHT, padx=(8, 0))

        # =========================
        # Login Button
        # =========================

        Button(
            card,
            text="LOGIN",
            bg=PRIMARY,
            fg="white",
            activebackground=PRIMARY_DARK,
            activeforeground="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.login
        ).pack(
            padx=40,
            fill="x",
            ipady=8
        )

        Label(
            card,
            text="",
            bg="white"
        ).pack(pady=5)

        Button(
            card,
            text="Belum punya akun? Register",
            font=("Segoe UI", 10),
            fg=PRIMARY,
            bg="white",
            bd=0,
            cursor="hand2",
            activebackground="white",
            activeforeground=PRIMARY_DARK,
            command=self.master.show_register
        ).pack()

    # =========================
    # Toggle Password
    # =========================

    def toggle_password(self):

        if self.show_password:
            self.password.config(show="*")
            self.toggle_btn.config(text="👁")
            self.show_password = False
        else:
            self.password.config(show="")
            self.toggle_btn.config(text="🙈")
            self.show_password = True

    # =========================
    # Login
    # =========================

    def login(self):

        username = self.username.get()
        password = self.password.get()

        if username == "" or password == "":
            messagebox.showwarning(
                "Peringatan",
                "Username dan Password harus diisi!"
            )
            return

        filename = "users.json"

        if not os.path.exists(filename):
            messagebox.showerror(
                "Error",
                "Belum ada akun."
            )
            return

        with open(filename, "r") as f:
            users = json.load(f)

        for user in users:

            if user["username"] == username and user["password"] == password:

                messagebox.showinfo(
                    "Berhasil",
                    "Login berhasil."
                )

                self.master.clear_frame()

                from dashboard_frame import DashboardFrame
                DashboardFrame(self.master)

                return

        messagebox.showerror(
            "Gagal",
            "Username atau Password salah!"
        )