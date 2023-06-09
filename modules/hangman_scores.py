import os

current_dir = os.path.dirname(os.path.abspath(__file__))
high_scores_file = os.path.join(current_dir, "high_scores.txt")

def update_high_scores(player_name, score):
    try:
        with open(high_scores_file, "a") as file:
            file.write(f"{player_name}: {score}\n")
    except IOError:
        print("Error occurred while updating high scores.")

def get_high_scores():
    try:
        with open(high_scores_file, "r") as file:
            scores = file.readlines()
            scores = [score.strip() for score in scores]
            scores = sorted(scores, key=lambda x: int(x.split(":")[1]), reverse=True)
            print("High Scores:")
            for rank, score in enumerate(scores, start=1):
                print(f"{rank}. {score}")
    except IOError:
        print("No high scores found.")

def calculate_score(player_name, word, max_attempts, incorrect_attempts, word_guess=0):
    base_score = len(word) * 10
    attempt_penalty = (max_attempts - incorrect_attempts) * 5

    word_bonus = len(word_guess) * 20 if word_guess is not None and isinstance(word_guess, str) else 0
    return max(base_score - attempt_penalty + word_bonus, 0)

