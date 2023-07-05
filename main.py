# main.py
from option import ui
from option import nonui

def run_with_ui():
    app = ui.App()
    app.mainloop()

def run_without_ui():
    nonui.run_app()

def main():
    print("Pilih opsi:")
    print("1. Jalankan dengan antarmuka pengguna (UI)")
    print("2. Jalankan tanpa antarmuka pengguna (Non-UI)")

    choice = input("Masukkan pilihan (1/2): ")

    if choice == "1":
        run_with_ui()
    elif choice == "2":
        run_without_ui()
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
