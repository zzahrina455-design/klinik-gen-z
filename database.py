import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):

        # ==========================
        # USERS
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
        """)

        # ==========================
        # ANTRIAN
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS antrian(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pasien TEXT,
            poli TEXT,
            nomor INTEGER,
            status TEXT,
            tanggal TEXT
        )
        """)

        # ==========================
        # REKAM MEDIS
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS rekam_medis(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pasien TEXT,
            dokter TEXT,
            keluhan TEXT,
            diagnosa TEXT,
            obat TEXT,
            tanggal TEXT
        )
        """)

        # ==========================
        # SURVEY
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS survey(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pasien TEXT,
            pelayanan INTEGER,
            kebersihan INTEGER,
            keramahan INTEGER,
            saran TEXT
        )
        """)

        # ==========================
        # NOTIFIKASI
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS notifikasi(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pasien TEXT,
            pesan TEXT,
            status TEXT
        )
        """)

        self.conn.commit()

        self.create_default_account()

    # =================================================

    def create_default_account(self):

        self.cursor.execute("SELECT * FROM users WHERE username=?", ("admin",))

        if self.cursor.fetchone() is None:

            self.cursor.execute(
                """
            INSERT INTO users
            (nama,username,password,role)
            VALUES(?,?,?,?)
            """,
                ("Administrator", "admin", "admin123", "admin"),
            )

        self.cursor.execute("SELECT * FROM users WHERE username=?", ("dokter",)
                            )

        if self.cursor.fetchone() is None:

            self.cursor.execute(
                """
            INSERT INTO users
            (nama,username,password,role)
            VALUES(?,?,?,?)
            """,
                ("Dokter", "dokter", "dokter123", "dokter"),
            )

        self.conn.commit()

    # =================================================

    def execute(self, query, values=()):
        self.cursor.execute(query, values)
        self.conn.commit()

    def fetchone(self, query, values=()):
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def fetchall(self, query, values=()):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
