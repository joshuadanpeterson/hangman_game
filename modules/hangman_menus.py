from modules.hangman_data import rules, credits

def display_rules():
    for rule in rules:
        print(rule)

def display_credits():
    for credit in credits:
        print(credit)

def quit():
    print("Thank you for playing! Goodbye!")
    exit(0)

def display_menu(menu, menu_message):
    print(menu_message)
    for index, option in enumerate(menu):
        print(f"{index + 1}. {option}")

def get_menu_choice(menu):
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in range(1, len(menu) + 1):
                return choice
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid choice.")