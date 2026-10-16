def jumlah_n(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


n = int(input("Masukkan bilangan bulat nonnegatif: "))

if n >= 0:
    hasil = jumlah_n(n)
    print(f"Jumlah bilangan dari 1 sampai {n} adalah {hasil}")
else:
    print("Masukkan bilangan bulat nonnegatif!")