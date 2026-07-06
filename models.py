from datetime import datetime
from database import Database


class UserModel:

    def __init__(self):
        self.db = Database()

    def register(self, nama, username, password, role):

        try:
            self.db.execute(
                """
            INSERT INTO users
            (nama,username,password,role)
            VALUES(?,?,?,?)
            """,
                (nama, username, password, role),
            )
            return True

        except Exception:
            return False

    def login(self, username, password):

        return self.db.fetchone(
            """
        SELECT * FROM users
        WHERE username=? AND password=?
        """,
            (username, password),
        )


# ======================================================


class AntrianModel:

    def __init__(self):
        self.db = Database()

    def ambil_nomor(self, pasien, poli):

        today = datetime.now().strftime("%Y-%m-%d")

        nomor = self.db.fetchone(
            """
        SELECT MAX(nomor)
        FROM antrian
        WHERE tanggal=?
        """,
            (today,),
        )

        if nomor[0] is None:
            nomor_baru = 1
        else:
            nomor_baru = nomor[0] + 1

        self.db.execute(
            """
        INSERT INTO antrian
        (pasien,poli,nomor,status,tanggal)
        VALUES(?,?,?,?,?)
        """,
            (pasien, poli, nomor_baru, "Menunggu", today),
        )

        return nomor_baru

    def antrian_aktif(self, pasien):

        return self.db.fetchone(
            """
        SELECT *
        FROM antrian
        WHERE pasien=?
        AND status!='Selesai'
        """,
            (pasien,),
        )

    def semua_antrian(self):

        return self.db.fetchall("""
        SELECT * FROM antrian
        ORDER BY nomor
        """)

    def update_status(self, id_antrian, status):

        self.db.execute(
            """
        UPDATE antrian
        SET status=?
        WHERE id=?
        """,
            (status, id_antrian),
        )

    def hapus(self, id_antrian):

        self.db.execute(
            """
        DELETE FROM antrian
        WHERE id=?
        """,
            (id_antrian,),
        )

    def update_status_dan_notifikasi(self, id_antrian, status):

        data = self.db.fetchone(
            """
        SELECT pasien
        FROM antrian
        WHERE id=?
        """,
            (id_antrian,),
        )

        if data is None:
            return

        pasien = data[0]

        self.db.execute(
            """
        UPDATE antrian
        SET status=?
        WHERE id=?
        """,
            (status, id_antrian),
        )

        pesan = ""

        if status == "Dipanggil":
            pesan = "Nomor antrian Anda sedang dipanggil."

        elif status == "Selesai":
            pesan = "Pelayanan selesai. Silakan mengisi survey."

        if pesan != "":
            self.db.execute(
                """
            INSERT INTO notifikasi
            (pasien,pesan,status)
            VALUES(?,?,?)
            """,
                (pasien, pesan, "Belum Dibaca"),
            )


# ======================================================


class RekamMedisModel:

    def __init__(self):
        self.db = Database()

    def simpan(self, pasien, dokter, keluhan, diagnosa, obat):

        tanggal = datetime.now().strftime("%Y-%m-%d")

        self.db.execute(
            """
        INSERT INTO rekam_medis
        (pasien,dokter,keluhan,diagnosa,obat,tanggal)
        VALUES(?,?,?,?,?,?)
        """,
            (pasien, dokter, keluhan, diagnosa, obat, tanggal),
        )

    def semua(self):

        return self.db.fetchall("""
        SELECT * FROM rekam_medis
        """)


# ======================================================


class SurveyModel:

    def __init__(self):
        self.db = Database()

    def simpan(self, pasien, pelayanan, kebersihan, keramahan, saran):

        self.db.execute(
            """
        INSERT INTO survey
        (pasien,pelayanan,kebersihan,keramahan,saran)
        VALUES(?,?,?,?,?)
        """,
            (pasien, pelayanan, kebersihan, keramahan, saran),
        )

    def semua(self):

        return self.db.fetchall("""
        SELECT * FROM survey
        """)


# ======================================================


class NotifikasiModel:

    def __init__(self):
        self.db = Database()

    def tambah(self, pasien, pesan):

        self.db.execute(
            """
        INSERT INTO notifikasi
        (pasien,pesan,status)
        VALUES(?,?,?)
        """,
            (pasien, pesan, "Belum Dibaca"),
        )

    def semua(self, pasien):

        return self.db.fetchall(
            """
        SELECT *
        FROM notifikasi
        WHERE pasien=?
        ORDER BY id DESC
        """,
            (pasien,),
        )
