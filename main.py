import tkinter as tk

from login_frame import LoginFrame
from register_frame import RegisterFrame
from style import BACKGROUND


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # ===============================
        # Pengaturan Window
        # ===============================
        self.title("Sistem Manajemen Data Pasien")

        WINDOW_WIDTH = 1000
        WINDOW_HEIGHT = 800

        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.configure(bg=BACKGROUND)
        self.resizable(False, False)

        # Menampilkan halaman pertama
        self.show_login()

    # ===============================
    # Menghapus semua frame yang sedang tampil
    # ===============================
    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    # ===============================
    # Halaman Login
    # ===============================
    def show_login(self):
        self.clear_frame()
        LoginFrame(self)

    # ===============================
    # Halaman Register
    # ===============================
    def show_register(self):
        self.clear_frame()
        RegisterFrame(self)


# ===============================
# Menjalankan Program
# ===============================
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
