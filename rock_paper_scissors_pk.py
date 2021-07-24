import random

flag='y'
while flag=='y':
    print("'r' for rock, 'p' for paper , 's' for scissors")
    user_guess=input("user guess : ")
    comp_guess=random.choice(['r','p','s'])
    print(f'computer guess : {comp_guess}')

    # s>p p>r r>s
    if user_guess==comp_guess:
        print("It's a tie")
    elif user_guess == "r":
        if comp_guess == "s":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_guess == "p":
        if comp_guess == "r":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_guess == "s":
        if comp_guess == "p":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    flag=input("Do you want to play again ? ").lower()