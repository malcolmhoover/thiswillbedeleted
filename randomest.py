import random

#this little program asks the user to guess a random number from 1-70.
computer_num = int(random.randint(1, 70))
correct = False
while correct == False:
    user_guess = int(input('Guess a number between 1 and 70  '))
    if user_guess > computer_num:
        print('too high homey. ')

    if user_guess < computer_num:
        print('too low my dude. ')

    elif user_guess == computer_num:
        print('that\'s exactly it! ')
