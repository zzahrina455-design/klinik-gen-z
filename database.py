import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect("pasien.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):

        # ==========================
        # USERS
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
        """)

        # ==========================
        # PASIEN
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS pasien(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            nik TEXT,
            umur TEXT,
            jk TEXT,
            alamat TEXT,
            nohp TEXT,
            poli TEXT,
            dokter TEXT
        )
        """)

        # ==========================
        # ANTRIAN
        # (sementara masih dipakai)
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS antrian(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            poli TEXT,
            dokter TEXT,
            tanggal TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # ==========================
        # REVIEW / SURVEI
        # ==========================
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS review(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            pelayanan_petugas TEXT,
            kebersihan TEXT,
            kenyamanan TEXT,
            kecepatan TEXT,
            akan_kembali TEXT,
            saran TEXT
        )
        """)
        self.conn.commit()

    # ==========================
    # EXECUTE
    # ==========================
    def execute(self, query, values=()):
        self.cursor.execute(query, values)
        self.conn.commit()

    # ==========================
    # FETCH ONE
    # ==========================
    def fetchone(self, query, values=()):
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    # ==========================
    # FETCH ALL
    # ==========================
    def fetchall(self, query, values=()):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    # ==========================
    # CLOSE DATABASE
    # ==========================
    def close(self):
        self.conn.close()
