pesan_global = "Saya berada di luar fungsi."


def tampilkan_pesan():
    pesan_lokal = "Saya berada di dalam fungsi."

    print(pesan_global)
    print(pesan_lokal)


tampilkan_pesan()

print(pesan_global)