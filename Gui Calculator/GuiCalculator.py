import tkinter as tki

def button_click(number):
    current = entry.get()
    entry.delete(0, tki.END)
    entry.insert(tki.END, str(current) + str(number))

def button_clear():
    entry.delete(0, tki.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tki.END)
        entry.insert(tki.END, str(result))
    except:
        entry.delete(0, tki.END)
        entry.insert(tki.END, "Error")

def create_button(frame, text, row, col, width=7):
    button = tki.Button(frame, text=text, padx=15, pady=10, width=width,
                       command=lambda: button_click(text))
    button.grid(row=row, column=col)

# Create the main window
window = tki.Tk()
window.title("Calculator")


entry = tki.Entry(window, width=25)
entry.grid(row=0, column=0, columnspan=4, pady=10)


for i in range(9):
    create_button(window, str(i+1), 3 - i // 3, i % 3)

create_button(window, "0", 4, 0, width=15)
create_button(window, ".", 4, 1)
create_button(window, "=", 4, 2)
create_button(window, "/", 1, 3)
create_button(window, "*", 2, 3)
create_button(window, "-", 3, 3)
create_button(window, "+", 4, 3)
create_button(window, "C", 1, 2)

button_clear = tki.Button(window, text="C", padx=15, pady=10, width=7,command=button_clear)

button_clear.grid(row=1, column=2)


button_equal = tki.Button(window, text="=", padx=15, pady=10, width=7,command=button_equal)

button_equal.grid(row=4, column=2)


window.mainloop()
