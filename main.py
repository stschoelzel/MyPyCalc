from tkinter import *
import layout
import functions

def main():
    window = Tk()
    window.title("MyPyCalc")
    window.geometry("600x400")

    # Erstelle das Layout und das Eingabefeld
    entry = Entry(window, width=20, borderwidth=5, font=("Arial", 18))
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Importiere das Layout aus layout.py und übergebe das Eingabefeld
    layout.create_layout(window, entry)

    window.mainloop()

if __name__ == '__main__':
    main()
