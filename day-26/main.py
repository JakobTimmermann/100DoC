import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pd.DataFrame(student_dict)

df = pd.read_csv("nato_phonetic_alphabet.csv")
code = {row.letter:row.code for (index, row) in df.iterrows()}

running = True
while running:
    word = input("Enter a word: ").upper()
    try:
        print([code[w] for w in word])
        running = False
    except KeyError:
        print("Sorry only letters in the alphabet.")