import tkinter as tk

from login_frame import LoginFrame
from register_frame import RegisterFrame

# Frame berikut akan dibuat pada bagian selanjutnya
from admin_frame import AdminFrame
from dokter_frame import DokterFrame
from pasien_frame import PasienFrame


class MainApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("KLINIK GEN-Z")
        self.geometry("1000x700")
        self.resizable(False, False)

        # Mengatur konfigurasi grid pada MainApp (Window Utama)
        # agar frame yang dimasukkan bisa mengisi penuh layar secara responsif
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.current_frame = None

        self.show_login()

    # =====================================================
    # Menghapus frame yang sedang aktif
    # =====================================================
    def clear_frame(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

    # =====================================================
    # Navigasi Halaman
    # =====================================================
    def show_login(self):
        self.clear_frame()
        # Menggunakan grid untuk menempatkan frame ke jendela utama
        self.current_frame = LoginFrame(self)
        self.current_frame.grid(row=0, column=0, sticky="nsew")

    def show_register(self):
        self.clear_frame()
        self.current_frame = RegisterFrame(self)
        self.current_frame.grid(row=0, column=0, sticky="nsew")

    def show_admin(self, user):
        self.clear_frame()
        self.current_frame = AdminFrame(self, user)
        self.current_frame.grid(row=0, column=0, sticky="nsew")

    def show_dokter(self, user):
        self.clear_frame()
        self.current_frame = DokterFrame(self, user)
        self.current_frame.grid(row=0, column=0, sticky="nsew")

    def show_pasien(self, user):
        self.clear_frame()
        self.current_frame = PasienFrame(self, user)
        self.current_frame.grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
