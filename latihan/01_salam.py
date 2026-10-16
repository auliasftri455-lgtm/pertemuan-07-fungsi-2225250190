def salam(nama):
    return f"Halo, {nama}! Selamat belajar Python."


nama_pengguna = input("Masukkan nama kamu: ")
pesan = salam(nama_pengguna)
print(pesan)