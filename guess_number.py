import random
guess_count = 0
guess = random.randint(1,100)
while True:
    player_guess = int(input("Enter Your Guess:"))
    if player_guess < 1 or player_guess > 100:
        print("Out of Bounds")
    elif abs(player_guess - guess) == 0:
        guess_count += 1
        print(f"Correct Guess in {guess_count} attempts")
        break
    elif abs(player_guess - guess) in range(5,11):
        guess_count += 1
        print("Warm!")
    elif abs(player_guess - guess) in range(0,5):
        guess_count += 1
        print("Warmer!")
    elif abs(player_guess - guess) > 10:
        guess_count += 1
        print("Cold!")