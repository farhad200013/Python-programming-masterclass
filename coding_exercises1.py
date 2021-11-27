

"""
Coding Exercise 1 - Printing text
Write the code to print out the string
My hovercraft is full of eels
"""
print("My hovercraft is full of eels")


"""
Coding Exercise 2 - Printing the result of a calculation
Write a program to print the answer to the calculation 6 times 7
"""
print(6 * 7)



"""
Coding Exercise 3 - Printing tabs
Write a program that will produce the following output.
All the text should appear in your program's output.

Number 1    The Larch
Number 2    The Horse Chestnut
"""
print("Number 1\tThe Larch")
print("Number 2\tThe Horse Chestnut")


"""
Coding Exercise 4 - Integer division
You have a shop selling buns for $2.40 each.
A customer comes in with $15, and would like to buy as many buns as possible.
Complete the code to calculate how many buns the customer can afford.
"""
bun_price = 2.40
money = 15
print(money // bun_price)


"""
Coding Exercise 5 - Using if with strings
Write a small program that assigns the name of 2 trees to 2 variables, called tree1 and tree 2.
If the values of the 2 variables are equal
print the message 'The trees are the same',
otherwise print 'The trees are different'.
"""
tree1 = 'put your first tree name here'
tree2 = 'put your second tree name here'

if tree1 == tree2:
    print("The trees are the same")
else:
    print("The trees are different")




"""
Coding Exercise 6 - Simple condition
Write a small program that assigns the value 5 to one variable,
called x, and the value 7 to another, called y.

Your program should then use an if statement to compare the values,
and print out 'x is greater than y' if x is greater,
or 'x is smaller than y' if y is greater.
If x equals y, print out 'x equals y'
"""
x = 5
y = 7

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is smaller than y")
else:
    print("x equals y")


"""
Coding Exercise 8 - Extracting capitals
Write a program to print out the capital letters in the string

"Alright, but apart from the Sanitation, the Medicine, Education,
Wine, Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?"
"""
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
for i in quote:
    if i.istitle():
        print(i)



"""
Coding Exercise 9 - For loop with step
Write a program to print out all the numbers from 0 to 100 that are divisible by 7.
Note that zero is considered to be divisible by all other integers, so your output should include zero.
"""
for i in range(0, 101, 7):
    if i % 7 == 0:
        print(i)




"""
Coding Exercise 10 - Break
Modify the code so that it stops printing when it reaches a number that's exactly divisible by 11.
That number should be the last value printed.

Reminder: If a value, x, is divisible by 11 then x % 11 will be zero.
"""
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break






"""
Coding Exercise 11 - Continue
Write a program to print out all the numbers from 0 to 20 that aren't divisible by 3 or 5.
Zero is considered divisible by everything (zero should not appear in the output).
The aim is to use the continue statement, but it's also possible to do this without continue.
"""
for i in range(0, 21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    else:
        print(i)


"""
Coding Exercise 12 - Augmented assignment in a loop
Early computers could only perform addition.
In order to multiply one number by another, they performed repeated addition.
For example, 5 * 8 was performed by adding 5 eight times

5 + 5 + 5 + 5 + 5 + 5 + 5 + 5 = 40.
Use a for loop, and augmented assignment,
to give answer the result of multiplying number by multiplier.
"""
number = 5
multiplier = 8
answer = 0

for i in range(multiplier):
    answer += number

print(answer)



"""
Section 4 Challenge - If Then Else
Write a small program to ask for a name and an age.
When both values have been entered, check if the person
is the right age to go on 18-30 holiday (they must be over 18 and under 31).
If they are, welcome them to the holiday, otherwise print
a (polite) message refusing them entry.
"""
name = input("Please enter your name: ")
age = int(input("How old are you, {}? ".format(name)))

if 18 <= age <= 30:
    print("Welcome {} you can go on a holiday!".format(name))
else:
    print("Sorry {} you cannot go for a holiday".format(name))



"""
Section 4 Challenge - Program Flow
Create a program that takes an IP address entered at the keyboard
and prints out the number of segments it contains, and the length of each segment.

An IP address consists of 4 numbers, separated from each other with a full stop.
But your program should just count however many are entered.
Examples of the input you may get are:
    127.0.0.1
    .192.168.0.1
    10.0.123456.255
    172.16
    255

So your program should work even with invalid IP addresses.
We're just interested in the number of segments and how long each one is.

Once you have a working program, here are some more suggestions for invalid input to test:
    .123.45.678.91
    123.4567.8.9
    123.156.289.10123456
    10.10t.10.10
    12.9.34.6.12.90
    '' - that is, press enter without typing anything

This challenge is intended to practise for loops and if/else statements, so although
you could se other techniques (such as splitting the string up), that's not the
approach we're looking for here.
"""
ipAddress = input("Please enter an IP address: ")
ipAddress += '.'
segment_counter = 0
segment = 1

for i in ipAddress:
    if i == '.':
        print("segment {} contains {} characters".format(segment, segment_counter))
        segment_counter = 0
        segment += 1
    else:
        segment_counter += 1



"""
Section 4 Challenge - While Loop
Modify the program below to use a while loop to
allow as many guesses as necessary.

The program should let the player know whether to
guess higher or lower, and should print a message
when the guess is correct. A correct guess will
terminate the program

As an optional extra, allow the player to quit
by entering 0 (zero) for their guess.
"""
import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0

while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    elif guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("Well done, you guessed it")
