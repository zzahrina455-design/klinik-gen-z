from tkinter import *
from tkinter import ttk, messagebox

from database import Database


class PasienFrame(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        self.db = Database()
        self.selected_id = None

        Label(self, text="DATA PASIEN",
              font=("Arial", 18, "bold")).pack(pady=10)

        Label(self, text="Nama")
        self.nama = Entry(self, width=35)
        self.nama.pack()

        Label(self, text="Umur")
        self.umur = Entry(self, width=35)
        self.umur.pack()

        Label(self, text="Alamat")
        self.alamat = Entry(self, width=35)
        self.alamat.pack()

        Button(self, text="Tambah",
               command=self.tambah).pack(pady=5)

        Button(self, text="Update",
               command=self.update).pack(pady=5)

        Button(self, text="Hapus",
               command=self.hapus).pack(pady=5)

        self.tree = ttk.Treeview(
            self,
            columns=("ID", "Nama", "Umur", "Alamat"),
            show="headings",
            height=8
        )

        self.tree.heading("ID", text="ID")
        self.tree.heading("Nama", text="Nama")
        self.tree.heading("Umur", text="Umur")
        self.tree.heading("Alamat", text="Alamat")

        self.tree.bind("<<TreeviewSelect>>", self.pilih_data)

        self.tree.pack(pady=10)

        Button(
            self,
            text="Kembali",
            command=self.kembali
        ).pack()

        self.load_data()

    def load_data(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        data = self.db.fetchall(
            "SELECT * FROM pasien"
        )

        for row in data:
            self.tree.insert("", END, values=row)

    def tambah(self):

        self.db.execute(
            "INSERT INTO pasien(nama,umur,alamat) VALUES(?,?,?)",
            (
                self.nama.get(),
                self.umur.get(),
                self.alamat.get()
            )
        )

        messagebox.showinfo("Berhasil", "Data berhasil ditambahkan")

        self.load_data()

    def pilih_data(self, event):

        data = self.tree.focus()

        if data:

            values = self.tree.item(data)["values"]

            self.selected_id = values[0]

            self.nama.delete(0, END)
            self.umur.delete(0, END)
            self.alamat.delete(0, END)

            self.nama.insert(0, values[1])
            self.umur.insert(0, values[2])
            self.alamat.insert(0, values[3])

    def update(self):

        if self.selected_id is None:
            return

        self.db.execute(
            "UPDATE pasien SET nama=?,umur=?,alamat=? WHERE id=?",
            (
                self.nama.get(),
                self.umur.get(),
                self.alamat.get(),
                self.selected_id
            )
        )

        messagebox.showinfo("Berhasil", "Data berhasil diubah")

        self.load_data()

    def hapus(self):

        if self.selected_id is None:
            return

        self.db.execute(
            "DELETE FROM pasien WHERE id=?",
            (self.selected_id,)
        )

        messagebox.showinfo("Berhasil", "Data berhasil dihapus")

        self.load_data()

    def kembali(self):

        self.master.clear_frame()

        from dashboard_frame import DashboardFrame

        DashboardFrame(self.master)