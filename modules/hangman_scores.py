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

def calculate_score(player_name, word, max_attempts, incorrect_attempts, elapsed_time):
    base_score = len(word) * 10
    attempt_penalty = (max_attempts - incorrect_attempts) * 5
    time_penalty = int(elapsed_time)  # Penalty for each second over the time limit
    return max(base_score - attempt_penalty - time_penalty, 0)
