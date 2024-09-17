from tkinter import END

def button_click(entry, number):
    # Füge die Zahl oder das Zeichen dem Eingabefeld hinzu
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + number)

def button_clear(entry):
    # Lösche das Eingabefeld
    entry.delete(0, END)
