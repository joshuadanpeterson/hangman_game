import random
import time
from modules.data_structures import words
from modules.hangman_data import difficulties, game_states, menu_options, menu_messages, high_scores, rules, credits, main_menu, game_menu, high_scores_menu, rules_menu, credits_menu, main_menu_menu
from modules.hangman_display import display_hangman
from modules.hangman_words import choose_word, display_word
from modules.hangman_scores import update_high_scores, get_high_scores, calculate_score
from modules.hangman_menus import display_menu, get_menu_choice, display_credits, display_rules, quit

# Constants
MAX_ATTEMPTS = 6
MAX_LEVELS = 3
MAX_LOSSES = 3
TIME_PER_LETTER = 10

themes = list(words.keys())

# Game Play
def enter_player_name():
    return input("Enter your name: ")

def play_hangman():
    print("Game start! Let's play Hangman.")
    
    player_name = enter_player_name()

    # Choose difficulty
    display_menu(game_menu, menu_messages["game menu"])
    difficulty_choice = get_menu_choice(game_menu)

    # Return to main menu if choice is 4
    if difficulty_choice == 4:
        return

    difficulty = difficulties[difficulty_choice - 1]

    # Choose theme
    theme = random.choice(themes)
    print(f"Theme chosen: {theme}")

    # Choose word
    word = choose_word(difficulty, theme)
    print(f"Word chosen, length: {len(word)}")

    guessed_letters = []
    incorrect_attempts = 0

    start_time = time.time()

    while True:
        # Display hangman
        display_hangman(incorrect_attempts)
        print(display_word(word, guessed_letters))

        # Get guess
        guess = input("Guess a letter or enter 'guess' to guess the entire word: ").lower()
        
        if guess == "guess":
            # Guess the entire word
            word_guess = input("Enter your word guess: ").lower()
            if word_guess == word:
                elapsed_time = time.time() - start_time
                print(f"Congratulations! You've guessed the word: {word}")
                score = calculate_score(player_name, word, MAX_ATTEMPTS, incorrect_attempts, elapsed_time)
                update_high_scores(player_name, score)
                break
            else:
                incorrect_attempts += 1
                print("Sorry, that's not the correct word.")
        else:
            # Check letter guess
            if guess in word:
                guessed_letters.append(guess)
                print(f"Good job! {guess} is in the word.")
            else:
                incorrect_attempts += 1
                print(f"Sorry, {guess} is not in the word.")

        # Check if game is over
        if incorrect_attempts >= MAX_ATTEMPTS:
            elapsed_time = time.time() - start_time
            print("You've run out of attempts. Game over.")
            print(f"The word was: {word}")
            score = calculate_score(player_name, word, MAX_ATTEMPTS, incorrect_attempts, elapsed_time)
            update_high_scores(player_name, score)
            break
        elif set(guessed_letters) == set(word):
            elapsed_time = time.time() - start_time
            print(f"Congratulations! You've guessed the word: {word}")
            score = calculate_score(player_name, word, MAX_ATTEMPTS, incorrect_attempts, elapsed_time)
            update_high_scores(player_name, score)
            break

def main():
    print("Welcome to Hangman!")
    print("Please choose an option from the menu below.")

    while True:
        display_menu(main_menu, menu_messages["main menu"])
        choice = get_menu_choice(main_menu)
        menu_functions[menu_options[choice - 1]]()

menu_functions = {
    "play": play_hangman,
    "high scores": get_high_scores,
    "rules": display_rules,
    "credits": display_credits,
    "quit": quit
}

if __name__ == "__main__":
    main()
