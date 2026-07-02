from tkinter import *
from tkinter import ttk, messagebox

from style import *
from components import Sidebar
from database import Database


class PasienFrame(Frame):

    def __init__(self, master):
        super().__init__(master, bg=BACKGROUND)
        self.pack(fill="both", expand=True)

        self.db = Database()

        # ======================================================
        # SIDEBAR
        # ======================================================

        Sidebar(self, master, "pasien").pack(side=LEFT, fill=Y)

        # ======================================================
        # CONTENT
        # ======================================================

        content = Frame(self, bg=BACKGROUND)
        content.pack(side=LEFT, fill=BOTH, expand=True)

        # ======================================================
        # HEADER
        # ======================================================

        header = Frame(
            content,
            bg=WHITE,
            height=80,
            highlightbackground=BORDER,
            highlightthickness=1,
        )

        header.pack(fill=X)
        header.pack_propagate(False)

        Label(
            header,
            text="Data Pasien",
            bg=WHITE,
            fg=TEXT,
            font=TITLE_FONT,
        ).pack(anchor="w", padx=25, pady=(15, 0))

        Label(
            header,
            text="Daftar seluruh pasien beserta hasil survei pelayanan.",
            bg=WHITE,
            fg=TEXT_SECONDARY,
            font=TEXT_FONT,
        ).pack(anchor="w", padx=25)

        # ======================================================
        # SEARCH
        # ======================================================

        search_frame = Frame(content, bg=BACKGROUND)
        search_frame.pack(fill=X, padx=20, pady=(15, 0))

        Label(
            search_frame,
            text="Cari Nama",
            bg=BACKGROUND,
            fg=TEXT,
            font=TEXT_FONT,
        ).pack(side=LEFT)

        self.keyword = Entry(
            search_frame,
            width=35,
            font=("Segoe UI", 10)
        )

        self.keyword.pack(side=LEFT, padx=10)

        Button(
            search_frame,
            text="Cari",
            bg=PRIMARY,
            fg="white",
            relief="flat",
            command=self.cari_data,
        ).pack(side=LEFT)

        Button(
            search_frame,
            text="Refresh",
            bg=SUCCESS,
            fg="white",
            relief="flat",
            command=self.load_data,
        ).pack(side=LEFT, padx=10)

        # ======================================================
        # CARD
        # ======================================================

        card = Frame(
            content,
            bg=WHITE,
            highlightbackground=BORDER,
            highlightthickness=1,
        )

        card.pack(fill=BOTH, expand=True, padx=20, pady=20)

        Label(
            card,
            text="Daftar Pasien",
            bg=WHITE,
            fg=TEXT,
            font=("Segoe UI", 15, "bold"),
        ).pack(anchor="w", padx=20, pady=(15, 10))

        # ======================================================
        # TABLE
        # ======================================================

        columns = (
            "ID",
            "Nama",
            "NIK",
            "Umur",
            "JK",
            "Poli",
            "Dokter",
            "Pelayanan",
            "Kebersihan",
            "Kenyamanan",
            "Kecepatan",
            "Kembali"
        )

        self.tree = ttk.Treeview(
            card,
            columns=columns,
            show="headings",
            height=15
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=110, anchor=CENTER)

        self.tree.column("ID", width=50)
        self.tree.column("Nama", width=160)
        self.tree.column("NIK", width=150)

        scroll = Scrollbar(
            card,
            orient=VERTICAL,
            command=self.tree.yview
        )

        self.tree.configure(yscrollcommand=scroll.set)

        self.tree.pack(side=LEFT,
                       fill=BOTH,
                       expand=True,
                       padx=(20, 0),
                       pady=15)

        scroll.pack(side=RIGHT, fill=Y, pady=15)

        self.load_data()

            # ======================================================
    # LOAD DATA
    # ======================================================

    def load_data(self):

        self.keyword.delete(0, END)

        for item in self.tree.get_children():
            self.tree.delete(item)

        data = self.db.fetchall("""
            SELECT
                pasien.id,
                pasien.nama,
                pasien.nik,
                pasien.umur,
                pasien.jk,
                pasien.poli,
                pasien.dokter,

                IFNULL(review.pelayanan_petugas,'-'),
                IFNULL(review.kebersihan,'-'),
                IFNULL(review.kenyamanan,'-'),
                IFNULL(review.kecepatan,'-'),
                IFNULL(review.akan_kembali,'-')

            FROM pasien

            LEFT JOIN review
            ON pasien.nama = review.nama

            ORDER BY pasien.id DESC
        """)

        for row in data:

            self.tree.insert("", END, values=row)

                # ======================================================
    # CARI DATA
    # ======================================================

    def cari_data(self):

        keyword = self.keyword.get().strip()

        for item in self.tree.get_children():
            self.tree.delete(item)

        data = self.db.fetchall(
            """
            SELECT
                pasien.id,
                pasien.nama,
                pasien.nik,
                pasien.umur,
                pasien.jk,
                pasien.poli,
                pasien.dokter,

                IFNULL(review.pelayanan_petugas,'-'),
                IFNULL(review.kebersihan,'-'),
                IFNULL(review.kenyamanan,'-'),
                IFNULL(review.kecepatan,'-'),
                IFNULL(review.akan_kembali,'-')

            FROM pasien

            LEFT JOIN review
            ON pasien.nama = review.nama

            WHERE pasien.nama LIKE ?

            ORDER BY pasien.id DESC
            """,
            ("%" + keyword + "%",)
        )

        for row in data:

            self.tree.insert("", END, values=row)

                # ======================================================
    # KEMBALI
    # ======================================================

    def kembali(self):

        self.master.clear_frame()

        from dashboard_frame import DashboardFrame

        DashboardFrame(self.master)

                bottom = Frame(content, bg=BACKGROUND)
        bottom.pack(fill=X, padx=20, pady=(0,20))

        Button(
            bottom,
            text="Kembali",
            bg=DANGER,
            fg="white",
            relief="flat",
            width=15,
            command=self.kembali
        ).pack(side=RIGHT)