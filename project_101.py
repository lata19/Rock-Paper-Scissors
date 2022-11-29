print("Welcome to Rock, Paper, Scissors game. Choose between Rock, Paper and Scissors to compete against Computer and try to win in best of 7 game. If you wanna stop just write Stop and game will be suspended.")
first_count = 0
second_count = 0
while first_count + second_count < 7:
    first = input("Choose between Rock, Paper and Scissors: ")
    first = first.capitalize()

    if first == "Stop":
        print("You stopped the game.")
        break
    if first != "Rock" and first != "Paper" and first != "Scissors":
        print("You have to choose between Rock, Paper, Scissors!")
        continue
    
    second = random.choice(["Rock", "Paper", "Scissors"])
    print(f"Computer choose: {second}")
    if first == second:
        print("It's a draw, play again!")
    elif first == "Rock" and second == "Scissors":
        print("You win!")
        first_count += 1
    elif first == "Paper" and second == "Rock":
        print("You win!")
        first_count += 1
    elif first == "Scissors" and second == "Paper":
        print("You win!")
        first_count += 1
    else:
        print("You lost")
        second_count += 1

print(f"Final result is:\nYou {first_count}:{second_count} Computer")
