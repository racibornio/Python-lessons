import tkinter as tk
from tkinter import messagebox

class ListaWypelniaczApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wypełnianie listy danymi")

        self.licznik = 10
        self.lista = []

        self.label = tk.Label(root, text=f"Wpisz dane jeszcze {self.licznik} razy:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)
        self.entry.focus()

        self.button = tk.Button(root, text="Dodaj", command=self.dodaj_do_listy)
        self.button.pack(pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def dodaj_do_listy(self):
        wpis = self.entry.get().strip()
        if wpis:
            self.lista.append(wpis)
            self.licznik -= 1
            self.entry.delete(0, tk.END)

            if self.licznik > 0:
                self.label.config(text=f"Wpisz dane jeszcze {self.licznik} razy:")
            else:
                self.label.config(text="Wpisy zakończone.")
                self.entry.config(state="disabled")
                self.button.config(state="disabled")
                self.pokaz_wynik()
        else:
            messagebox.showwarning("Uwaga", "Nie możesz wpisać pustego pola!")

    def pokaz_wynik(self):
        wynik = "\n".join(self.lista)
        messagebox.showinfo("Lista danych", f"Oto Twoje dane:\n\n{wynik}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ListaWypelniaczApp(root)
    root.mainloop()