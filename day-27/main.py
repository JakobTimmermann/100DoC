import tkinter
import numpy as np


def button_clicked():
    text3["text"] = np.round(float(input_text.get()) * 1.60934, 2)
    # print("I got clicked!")


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

text1 = tkinter.Label(text="Miles")
text1.grid(column=2, row=0)

text2 = tkinter.Label(text="is equal to")
text2.grid(column=0, row=1)

text3 = tkinter.Label(text="0")
text3.grid(column=1, row=1)

text4 = tkinter.Label(text="Km")
text4.grid(column=2, row=1)

input_text = tkinter.Entry(width=7, justify='center')
input_text.grid(column=1, row=0)
input_text.config()
input_text.insert(-1, "0")

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

window.mainloop()
