kalimat = input("Masukkan Kalimat: ")
mulai = int(input("Index Start: "))
akhir = int(input("Index Stop: "))


def hitung_hapus(kalimat, mulai, akhir):
    hitung_awal = len(kalimat)
    hitung_akhir = len(kalimat[mulai-1:akhir])
    persentase = (hitung_akhir / hitung_awal) * 100
    return persentase


print(hitung_hapus(kalimat, mulai, akhir))
