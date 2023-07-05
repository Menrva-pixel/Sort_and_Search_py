angka = []  # Mendeklarasikan sebuah list kosong

# Fungsi untuk melakukan sorting angka
def sorting():
    angka.sort()
    print("Hasil sorting:", angka)

# Fungsi untuk melakukan searching angka
def searching():
    x = int(input("Masukkan angka yang ingin dicari: "))
    if x in angka:
        print("Angka ditemukan")
    else:
        print("Angka tidak ditemukan")

# Main program
while True:
    print("MENU PILIHAN")
    print("1. Input angka")
    print("2. Sorting")
    print("3. Searching")
    print("4. Selesai")

    pilihan = int(input("Masukkan pilihan [1/2/3/4]: "))

    if pilihan == 1:
        n = int(input("Masukkan jumlah angka: "))
        angka = []
        for i in range(n):
            angka.append(int(input("Angka {}: ".format(i + 1))))
    elif pilihan == 2:
        sorting()
    elif pilihan == 3:
        searching()
    elif pilihan == 4:
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

print("Selesai")
