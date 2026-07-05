import tkinter as tk

from login_frame import LoginFrame
from register_frame import RegisterFrame


class MainApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Sistem Manajemen Data Pasien")
        WINDOW_WIDTH = 1000
        WINDOW_HEIGHT = 800
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        from style import BACKGROUND

        self.configure(bg=BACKGROUND)
        self.resizable(False, False)

        self.show_login()

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_login(self):
        self.clear_frame()
        LoginFrame(self)

    def show_register(self):
        self.clear_frame()
        RegisterFrame(self)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

from login_frame import LoginFrame
from register_frame import RegisterFrame


class MainApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Sistem Manajemen Data Pasien")
        WINDOW_WIDTH = 1000
        WINDOW_HEIGHT = 800
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        from style import BACKGROUND

        self.configure(bg=BACKGROUND)
        self.resizable(False, False)

        self.show_login()

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_login(self):
        self.clear_frame()
        LoginFrame(self)

    def show_register(self):
        self.clear_frame()
        RegisterFrame(self)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

from login_frame import LoginFrame
from register_frame import RegisterFrame


class MainApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Sistem Manajemen Data Pasien")
        WINDOW_WIDTH = 1000
        WINDOW_HEIGHT = 800
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        from style import BACKGROUND

        self.configure(bg=BACKGROUND)
        self.resizable(False, False)

        self.show_login()

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_login(self):
        self.clear_frame()
        LoginFrame(self)

    def show_register(self):
        self.clear_frame()
        RegisterFrame(self)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

from login_frame import LoginFrame
from register_frame import RegisterFrame


class MainApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Sistem Manajemen Data Pasien")
        WINDOW_WIDTH = 1000
        WINDOW_HEIGHT = 800
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        from style import BACKGROUND

        self.configure(bg=BACKGROUND)
        self.resizable(False, False)

        self.show_login()

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_login(self):
        self.clear_frame()
        LoginFrame(self)

    def show_register(self):
        self.clear_frame()
        RegisterFrame(self)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
