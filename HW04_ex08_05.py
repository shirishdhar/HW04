#!/usr/bin/env python
# HW04_ex08_05

# The following program counts the number of times the letter a appears in a 
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print count

# Encapsulate this code in a function named "count", and generalize it so that 
# it accepts the string and the letter as arguments.

################################################################################
# Imports

def count(word, letter):
    counter = 0
    for i in word:
        if i == letter:
            counter = counter + 1
    print counter


# Body




################################################################################
def main():

    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters
    count('mississipi', 's')
    count('hallelujah', 'l')
    
    

if __name__ == '__main__':
    main()
