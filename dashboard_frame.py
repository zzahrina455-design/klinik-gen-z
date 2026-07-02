from tkinter import *
from style import *
from components import Sidebar


class DashboardFrame(Frame):

    def __init__(self, master):
        super().__init__(master, bg=BACKGROUND)
        self.pack(fill="both", expand=True)

        # ===============================
        # SIDEBAR
        # ===============================

        Sidebar(self, master, "dashboard").pack(side=LEFT, fill=Y)

        # ===============================
        # CONTENT
        # ===============================

        content = Frame(self, bg=BACKGROUND)
        content.pack(side=LEFT, fill=BOTH, expand=True)

        # ===============================
        # HEADER
        # ===============================

        header = Frame(
            content,
            bg=WHITE,
            height=80,
            highlightbackground=BORDER,
            highlightthickness=1,
        )
        header.pack(fill=X)
        header.pack_propagate(False)

        Label(header, text="Selamat Datang!", bg=WHITE, fg=TEXT, font=TITLE_FONT).pack(
            anchor="w", padx=25, pady=(12, 0)
        )

        Label(header, bg=WHITE, fg=TEXT_SECONDARY, font=TEXT_FONT).pack(
            anchor="w", padx=25
        )

        # ===============================
        # BODY
        # ===============================

        body = Frame(content, bg=BACKGROUND)
        body.pack(fill=BOTH, expand=True, padx=18, pady=15)

        # ===============================
        # CARD STATISTIK
        # ===============================

        stat_frame = Frame(body, bg=BACKGROUND)
        stat_frame.pack(fill=X)

        self.create_stat_card(stat_frame, "👥", "125", "Total Pasien").grid(
            row=0, column=0, padx=5
        )

        self.create_stat_card(stat_frame, "📅", "18", "Antrian Hari Ini").grid(
            row=0, column=1, padx=5
        )

        self.create_stat_card(stat_frame, "💬", "56", "Total Review").grid(
            row=0, column=2, padx=5
        )

        self.create_stat_card(stat_frame, "⭐", "4.8", "Rating").grid(
            row=0, column=3, padx=5
        )

        for i in range(4):
            stat_frame.grid_columnconfigure(i, weight=1)

        # ===============================
        # INFORMASI
        # ===============================

        info_frame = Frame(body, bg=BACKGROUND)
        info_frame.pack(fill=BOTH, expand=True, pady=15)

        # -------------------------------
        # Informasi Klinik
        # -------------------------------

        left = Frame(
            info_frame,
            bg=WHITE,
            height=210,
            highlightbackground=BORDER,
            highlightthickness=1,
        )
        left.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))
        left.pack_propagate(False)

        Label(left, text="Informasi Klinik", bg=WHITE, fg=TEXT, font=HEADER_FONT).pack(
            anchor="w", padx=20, pady=(18, 10)
        )

        Label(
            left,
            text="• Kelola data pasien\n\n"
            "• Tambahkan antrian online\n\n"
            "• Lihat review pasien\n\n"
            "• Pelayanan lebih cepat\n\n"
            "• Data tersimpan aman",
            justify=LEFT,
            bg=WHITE,
            fg=TEXT_SECONDARY,
            font=TEXT_FONT,
        ).pack(anchor="w", padx=20)

        # -------------------------------
        # Jam Operasional
        # -------------------------------

        right = Frame(
            info_frame,
            bg=WHITE,
            width=235,
            height=210,
            highlightbackground=BORDER,
            highlightthickness=1,
        )

        right.pack(side=RIGHT, fill=BOTH)
        right.pack_propagate(False)

        Label(right, text="Jam Operasional", bg=WHITE, fg=TEXT, font=HEADER_FONT).pack(
            anchor="w", padx=20, pady=(18, 10)
        )

        jadwal = [
            ("Senin", "08.00 - 16.00"),
            ("Selasa", "08.00 - 16.00"),
            ("Rabu", "08.00 - 16.00"),
            ("Kamis", "08.00 - 16.00"),
            ("Jumat", "08.00 - 15.00"),
            ("Sabtu", "08.00 - 12.00"),
            ("Minggu", "Tutup"),
        ]

        for hari, jam in jadwal:
            row = Frame(right, bg=WHITE)
            row.pack(fill=X, padx=18, pady=2)

            Label(
                row,
                text=hari,
                bg=WHITE,
                fg=TEXT,
                font=("Segoe UI", 9),
                width=9,
                anchor="w",
            ).pack(side=LEFT)

            Label(
                row, text=jam, bg=WHITE, fg=PRIMARY, font=("Segoe UI", 9, "bold")
            ).pack(side=RIGHT)

    # ==========================================
    # CARD STATISTIK
    # ==========================================

    def create_stat_card(self, parent, icon, number, title):

        card = Frame(
            parent,
            bg=WHITE,
            width=155,
            height=120,
            highlightbackground=BORDER,
            highlightthickness=1,
        )

        card.grid_propagate(False)
        card.pack_propagate(False)

        Label(card, text=icon, bg=WHITE, font=("Segoe UI Emoji", 20)).pack(pady=(10, 2))

        Label(
            card, text=number, bg=WHITE, fg=PRIMARY, font=("Segoe UI", 17, "bold")
        ).pack()

        Label(
            card, text=title, bg=WHITE, fg=TEXT_SECONDARY, font=("Segoe UI", 9)
        ).pack()

        return card
