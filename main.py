import pandas as pd

# with open("nato_phonetic_alphabet.csv") as nato_alphabet:
#     nato_data = pd.read_csv(nato_alphabet)

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

user_word = input("Enter a word: ").upper()

user_word_phonetics = [nato_dict[letter] for letter in user_word]
print(user_word_phonetics)
