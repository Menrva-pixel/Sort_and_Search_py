# main.py
import os
from art import *

def run_with_ui():
    os.system("python option/ui.py")

def run_without_ui():
    os.system("python option/nonui.py")

   
tprint("APLIKASI")
 


def main():
    print("Pilih opsi:")
    print("1. Jalankan dengan antarmuka pengguna (UI)")
    print("2. Jalankan tanpa antarmuka pengguna (Non-UI)")
    print("3. Keluar Aplikasi")


    while True:
        choice = input("Masukkan pilihan (1/2/3): ")

        if choice == "1":
            run_with_ui()
            break
        elif choice == "2":
            run_without_ui()
            break
        elif choice == "3":
            print("Aplikasi selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
