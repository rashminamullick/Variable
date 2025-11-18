# what is variables?
# variables refers to a value stored in memory.

# why called a variable?
#Because its value can vary and change whie the program runs.
# Try to set a number value.
# adding two numbers

num = 5
 # Here, I created two variables a & b.
#  Here I assigned the value 5 and b as the value 4. The + operator adds them together. When I ran the code, the output was 9.
### I learned that variables can store numbers, and we can perform arithmetic operations like addition using +.

# Try to set a variable with a decimal value.
# subtracting two numbers

dec = 5.5
 # Here I changed the variables values: a =8 (integer) & b = 5.5 (decimal). The subtraction operator - calculates the difference between the two numbers. Phyton automatically handles both integer and float values in arithmetic.
### I learned python supports different data types (like integers and floats) & performs arithmetic smoothly between them.

#Try to set a variable with a string value
# working with strings

name = "John"
  # Here I created a new variable name & assigned it the string value "John". When I ran the code, python displayed the text stored in the variable.
### I learned that strings (text) are stored inside quotation marks " ". print() is used to display their value.

# changing variable values


#I changed the variable name to a new value "selly". When I printed it, the new value was displayed. this shows that variables in python can be reassigned and their value can be changed too.
### I learned that when a variable's value is updated, the old value is replaced. Python automatically points the variable name to the new data in memory.

# how is using '==' different?
# == is a comparison
print (num == 5)

print(num, 'data type:', type (num))
print(dec, 'data type:', type(dec))
print(name, 'data type:', type(name))

''' • What does it mean that Python is... 
o A strongly typed language? Compare to a weakly typed language. Include 
a code example 
o A dynamically typed language? Compare to a statically typed language. 
Include a code example '''
# A strongly typed language is one in which each data type is strictly
# enforced/ variables keep their type
# Example Python
num = 1
name = 'selly'
#
#
# print(num+name) this won't work - have to convert integer to string to add
# A weakly typed language allows you to convert between variables data types
# Example
num = 1
name = 'selly'
# print(num+name)  will output 1selly
# A dynamically typed language is when you don't have to declare the
# variable types - this is checked when you run the code
# Example Python
num = 1
num = 'selly'
# we haven't had to declare what the variable type is here
# A statically typed language is when you have to declare the variable type
# - this is checked before running
# Example Delphi would have to declare variable type at the top of script
# var
# num:integer;
''' 
• Overwrite the value of one of your variables which stores a number
# o Check the id() of the variable before and after you overwrite the 
variable with a new number 
o Why does the 'id' of the variable change? 
• Assign one variable to another 
o Start with this code: 
x = 10 
y = x 
o Check the id of x and y 
o Explain why the id of x and y are the same 
o What happens if after assigning x = y, I give x a different value? 
Does the id of y change also? 
'''

# Overwrite a number variable
print('id before')
print(id(num))
num = 20
print('id after')
print(id(num))
# The id changes because it identifies the specific memory location of the
# object, not the variable name itself. If the object changes, so does its
# unique id - its pointing to different memory location

# Assigning one variable to another
x=10 # 10 is an object in the memory with an id
y=x # y is also pointing to the same object in the memory - so the id is
# the same
print('id of x')
print(id(x))
print('id of y')
print(id(y))
# The id of x and y are the same because x was assigned to y, so the id of
# y is the id of x
x=y
x=20 # new object is created with new id
# Here the id of y would not change as y hasn't been assigned to a new value
# test
print(x)
print(y)
print('id of x')
print(id(x))
print('id of y')
print(id(y))
''' 
• Ask the user for some input and print the input to the screen 
o Get the user's name and print to the screen 
o Improve previous code to: Get name, age and DOB details from a user and 
print the details to the screen 
o If time, improve previous code to: 
§ Prompt the user and get the input on the same line 
§ Print "Hi " on the one line 
'''
# Get name and print on screen:
user_input = input('Enter your name here: ')
print(user_input)
# Get name, age and DOB details from a user and print the details to the
# screen
name = input('Enter your name here: ')
age = input('Enter your age here: ')
dob = input('Enter your dob here: ')
print('Your name is', name)
print('Your age is', age)
print('Your date of birth is', dob)

# Improve previous and print Hi
print('Hi ',name,'!')



# string concatenation & type conversion

first_name = ("Taz") # These two variables store string values.
last_name = ("Khan") # Strings are always written inside quotation marks " ".
full_name = first_name + " " + last_name # Here I joined the first name & the last name together using the + operator. The " " adds a space between them.
age = 20

## when I tried the line ( without converting age), Python showed an error message. To fix it, I used type conversion by wrapping age in str():
### Here I can learn that str(age) converts the integer 20 into a sering "20". This allows Python to join it with other strings.

print(full_name + str(age))

## Below the * operator repeats a string a specific number of times, since age is 20, the name full_name repeats 20 times in one long line.

print(full_name * age)
("rollick")
# working with strings & quotes
## First, I created a variable  text and gave it a sentence inside double quotation marks:


text = " have a nice day, she added"
print(text)

# when I ran the code , it printed: have a nice day, she added. It worked perfectly because the text didn't have any extra quotes inside it.

## Now, when I tried to include another sentence that already has quotes in it
#text = " let's go shopping, "the weather is great""
#print(text)

## when I ran this above sentence, I got an error message saying: invalid syntax
## I realised that Python got confused because I used double quotes " both to start & to end the string & inside the text itself.

# To fix it, I used ecape characters(\) so Python knows the inner quotes are part of the text.

text = 'lets go shopping, \'the weather is great\''
print(text)


# This time it worked and printed.
### I learned that I can use single ' ' or double " " quotes when writing strings.
### If I want to include quotes inside my string, I must use a backslash\ to escape them.
### The backslash tells Python, 2 this next quote is part of my sentence, not the end of it."
### If I forget to escape it, Python done;t understand where my string ends & shows a syntax error.
text = 'lets go shopping, \'the weather is great\''
print(text)

### This was useful because it helped me understand how strings & quotes really work in Python.