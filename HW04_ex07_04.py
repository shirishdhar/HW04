#!/usr/bin/env python
# HW04_ex07_04

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:
    
#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes the
# resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

################################################################################
# Imports
import math  #I tried to make the code comprehensive. So for any other input apart from 'done', it will prompt the user to enter another expression. But the problem comes in the if x=='done' loop, which only works if I don't add '+ a' to it. If I add + a, the code never enters that loop somehow !
def eval_loop(x):
    try:
        a = eval(x)
        print a
        new_x=raw_input('Enter any mathematical expression: ')
        eval_loop(new_x)
    except:
        if x=='done':
            print ('Evaluated value of last expression is: ' + str(a))
        else:
            print 'Invalid Input. Try Again!'
            new_x=raw_input('Enter any mathematical expression: ')
            eval_loop(new_x)
            
 #       print('Evaluated value of last expression: ' + "'" + str(a) + "'." + ' Goodbye!')
 #       else:
#            print('Invalid Input')
  #          new_x=raw_input('Enter any mathematical expression: ')
#            eval_loop(new_x)
            
        
        
        

# Body




################################################################################
def main():
    x=raw_input("Enter any mathematical expression: ")
    eval_loop(x)
    

if __name__ == '__main__':
    main()
