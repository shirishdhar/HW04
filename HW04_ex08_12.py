# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 12 for guidance
# Please do provide function calls that test/demonstrate your function

#See comments for explanation

def rotate_word(string, integer):
	result=''											#Creating an empty string
	for char in string:
		x=ord(char)+(integer%26)						#Calculating index of new character. A modulo-26 function is applied to allow for large integers.
		if char.islower():								#Condition that will accept only lowercase letters.
			if x>122:									#If index of new character goes beyond upper boundary, it is looped back to start again from a.
				x_high=x-26								
				result+=chr(x_high)
			elif x<97:									#If index goes below lower boundary, looped back to start from z.									
				x_low=x+26
				result+=chr(x_low)
			else:
				result+=chr(x)
		if char.isupper():								#Same process repeated for Upper case letters.
			if x>90:
				x_high=x-26
				result+=chr(x_high)
			elif x<65:
				x_low=x+26
				result+=chr(x_low)
			else:
				result+=chr(x)
	print result

rotate_word('azure', 500)								#Foolproof program, as you requested. Takes into account large integers as well as Upper case.
rotate_word('ABcd', 3)
rotate_word('abcd', -4)
