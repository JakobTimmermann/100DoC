import tkinter as tk
import pandas as pd
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
word = ""
translation = ""
flip_timer = None
# ---------------------------- WORD MANGER ------------------------------- #
try:
    data = pd.read_csv("data/palabras_espanolas_quedado.csv", header=None, index_col=0).squeeze("columns").to_dict()
except FileNotFoundError:
    data = pd.read_csv("data/palabras_espanolas.csv", header=None, index_col=0).squeeze("columns").to_dict()


def lo_se():
    del data[word]
    pd.DataFrame(data.items()).to_csv("data/palabras_espanolas_quedado.csv", index=False, header=False)
    pick_a_word()


def pick_a_word():
    global word, flip_timer, translation, data
    try:
        window.after_cancel(flip_timer)
    except ValueError:
        pass
    word = random.choice(list(data))
    translation = data[word]
    canvas.itemconfig(palabra, text=word, fill="black")
    canvas.itemconfig(idioma, text="Espanol", fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(4000, flip_card)
    remaining_words.config(text=f"Palabras restantes: {len(data)}")


# ---------------------------- FLIP CARD ------------------------------ #
def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(palabra, text=translation, fill="white")
    canvas.itemconfig(idioma, text="German", fill="white")


# ---------------------------- UPDATE TRANSLATION ------------------------------ #
def update_translation():
    data[word] = add_translation.get()
    pd.DataFrame(data.items()).to_csv("data/palabras_espanolas_quedado.csv", index=False, header=False)
    pick_a_word()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Flashly")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.option_add('*Dialog.msg.width', 34)
window.option_add('*Dialog.msg.font', 'Helvetica 10')

card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")

canvas = tk.Canvas(width=900, height=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = canvas.create_image(450, 450, image=card_front)
idioma = canvas.create_text(450, 300, text="Espanol", fill="black", font=(FONT_NAME, 15, "italic"))
palabra = canvas.create_text(450, 450, text=word, fill="black", font=(FONT_NAME, 22, "bold"))
canvas.grid(column=0, row=1, columnspan=3)


remaining_words = tk.Label(text=f"Palabras restantes: {len(data)}", bg=BACKGROUND_COLOR, font=(FONT_NAME, 9, "bold"))
remaining_words.grid(column=1, row=0)

check_mark_image = tk.PhotoImage(file="images/right.png")
red_cross = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=red_cross, highlightthickness=0, command=pick_a_word)
wrong_button.grid(column=2, row=3)
right_button = tk.Button(image=check_mark_image, highlightthickness=0, command=lo_se)
right_button.grid(column=0, row=3)

add_translation = tk.Entry(width=19)
add_translation.grid(column=1, row=2)
update_button = tk.Button(text="Change translation", highlightthickness=0, command=update_translation)
update_button.grid(column=1, row=3)

pick_a_word()

tk.mainloop()
