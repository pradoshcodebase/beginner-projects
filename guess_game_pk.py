

from random import randint

def guess(x):
    comp_guess=randint(1,x)

    while True:
        user_guess=int(input("user guess : "))

        if comp_guess == user_guess:
            print(f"Oooof brilliant !! I guessed {comp_guess} too")
            break

        else:
            print(f"oouch!! I guessed {comp_guess} !! HHAAA")
            print("better luck next time")


def computer_guess(x):
    low=1
    high=x

    feedback=''
    while feedback != 'c':
        if low != high:
            comp_guess = randint(low, high)
        else:
            comp_guess=low  #could also be high
        feedback=input(f'Is {comp_guess} too high (H) , too low (L) or correct (C)?').lower()
        if feedback == 'l':
            low=low+1
            print(f'high:{high} low:{low}')
        else:
            high=high-1
            print(f'high:{high}  low:{low}')
    print(f"Yipeee , it's the correct number")


if __name__ == '__main__':
    computer_guess(int(input("Dear computer , guess a number under ")))
