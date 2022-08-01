import pandas
data = pandas.read_csv("pandas/nato_phonetic_alphabet.csv")

dic = {row.letter:row.code for (index, row) in data.iterrows()}

name = input("What's your name? ")

nom = [dic[letter.upper()] for letter in name]

print(nom)
