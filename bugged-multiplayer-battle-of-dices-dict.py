import random
import copy

print("...___Welcome to Battle of Dices!___...")

# ===== Game Setup =====
winning_score = 3
gameover = False
rounds = 0

# Dictionary template for each player
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []
}

players = []

# === Obtain players ===
number_of_players = int(input("How many players? "))

for i in range(number_of_players):
    # Make a deep copy of the template for this player
    player = player_info.copy()
    
    player["name"] = input(f"What is the name of Player {i + 1}? ")
    player["email"] = input(f"What is the e-mail of Player {i + 1}? ")
    player["country"] = input(f"What is the country of Player {i + 1}? ")
    players.append(player)

# === Game Loop ===
while not gameover:
    print(f"\nRound {rounds + 1}:")
    input("Press ENTER to roll the dice...")
    current_rolls = []

    # Each player rolls once
    for each_player in players:
        roll = random.randint(1, 6)  # D6
        each_player["rolls"].append(roll)
        current_rolls.append(roll)
        print(f"Player {each_player['name']} rolled: {roll}")

    # Determine winners of this round
    max_roll = max(current_rolls)
    round_winners = []
    for idx, each_player in enumerate(players):
        if current_rolls[idx] == max_roll:
            each_player["wins"] += 1
            round_winners.append(each_player["name"])

    print("Winner(s) this round:", ", ".join(round_winners))

    # Check if someone reached the winning score
    for each_player in players:
        if each_player["wins"] >= winning_score:
            print(f"\n🏆 {each_player['name']} wins the game with {each_player['wins']} wins!")
            gameover = True
            break

    rounds += 1

# === Optional: Save Game Log ===
save = input("\nSave results to a file? (y/n): ").lower()
if save == "y":
    filename = input("Enter filename: ")
    with open(filename, "w") as f:
        f.write("Player Information:\n")
        for p in players:
            f.write(
                f"Name: {p['name']}\n"
                f"Email: {p['email']}\n"
                f"Country: {p['country']}\n"
                f"Wins: {p['wins']}\n\n"
            )
        f.write("\nGame rounds:\n")
        for r in range(rounds):
            rolls_str = ", ".join(
                f"{p['name']} rolled {p['rolls'][r]}" for p in players
            )
            f.write(f"Round {r + 1}: {rolls_str}\n")
    print("Game log saved successfully!")