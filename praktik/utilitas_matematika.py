def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar


def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi


def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def faktorial(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil


def main():
    while True:
        print("\n=== UTILITAS MATEMATIKA ===")
        print("1. Luas Persegi Panjang")
        print("2. Luas Segitiga")
        print("3. Jumlah Bilangan 1 sampai n")
        print("4. Faktorial")
        print("0. Keluar")

        pilihan = input("Pilih menu (0-4): ")

        if pilihan == "1":
            panjang = float(input("Masukkan panjang: "))
            lebar = float(input("Masukkan lebar: "))
            hasil = luas_persegi_panjang(panjang, lebar)
            print("Luas persegi panjang:", hasil)

        elif pilihan == "2":
            alas = float(input("Masukkan alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            hasil = luas_segitiga(alas, tinggi)
            print("Luas segitiga:", hasil)

        elif pilihan == "3":
            n = int(input("Masukkan bilangan bulat nonnegatif: "))
            if n >= 0:
                print("Jumlah:", jumlah_n(n))
            else:
                print("Bilangan tidak boleh negatif.")

        elif pilihan == "4":
            n = int(input("Masukkan bilangan bulat nonnegatif: "))
            if n >= 0:
                print("Faktorial:", faktorial(n))
            else:
                print("Bilangan tidak boleh negatif.")

        elif pilihan == "0":
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")


if __name__ == "__main__":
    main()

# Pengujian:
# Luas persegi panjang: 8 x 5 = 40
# Luas segitiga: 0.5 x 10 x 6 = 30
# Jumlah bilangan 1 sampai 10 = 55
# Faktorial 5 = 120
# Faktorial 0 = 1