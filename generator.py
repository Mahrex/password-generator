import art
from chars import *
import random
import os

while True:

    # Printing the main logo
    print(art.password)

    # User's password, started as an empty list
    your_password = []

    print('WELCOME TO PASSWORD GENERATOR! 🔐')
    print('Please choose according to your needs.')

    # NUMBERS!
    numbers_in_password = int(input('Please enter how many numbers you want to include in your password: '))
    print('Thanks!')

    # Adding numbers to the main password
    for i in range(numbers_in_password):
        num = random.choice(numbers)
        your_password.append(num)
        
    # CHARACTERS!
    alphabets_in_password = int(input('Please enter how many alphabets you want to include in your password: '))
    print('Thanks!')

    # Adding characters to the main password
    for i in range(alphabets_in_password):
        char = random.choice(alphabets)
        your_password.append(char)
        
    # SPECIAL CHARACTERS!
    special_chars_in_password = int(input('Please enter how many special characters you want to include in your password: '))
    print('Thanks!')

    # Adding special characters to the main password
    for i in range(special_chars_in_password):
        spcl = random.choice(special_chars)
        your_password.append(spcl)

    # Shuffling the main password!
    random.shuffle(your_password)

    # Making it as a string!
    new_password = ''.join(your_password)

    print(f'\nHere is your password: {new_password}\n')
    
    # Asking if they want to create again
    again = input('Do you want to create again? (Y/N): ')
    
    if again[0].upper() == 'Y':
        os.system('cls')
        continue
    elif again[0].upper() == 'N':
        print('Thanks for creating password with us. Have a nice day!')
        break
    else:
        print('Invalid input. Exiting program!')
        break