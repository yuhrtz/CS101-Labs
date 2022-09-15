import random
print('Welcome to the Flarsheim Guesser!\n')

def main():
    print('Please think of a number between and including 1 and 100.')

    remainder_3 = int(input('\n What is the remainder when your number is divided by 3 ?'))

    while remainder_3 != 0 or 1 or 2:
        if remainder_3 < 0:
            print('The value must be 0 or greater')
            remainder_3 = int(input('\n What is the remainder when your number is divided by 3 ?'))
        elif remainder_3 > 2:
            print('The value must be less than 3')
            remainder_3 = int(input('\n What is the remainder when your number is divided by 3 ?'))
        else:
            break

    remainder_5 = int(input('\n What is the remainder when your number is divided by 5 ?'))

    while remainder_5 != 0 or 1 or 2 or 3 or 4:
        if remainder_5 < 0:
            print('The value must be 0 or greater')
            remainder_5 = int(input('\n What is the remainder when your number is divided by 5 ?'))
        elif remainder_5 > 4:
            print('The value must be less than 5')
            remainder_5 = int(input('\n What is the remainder when your number is divided by 5 ?'))
        else:
            break

    remainder_7 = int(input('\n What is the remainder when your number is divided by 7 ?'))

    while remainder_7 != 0 or 1 or 2 or 3 or 4 or 5 or 6:
        if remainder_7 < 0:
            print('The value must be 0 or greater')
            remainder_7 = int(input('\n What is the remainder when your number is divided by 7 ?'))
        elif remainder_7 > 6:
            print('The value must be less than 7')
            remainder_7 = int(input('\n What is the remainder when your number is divided by 7 ?'))
        else:
            break

    for n in range(1, 101):
        if n % 3 == remainder_3 and n % 5 == remainder_5 and n % 7 == remainder_7:
            print(f'Your number was {n}')
            print('How amazing is that?')

    play_again = input('Do you want to play again? Y to continue, N to quit ==>')

    while play_again != 'Y' or 'y' or 'N' or 'n':
        if play_again == 'Y' or 'y':
            main()
        if play_again == 'N' or 'n':
            break
    
main()





