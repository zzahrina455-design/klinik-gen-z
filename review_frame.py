from tkinter import *
from tkinter import ttk, messagebox
from database import Database


class ReviewFrame(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        self.db = Database()

        Label(self, text="REVIEW PASIEN", font=("Arial", 18, "bold")).pack(pady=15)

        Label(self, text="Nama Pasien")
        self.nama = Entry(self, width=35)
        self.nama.pack()

        Label(self, text="Rating")

        self.rating = ttk.Combobox(
            self, values=["1", "2", "3", "4", "5"], state="readonly", width=32
        )
        self.rating.pack()

        Label(self, text="Komentar")

        self.komentar = Text(self, width=35, height=5)

        self.komentar.pack()

        Button(self, text="Simpan Review", command=self.simpan).pack(pady=10)

        self.tree = ttk.Treeview(
            self,
            columns=("ID", "Nama", "Rating", "Komentar"),
            show="headings",
            height=8,
        )

        self.tree.heading("ID", text="ID")
        self.tree.heading("Nama", text="Nama")
        self.tree.heading("Rating", text="Rating")
        self.tree.heading("Komentar", text="Komentar")

        self.tree.pack(pady=10)

        Button(self, text="Kembali", command=self.kembali).pack()

        self.load_data()

    def simpan(self):

        if self.nama.get() == "" or self.rating.get() == "":
            messagebox.showwarning("Peringatan", "Semua data harus diisi!")
            return

        komentar = self.komentar.get("1.0", END).strip()

        self.db.execute(
            "INSERT INTO review(nama,rating,komentar) VALUES(?,?,?)",
            (self.nama.get(), self.rating.get(), komentar),
        )

        messagebox.showinfo("Berhasil", "Review berhasil disimpan.")

        self.nama.delete(0, END)
        self.rating.set("")
        self.komentar.delete("1.0", END)

        self.load_data()

    def load_data(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        data = self.db.fetchall("SELECT * FROM review")

        for row in data:
            self.tree.insert("", END, values=row)

    def kembali(self):

        self.master.clear_frame()

        from dashboard_frame import DashboardFrame

        DashboardFrame(self.master)
