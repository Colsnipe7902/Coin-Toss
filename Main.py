from random import randint
playing = True
winning_streak = 0
while playing :
    user_choice = input("Do you pick heads (1) or tails(2) ?")
    coin_face = randint(1,2)
    if user_choice == coin_face:
        winning_streak += 1
        print(f"That's correct! You're on a {winning_streak} winning streak!")
        print("Thats correct!")
    else:
        print("You guessed wrong.  😢")
        playing = False
grand_prize_streak = 5
if grand_prize_streak >= winning_streak:
    print(f"You're streak is {winning_streak} and you've won 100$")
elif winning_streak +1== grand_prize_winning_streak:
    pass
