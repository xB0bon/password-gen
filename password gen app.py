from tkinter import *
from tkinter import messagebox
import string
import random


def copy():
    try:
        text_to_copy = wynik.get()
        window.clipboard_clear()
        window.clipboard_append(text_to_copy)
        messagebox.showinfo("Skopiowano", "Tekst został skopiowany do schowka")
    except Exception as e:
        messagebox.showerror("Błąd kopiowania", f"Wystąpił błąd podczas kopiowania {e}")


def gen():
    try:
        length = int(dlugosc.get())
        if length <= 0 or length > 90:
            messagebox.showinfo("Długość hasła", "Długość hasła powinna być większa niż 0 i mniejsza niż 90")
            return
    except ValueError:
        messagebox.showinfo("Wpisz długość hasła!", "Wpisz długość hasła przed generowaniem!")
        return

    all_chars = ""
    if var1.get():
        all_chars += string.ascii_lowercase
    if var2.get():
        all_chars += string.ascii_uppercase
    if var3.get():
        all_chars += string.punctuation
    if var4.get():
        all_chars += string.digits

    if not all_chars:
        messagebox.showinfo("Wybierz opcje!", "Wybierz przynajmniej jeden rodzaj znaków do generowania hasła!")
        return

    password = "".join(random.choices(all_chars, k=length))
    wynik.config(state="normal")
    wynik.delete(0, END)
    wynik.insert(0, password)
    wynik.config(state="readonly")


window = Tk()
window.geometry("400x500")
window.title("Generator Hasła")
window.configure(bg="#f7f7f7")

title_label = Label(window, text="Generator Hasła", font=("Arial", 30, "bold"), bg="#f7f7f7", pady=10)
title_label.pack()

length_label = Label(window, text="Podaj długość hasła:", font=("Arial", 12), bg="#f7f7f7")
length_label.pack(pady=(20, 5))
dlugosc = Entry(window)
dlugosc.pack(ipady=5)

allowed_chars_label = Label(window, text="Dozwolone znaki: ", font=("Arial", 12), bg="#f7f7f7")
allowed_chars_label.pack(pady=5)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

checkbox_malelitery = Checkbutton(window, text="Małe litery [a-z]", variable=var1, bg="#f7f7f7")
checkbox_malelitery.pack()
checkbox_duzelitery = Checkbutton(window, text="Duże litery [A-Z]", variable=var2, bg="#f7f7f7")
checkbox_duzelitery.pack()
checkbox_znaki = Checkbutton(window, text="Znaki specjalne [!@$]", variable=var3, bg="#f7f7f7")
checkbox_znaki.pack()
checkbox_liczby = Checkbutton(window, text="Liczby [1,2,3,4..]", variable=var4, bg="#f7f7f7")
checkbox_liczby.pack()

generate_button = Button(window, text="Generuj", command=gen, bg="#5cb85c", fg="white", padx=10, pady=5)
generate_button.pack(pady=20)

wynik_label = Label(window, text="Wygenerowane hasło:", font=("Arial", 12), bg="#f7f7f7")
wynik_label.pack(pady=(20, 5))
wynik = Entry(window, state="readonly", width=40)
wynik.pack(ipady=5)

copy_button = Button(window, text="Skopiuj", bg="#5bc0de", fg="white", command=copy, padx=10, pady=5)
copy_button.pack(pady=20)

window.mainloop()
