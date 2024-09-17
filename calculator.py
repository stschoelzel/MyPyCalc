from tkinter import END

def calculate(entry):

    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")
