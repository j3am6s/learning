import tkinter as tk
import pandas as p
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
time = None
card = {}

# ---------------------------- DATA ------------------------------- #

data = p.read_csv("tkinter/data/french_words.csv")
to_learn = data.to_dict(orient="records")

def next_word():
    global card, time
    window.after_cancel(time)
    card = choice(to_learn)
    canvas.itemconfig(image, image=french_image)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=card["French"], fill="black")
    time = window.after(3000, flip_card, card)

def flip_card(card):
    window.after_cancel(time)
    canvas.itemconfig(image, image=english_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=card["English"], fill="white")

def wrong():
    next_word()

def right():
    global to_learn
    to_learn.remove(card)
    data = p.DataFrame(to_learn)
    data.to_csv("tkinter/data/words_to_learn.csv", index=None)
    next_word()

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

time = window.after(3000, flip_card, card)

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
french_image = tk.PhotoImage(file="tkinter/images/card_front.png")
english_image = tk.PhotoImage(file="tkinter/images/card_back.png")
image = canvas.create_image(400, 263, image=french_image)
language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

image_wrong = tk.PhotoImage(file="tkinter/images/wrong.png")
button_wrong = tk.Button(image=image_wrong, highlightthickness=0, command=wrong)
button_wrong.grid(row=1, column=0)

image_right = tk.PhotoImage(file="tkinter/images/right.png")
button_right = tk.Button(image=image_right, highlightthickness=0, command=right)
button_right.grid(row=1, column=1)

next_word()

window.mainloop()
