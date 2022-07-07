import pandas

data = pandas.read_csv("pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

black = 0
red = 0
gray = 0

for color in data["Primary Fur Color"]:
    if color == "Black":
        black+=1
    elif color == "Gray":
        gray+=1
    else:
        red+=1

dictionnaire = {
    "Fur Color" :  ["Black", "Gray", "Red"],
    "Count" : [black, gray, red]
}

info = pandas.DataFrame(dictionnaire)
info.to_csv("pandas/result.csv")
