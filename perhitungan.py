import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplikasi Penyortiran dan Pencarian Angka")
        self.geometry("400x400")
        self.configure(bg="#f0f0f0")  # Set background color

        self.angka = []

        self.create_widgets()

    def create_widgets(self):
        # Label
        label = ttk.Label(self, text="Aplikasi Penyortiran dan Pencarian Angka", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Frame untuk tombol
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        # Tombol Input Angka
        input_button = ttk.Button(button_frame, text="Input Angka", command=self.input_angka)
        input_button.grid(row=0, column=0, padx=5, pady=5)

        # Tombol Sorting
        sorting_button = ttk.Button(button_frame, text="Sorting", command=self.sorting)
        sorting_button.grid(row=0, column=1, padx=5, pady=5)

        # Tombol Searching
        searching_button = ttk.Button(button_frame, text="Searching", command=self.searching)
        searching_button.grid(row=0, column=2, padx=5, pady=5)

        # Tombol Selesai
        selesai_button = ttk.Button(button_frame, text="Selesai", command=self.quit)
        selesai_button.grid(row=0, column=3, padx=5, pady=5)

        # Kotak Masukan
        input_frame = ttk.Frame(self)
        input_frame.pack(pady=10)

        input_label = ttk.Label(input_frame, text="Masukkan angka: ")
        input_label.grid(row=0, column=0)

        self.input_entry = ttk.Entry(input_frame)
        self.input_entry.grid(row=0, column=1)

        # Area Output
        output_frame = ttk.Frame(self)
        output_frame.pack(pady=10)

        output_label = ttk.Label(output_frame, text="Output:")
        output_label.grid(row=0, column=0)

        self.output_text = tk.Text(output_frame, height=10, width=30)
        self.output_text.grid(row=1, column=0)

    def input_angka(self):
        input_value = self.input_entry.get()
        if input_value.isdigit():
            angka = int(input_value)
            self.angka.append(angka)
            self.input_entry.delete(0, tk.END)
            self.output_text.insert(tk.END, f"Angka {angka} telah ditambahkan.\n")
        else:
            self.output_text.insert(tk.END, "Masukkan angka yang valid.\n")

    def sorting(self):
        if len(self.angka) > 0:
            sorted_angka = sorted(self.angka)
            self.output_text.insert(tk.END, "Hasil sorting: " + ", ".join(str(num) for num in sorted_angka) + "\n")
        else:
            self.output_text.insert(tk.END, "Belum ada angka yang dimasukkan.\n")

    def searching(self):
        if len(self.angka) > 0:
            search_value = self.input_entry.get()
            if search_value.isdigit():
                angka = int(search_value)
                if angka in self.angka:
                    self.output_text.insert(tk.END, f"Angka {angka} ditemukan.\n")
                else:
                    self.output_text.insert(tk.END, f"Angka {angka} tidak ditemukan.\n")
            else:
                self.output_text.insert(tk.END, "Masukkan angka yang valid.\n")
        else:
            self.output_text.insert(tk.END, "Belum ada angka yang dimasukkan.\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()
