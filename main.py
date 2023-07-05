# main.py
import os

def run_with_ui():
    os.system("python option/ui.py")

def run_without_ui():
    os.system("python option/nonui.py")

def main():
    print("Pilih opsi:")
    print("1. Jalankan dengan antarmuka pengguna (UI)")
    print("2. Jalankan tanpa antarmuka pengguna (Non-UI)")
    print("3. Keluar Aplikasi")

    choice = input("Masukkan pilihan (1/2/3): ")

    if choice == "1":
        run_with_ui()
    elif choice == "2":
        run_without_ui()
    elif choice == "3":
        quit
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
