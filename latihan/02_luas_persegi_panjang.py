def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas


panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

hasil = luas_persegi_panjang(panjang, lebar)
print(f"Luas persegi panjang adalah {hasil}")