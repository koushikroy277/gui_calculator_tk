from tkinter import *
import math

root = Tk()
root.title("Simple gui calculator")
root.minsize(400, 300)

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, width = 50, borderwidth = 5)
screen.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_add(event):
    global scvalue

    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

    
button_1 = Button(root, text="1", padx=40, pady=20)
button_1.bind('<Button-1>', button_add)

button_2 = Button(root, text="2", padx=40, pady=20)
button_2.bind('<Button-1>', button_add)

button_3 = Button(root, text="3", padx=40, pady=20)
button_3.bind('<Button-1>', button_add)

button_4 = Button(root, text="4", padx=40, pady=20)
button_4.bind('<Button-1>', button_add)

button_5 = Button(root, text="5", padx=40, pady=20)
button_5.bind('<Button-1>', button_add)

button_6 = Button(root, text="6", padx=40, pady=20)
button_6.bind('<Button-1>', button_add)

button_7 = Button(root, text="7", padx=40, pady=20)
button_7.bind('<Button-1>', button_add)

button_8 = Button(root, text="8", padx=40, pady=20)
button_8.bind('<Button-1>', button_add)

button_9 = Button(root, text="9", padx=40, pady=20)
button_9.bind('<Button-1>', button_add)

button_0 = Button(root, text="0", padx=40, pady=20)
button_0.bind('<Button-1>', button_add)

button_addition = Button(root, text="+", padx=40, pady=20)
button_addition.bind('<Button-1>', button_add)

button_minus = Button(root, text="-", padx=40, pady=20)
button_minus.bind('<Button-1>', button_add)

button_equal = Button(root, text="=", padx=40, pady=20)
button_equal.bind('<Button-1>', button_add)

button_clear = Button(root, text="C", padx=40, pady=20)
button_clear.bind('<Button-1>', button_add)

button_multi = Button(root, text="*", padx=40, pady=20, font=1)
button_multi.bind('<Button-1>', button_add)

button_divide = Button(root, text="/", padx=40, pady=20)
button_divide.bind('<Button-1>', button_add)

button_perc = Button(root, text="%", padx=40, pady=20)
button_perc.bind('<Button-1>', button_add)

button_root = Button(root, text="√", padx=40, pady=20)
button_root.bind('<Button-1>', button_add)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_equal.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
button_addition.grid(row=5, column=2)
button_minus.grid(row=5, column=0)
button_perc.grid(row=5, column=1)
button_multi.grid(row=6, column=2)
button_divide.grid(row=6, column=1)
button_root.grid(row=6, column=1)


root.mainloop()
