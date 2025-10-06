print("...___Welcome to Battle of Dices!___...")
import random

# ---- Setup ----
winning_score = 3
player_names = []
player_wins = []
player_rolls_history = []

# number of players
number_of_players = int(input("How many players are playing? "))

# get player names and initialize scores & history
player_names = [input(f"Enter the name of player {i+1}: ") for i in range(number_of_players)]
player_wins = [0] * number_of_players
player_rolls_history = [[] for _ in range(number_of_players)]

rounds_played = 0
gameover = False

# ---- Game loop ----
while not gameover:
    rounds_played += 1
    print(f"Round {rounds_played}")

    current_rolls = []
    for i in range(number_of_players):
        roll = random.randint(1, 6)
        current_rolls.append(roll)
        player_rolls_history[i].append(roll)
        print(f"{player_names[i]} rolled: {roll}")

    input("\nPress ENTER to continue...")

    max_roll = max(current_rolls)

    # determine winners and update scores
    round_winners = []
    for i, r in enumerate(current_rolls):
        if r == max_roll:
            round_winners.append(player_names[i])
            player_wins[i] += 1

    print(f"Winners this round: {', '.join(round_winners)}")

    # check for champion
    for i, wins in enumerate(player_wins):
        if wins >= winning_score:
            print(f"\n{player_names[i]} wins the game with {wins} wins!")
            gameover = True
            break

    if not gameover:
        print("The battle continues!\n-----------------------------------")

# ---- Save results ----
filename = input("Enter a filename to save the log history: ")
with open(filename, "w") as file:
    for r in range(rounds_played):
        rolls_str = ", ".join(
            f"{player_names[i]} rolled {player_rolls_history[i][r]}"
            for i in range(number_of_players)
        )
        print(f"Saving: Round {r+1}: {rolls_str}")
        file.write(f"Round {r+1}: {rolls_str}\n")