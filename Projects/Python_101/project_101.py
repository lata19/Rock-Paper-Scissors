import random
# first = random.choice(["Rock", "Paper", "Scissors", "Lizard", "Spock"])
# second = random.choice(["Rock", "Paper", "Scissors", "Lizard", "Spock"])
# print(first)
# print(second)

# if first == "Scissors" and second == "Paper" or first == "Paper" and second == "Scissors":
#     print("Scissors cut Paper")
# elif first == "Paper" and second == "Rock" or first == "Rock" and second == "Paper":
#     print("Paper covers Rock")
# elif first == "Rock" and second == "Lizard" or first == "Lizard" and second == "Rock":
#     print("Rock crushes Lizard")
# elif first == "Lizard" and second == "Spock" or first == "Spock" and second == "Lizard":
#     print("Lizard poisons Spock")
# elif first == "Spock" and second == "Scissors" or first == "Scissors" and second == "Spock":
#     print("Spock smashes Scissors")
# elif first == "Scissors" and second == "Lizard" or first == "Lizard" and second == "Scissors":
#     print("Scissors decapitates Lizard")
# elif first == "Lizard" and second == "Paper" or first == "Paper" and second == "Lizard":
#     print("Lizard eats Paper")
# elif first == "Paper" and second == "Spock" or first == "Spock" and second == "Paper":
#     print("Paper disproves Spock")
# elif first == "Spock" and second == "Rock" or first == "Rock" and second == "Spock":
#     print("Spock vaporizes Rock")
# elif first == "Rock" and second == "Scissors" or first == "Scissors" and second == "Rock":
#     print("Rock crushes Scissors")
# elif first == second:
#     print("It's a draw, try again")

# while True:
#     first = input("Choose between Rock, Paper, Scissors, Lizard and Spock: ")
#     first = first.capitalize()
#     second = random.choice(["Rock", "Paper", "Scissors", "Lizard", "Spock"])
#     if first == "Stop":
#         print("You stopped the game.")
#         break
#     if first != "Rock" and first != "Paper" and first != "Scissors" and first != "Lizard" and first != "Spock":
#         print("You have to choose between Rock, Paper, Scissors, Lizard and Spock!")
#         continue
#     elif first == "Scissors" and second == "Paper" or first == "Paper" and second == "Scissors":
#         print("Scissors cut Paper")
#     elif first == "Paper" and second == "Rock" or first == "Rock" and second == "Paper":
#         print("Paper covers Rock")
#     elif first == "Rock" and second == "Lizard" or first == "Lizard" and second == "Rock":
#         print("Rock crushes Lizard")
#     elif first == "Lizard" and second == "Spock" or first == "Spock" and second == "Lizard":
#         print("Lizard poisons Spock")
#     elif first == "Spock" and second == "Scissors" or first == "Scissors" and second == "Spock":
#         print("Spock smashes Scissors")
#     elif first == "Scissors" and second == "Lizard" or first == "Lizard" and second == "Scissors":
#         print("Scissors decapitates Lizard")
#     elif first == "Lizard" and second == "Paper" or first == "Paper" and second == "Lizard":
#         print("Lizard eats Paper")
#     elif first == "Paper" and second == "Spock" or first == "Spock" and second == "Paper":
#         print("Paper disproves Spock")
#     elif first == "Spock" and second == "Rock" or first == "Rock" and second == "Spock":
#         print("Spock vaporizes Rock")
#     elif first == "Rock" and second == "Scissors" or first == "Scissors" and second == "Rock":
#         print("Rock crushes Scissors")
#     elif first == second:
#         print("It's a draw, try again")
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