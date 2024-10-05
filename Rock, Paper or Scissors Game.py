import random

rock = 'Rock ✊'
paper = 'Paper ✋'
scissors = 'Scissors ✌️'

print("="*40)
print("Welcome to Rock-Paper-Scissors Game! 🎮")
print("Winning Rules:")
print("-" * 40)
print("Rock ✊ vs Paper ✋ -> Paper wins 🏆")
print("Rock ✊ vs Scissors ✌️ -> Rock wins 🏆")
print("Paper ✋ vs Scissors ✌️ -> Scissors wins 🏆")
print("="*40)

while True:
    print("\nYour Options:")
    print("[r] Rock ✊\n[p] Paper ✋\n[s] Scissors ✌️")

    player_move = input("Choose [r], [p], or [s]: ").lower().strip()
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print("❌ Invalid choice. Please try again...")
        continue

    computer_random_number = random.randint(1, 3)
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"\n🧑 You chose: {player_move}")
    print(f"💻 Computer chose: {computer_move}\n")

    if (player_move == rock and computer_move == scissors) or \
       (player_move == paper and computer_move == rock) or \
       (player_move == scissors and computer_move == paper):
        print("🎉 You win! 🏆")
    elif player_move == computer_move:
        print("🤝 It's a draw!")
    else:
        print("😞 You lose!")

    while True:
        play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
        if play_again == "y":
            print("\n🔄 Restarting the game...")
            break
        elif play_again == "n":
            print("\n👋 Thank you for playing! Goodbye!")
            exit()
        else:
            print("❌ Invalid input. Please enter 'y' for yes or 'n' for no.")
