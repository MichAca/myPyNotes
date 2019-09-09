
#---Strings---

#single qoute or double quote
#Strings Are Immutable - cannot be changed
print("Hello")

#You can specify multi-line strings using triple quotes - (""" or ''').
#You can use single quotes and double quotes freely within the triple quotes.

print ('''This is an example of a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
''')

#Format Method
#How it works:
#format method can be called to substitute those specifications with corresponding arguments to the format method.
#the conversion to string would be done automatically by the format method instead of the explicit conversion to strings needed in this case.
#when using the format method, we can change the message without having to deal with the variables used and vice-versa.

age = 24
name = 'Mich'

print('{0} was {1} years old when she wrote her first program.'.format(name, age))
print('Why is {0} starting to learn python?'.format(name))

#we could have achieved the same using string concatenation but that is much uglier and error-prone.
print (name + ' is ' + str(age) + ' years old')

#the numbers are optional, so you could have also written as:
print('{} was {} years old when she wrote her first program.'.format(name, age))
print('Why is {} starting to learn python?'.format(name))

#We can also name the parameters:
#print('{name} was {age} years old when she wrote her first program.'.format(name, age))
#print('Why is {name} starting to learn python?'.format(name))

#Python 3.6 introduced a shorter way to do named parameters, called "f-strings"
# print(f"{name} was {age} years old when she wrote her first program.")
# print(f"Why is {name} starting to learn python?")


#---Integers---
print(100)

#Enclose it in qoutation marks to make it as String
print("100")


#Variables
#No need to delaclare as var, const or let
# The type of data a variable holds can be changed,
# Python variables can change the type of data a variable holds

my_name = "Mich"
my_name = "Pia"
print(my_name)

#Python allows your variables to change data type.
name = "Mich Aca"
print(name)
age = 27
print(age)
age = "Joana"
print(age)
