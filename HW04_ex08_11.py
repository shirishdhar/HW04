#!/usr/bin/env python
# HW04_ex08_11

# The following functions are all intended to check whether a string contains 
# any lowercase letters, but at least some of them are wrong. For each function, 
# describe what the function actually does (assuming that the parameter is a
# string).

# Do not merely paste the output as a counterexample into the documentation 
# string, explain what is wrong.

################################################################################
# Body

def any_lowercase1(s):
   """Because of the return statement, this method will stop after checking the case of the first letter of the word. It will ignore the rest of the word.
   """
   for c in s:
       if c.islower():
           return True
       else:
           return False

def any_lowercase2(s):
   """Using c within inverted commas means that the islower() function always takes the letter 'c' (which is small case) as the parameter, and hence always holds True. 
   """
   for c in s:
       if 'c'.islower():
           return 'True'
       else:
           return 'False'

def any_lowercase3(s):
   """This will return False if the last letter of the string is Upper Case(or True if lowercase), regardless of the rest of the string.
   """
   for c in s:
       flag = c.islower()
   return flag

def any_lowercase4(s):
    """This one is right. No faults."""
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
##
def any_lowercase5(s):
##    """Due to the return statement, this method only checks the case of the first letter of every word. After checking the first letter, it returns either True or False and stops.
##    """
    for c in s:
        if not c.islower():
            return False
    return True

################################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong, 
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")
    print any_lowercase1('Abcd')
    print any_lowercase2('ABCD')
    print any_lowercase3('abcD')
    print any_lowercase5('Abcd')
    

if __name__ == '__main__':
    main()
