def hitung_statistik(daftar_angka):
    total = sum(daftar_angka)
    rata_rata = total / len(daftar_angka)
    nilai_minimum = min(daftar_angka)
    nilai_maksimum = max(daftar_angka)

    return total, rata_rata, nilai_minimum, nilai_maksimum


angka = input("Masukkan angka dipisahkan dengan spasi: ")
daftar_angka = [float(x) for x in angka.split()]

if len(daftar_angka) > 0:
    total, rata_rata, minimum, maksimum = hitung_statistik(daftar_angka)

    print(f"Jumlah: {total}")
    print(f"Rata-rata: {rata_rata}")
    print(f"Nilai minimum: {minimum}")
    print(f"Nilai maksimum: {maksimum}")
else:
    print("Masukkan minimal satu angka.")