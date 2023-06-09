import random
from modules.data_structures import words

def choose_word(difficulty, theme):
    if theme not in words:
        print("Invalid theme. Choosing a random theme.")
        theme = random.choice(themes)

    word_list = words[theme]

    if difficulty == "easy":
        word_list = [word for word in word_list if len(word) <= 5]
    elif difficulty == "medium":
        word_list = [word for word in word_list if 5 < len(word) <= 8]
    elif difficulty == "hard":
        word_list = [word for word in word_list if len(word) > 8]

    if not word_list:
        print("No words available for the chosen difficulty and theme. Choosing a random word.")
        word_list = random.choice(list(words.values()))

    return random.choice(word_list)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def get_hint(word, guessed_letters):
    remaining_letters = [letter for letter in word if letter not in guessed_letters]
    return random.choice(remaining_letters)