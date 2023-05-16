
stack = []

def tambah_buku(stack, buku_baru, pengarang_baru):
    stack.append(buku_baru)
    stack.append(pengarang_baru)
    print(f"{buku_baru} karya {pengarang_baru} berhasil ditambahkan ke dalam stack.")

def hapus_buku_terakhir(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada buku yang dapat dihapus")
    else:
        buku_terakhir = stack.pop()
        buku_terakhir = stack.pop()
        print(f"{buku_terakhir} berhasil dihapus dari stack.")

def tampilkan_buku_teratas(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada buku yang dapat ditampilkan.")
    else:
        buku_teratas = stack[-2]
        pengarang_teratas = stack[-1]
        print(f"Barang teratas di dalam stack adalah {buku_teratas} karya {pengarang_teratas}.")

while True:
    print("\nGudang saat ini:",stack)
    print("Menu:")
    print("1. Tambah Buku dan pengarang")
    print("2. Hapus Buku Terakhir")
    print("3. Tampilkan Buku Teratas")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan Anda (1/2/3/4):")
    
    if pilihan =="1":
        buku_baru = input("Masukkan buku baru  yang akan ditambahkan:")
        pengarang_baru = input("Masukan pengarang baru yang akan ditambahkan:")
        tambah_buku(stack, buku_baru, pengarang_baru)
    elif pilihan =="2":
        hapus_buku_terakhir(stack)
    elif pilihan =="3":
        tampilkan_buku_teratas(stack)
    elif pilihan =="4":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak Valid. Silahkan masukkan pilihan yang benar.")

