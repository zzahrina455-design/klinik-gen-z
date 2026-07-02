class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Pasien:

    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat


class Antrian:

    def __init__(self, nama, poli, dokter):
        self.nama = nama
        self.poli = poli
        self.dokter = dokter


class Review:

    def __init__(self, nama, rating, komentar):
        self.nama = nama
        self.rating = rating
        self.komentar = komentar