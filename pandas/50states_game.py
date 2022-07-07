import pandas
import turtle

screen = turtle.Screen()
image = "pandas/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

fichier = pandas.read_csv("pandas/50_states.csv")
score = 0
donne = []

def check(answer):
    for name in fichier["state"]:
        if answer == name:
            return True
    else:
        return False

while score!=50:
    answer_state = screen.textinput(title="Guess the State", prompt=f"{score}/50 What's another state?")
    answer = answer_state.title()
    if answer == "Exit":
        break
    if check(answer):
        if answer not in donne:
            donne.append(answer)
            score+=1
            jean = turtle.Turtle()
            jean.hideturtle()
            jean.penup()
            a = fichier[fichier["state"]==answer]
            jean.goto(int(a["x"]), int(a["y"]))
            jean.write(answer)

pastrouve = [state for state in fichier["state"].tolist() if state not in donne]

states_to_learn = pandas.DataFrame(pastrouve)
states_to_learn.to_csv("pandas/states_to_learn.csv")
