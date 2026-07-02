from tkinter import *
from style import *

class Sidebar(Frame):
    def __init__(self, parent, master, active="dashboard"):
        super().__init__(
            parent,
            bg=PRIMARY_DARK,
            width=SIDEBAR_WIDTH
        )

        self.master_window = master
        self.pack_propagate(False)

        # =========================
        # Logo
        # =========================

        Label(
            self,
            text="🏥",
            bg=PRIMARY_DARK,
            fg="white",
            font=("Segoe UI", 32)
        ).pack(pady=(25,5))

        Label(
            self,
            text="KLINIK GEN-Z",
            bg=PRIMARY_DARK,
            fg="white",
            font=("Segoe UI",14,"bold")
        ).pack()

        Label(
            self,
            text="Sistem Manajemen\nData Pasien",
            bg=PRIMARY_DARK,
            fg="#DCE8FF",
            font=("Segoe UI",10),
            justify="center"
        ).pack(pady=(0,30))

        self.create_button(
            "🏠 Dashboard",
            active=="dashboard",
            self.dashboard
        )

        self.create_button(
            "👤 Data Pasien",
            active=="pasien",
            self.pasien
        )

        self.create_button(
            "📋 Antrian",
            active=="antrian",
            self.antrian
        )

        self.create_button(
            "⭐ Review",
            active=="review",
            self.review
        )

        Frame(
            self,
            bg=PRIMARY_DARK
        ).pack(expand=True, fill="both")

        self.create_button(
            "🚪 Logout",
            False,
            self.logout
        )

    def create_button(self,text,active,command):

        bg = PRIMARY if active else PRIMARY_DARK

        Button(
            self,
            text=text,
            anchor="w",
            padx=20,
            relief="flat",
            bd=0,
            bg=bg,
            fg="white",
            activebackground=PRIMARY,
            activeforeground="white",
            font=BUTTON_FONT,
            command=command
        ).pack(fill="x",ipady=10,pady=2)

    def dashboard(self):
        self.master_window.clear_frame()
        from dashboard_frame import DashboardFrame
        DashboardFrame(self.master_window)

    def pasien(self):
        self.master_window.clear_frame()
        from pasien_frame import PasienFrame
        PasienFrame(self.master_window)

    def antrian(self):
        self.master_window.clear_frame()
        from antrian_frame import AntrianFrame
        AntrianFrame(self.master_window)

    def review(self):
        self.master_window.clear_frame()
        from review_frame import ReviewFrame
        ReviewFrame(self.master_window)

    def logout(self):
        self.master_window.show_login()