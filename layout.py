from tkinter import *
import functions
import calculator


def create_layout(window, entry):
    # Definiere die Buttons und übergebe die Entry-Box und Funktionen
    button_1 = Button(window, text="1", padx=10, pady=10, command=lambda: functions.button_click(entry, "1"))
    button_2 = Button(window, text="2", padx=10, pady=10, command=lambda: functions.button_click(entry, "2"))
    button_3 = Button(window, text="3", padx=10, pady=10, command=lambda: functions.button_click(entry, "3"))
    button_4 = Button(window, text="4", padx=10, pady=10, command=lambda: functions.button_click(entry, "4"))
    button_5 = Button(window, text="5", padx=10, pady=10, command=lambda: functions.button_click(entry, "5"))
    button_6 = Button(window, text="6", padx=10, pady=10, command=lambda: functions.button_click(entry, "6"))
    button_7 = Button(window, text="7", padx=10, pady=10, command=lambda: functions.button_click(entry, "7"))
    button_8 = Button(window, text="8", padx=10, pady=10, command=lambda: functions.button_click(entry, "8"))
    button_9 = Button(window, text="9", padx=10, pady=10, command=lambda: functions.button_click(entry, "9"))
    button_0 = Button(window, text="0", padx=10, pady=10, command=lambda: functions.button_click(entry, "0"))

    button_add = Button(window, text="+", padx=10, pady=10, command=lambda: functions.button_click(entry, "+"))
    button_subtract = Button(window, text="-", padx=10, pady=10, command=lambda: functions.button_click(entry, "-"))
    button_multiply = Button(window, text="*", padx=10, pady=10, command=lambda: functions.button_click(entry, "*"))
    button_divide = Button(window, text="/", padx=10, pady=10, command=lambda: functions.button_click(entry, "/"))

    button_equal = Button(window, text="=", padx=10, pady=10, command=lambda: calculator.calculate(entry))
    button_clear = Button(window, text="C", padx=10, pady=10, command=lambda: functions.button_clear(entry))

    # Platziere die Buttons im grid-Layout
    button_7.grid(row=1, column=0, sticky="nsew")
    button_8.grid(row=1, column=1, sticky="nsew")
    button_9.grid(row=1, column=2, sticky="nsew")
    button_divide.grid(row=1, column=3, sticky="nsew")

    button_4.grid(row=2, column=0, sticky="nsew")
    button_5.grid(row=2, column=1, sticky="nsew")
    button_6.grid(row=2, column=2, sticky="nsew")
    button_multiply.grid(row=2, column=3, sticky="nsew")

    button_1.grid(row=3, column=0, sticky="nsew")
    button_2.grid(row=3, column=1, sticky="nsew")
    button_3.grid(row=3, column=2, sticky="nsew")
    button_subtract.grid(row=3, column=3, sticky="nsew")

    button_0.grid(row=4, column=0, sticky="nsew")
    button_clear.grid(row=4, column=1, sticky="nsew")
    button_equal.grid(row=4, column=2, sticky="nsew")
    button_add.grid(row=4, column=3, sticky="nsew")
