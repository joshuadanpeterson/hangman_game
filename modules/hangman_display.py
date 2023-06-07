def display_hangman(incorrect_attempts):
    if incorrect_attempts == 0:
        print("""
    +---+
    |   |
        |
        |
        |
        |
=========""")
    elif incorrect_attempts == 1:
        print("""
    +---+
    |   |
    O   |
        |
        |
        |
=========""")
    elif incorrect_attempts == 2:
        print("""
    +---+
    |   |
    O   |
    |   |
        |
        |
=========""")
    elif incorrect_attempts == 3:
        print("""
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========""")
    elif incorrect_attempts == 4:
        print("""
    +---+
    |   |
    O   |
   /|\  |
        |
        |
=========""")
    elif incorrect_attempts == 5:
        print("""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========""")
    elif incorrect_attempts == 6:
        print("""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========""")
    else:
        print("Invalid number of incorrect attempts.")
