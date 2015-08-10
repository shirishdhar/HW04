#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
def random_guess():
    import random
    a=random.randrange(25)
    count=0                                     
    while (count<5):
        try :
            guess1=int(raw_input('Enter your guess: '))
        except:
            print('Nice try.Enter an integer')
            count+=1
        else :
            if (guess1>a):
                count+=1
                print('Too high. Try again !')
            elif (guess1<a):
                count+=1
                print('Too low. Try again !')
            else:
                print('Great! You got it!')
                return
    print ('Sorry ! You had 5 chances!!!')
    return





################################################################################
def main():

    random_guess()

    
    

if __name__ == '__main__':
    main()
