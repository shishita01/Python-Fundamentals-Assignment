import math
import pandas as pd
import numpy as np

import zipfile
import docx



# zip_path = r"DSassignment2/Python Fundamentals  - Module 1.zip"

# # Open the zip file
# with zipfile.ZipFile(zip_path, 'r') as z:
#     with z.open('Python Fundamentals  - Assignments/DS Internship -Python Fundamentals - Questions.docx') as f:
#         doc = docx.Document(f)

#         # Print all paragraphs
#         for para in doc.paragraphs:
#             print(para.text)



'''
Question 1: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
'''
x, y = input("Enter X,Y: ").split(',')


x = int(x)
y = int(y)

array = [[i * j for j in range(y)] for i in range(x)]

print(array)



'''
Question 2: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
'''

words = input("Enter words separated by commas: ")
word_list = words.split(',')

word_list.sort()

sorted_words = ",".join(word_list)

print(sorted_words)




'''
Question 3: Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
'''

words = input("Enter words separated by spaces: ")

word_list = words.split()
unique_words = set(word_list)

sorted_words = sorted(unique_words)

result = " ".join(sorted_words)

print(result)




'''
Question 4: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
'''

result = []

for num in range(1000, 3001):
    s = str(num) 
    all_even = True
    for char in s:
        if int(char) % 2 != 0:
            all_even = False
            break
    if all_even:
        result.append(s)


print(",".join(result))





'''
Question 5: Write a program that accepts a sentence and calculate the number of letters and digits.
'''

sentence = input("Enter a sentence: ")

letters = 0
digits = 0

for char in sentence:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print("LETTERS", letters)
print("DIGITS", digits)





'''
Question 6: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
'''

sentence = input("Enter a sentence: ")

upper = 0
lower = 0

for char in sentence:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

print("UPPER CASE", upper)
print("LOWER CASE", lower)





'''
Question 7: Write a program that computes the net amount of a bank account based a transaction log from console input.
'''

total = 0

while True:
    entry = input("Enter transaction (or press Enter to finish): ")
    if not entry:
        break
    action, amount = entry.split()
    amount = int(amount)
    if action == 'D':
        total += amount
    elif action == 'W':
        total -= amount

print(total)





'''
Question 8: A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
'''

import re

passwords = input("Enter passwords separated by commas: ").split(',')

valid_passwords = []

for pwd in passwords:
    pwd = pwd.strip()  
    if (6 <= len(pwd) <= 12 and
        re.search(r"[a-z]", pwd) and
        re.search(r"[A-Z]", pwd) and
        re.search(r"[0-9]", pwd) and
        re.search(r"[$#@]", pwd)):
        valid_passwords.append(pwd)

print(",".join(valid_passwords))





'''
Question 9: You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console.
'''

data = []
while True:
    entry = input("Enter name,age,height (or press Enter to finish): ")
    if not entry:
        break
    name, age, height = entry.split(",")
    data.append((name, age, height))

sorted_data = sorted(data, key=lambda x: (x[0], int(x[1]), int(x[2])))

print(sorted_data)





'''
Question 10: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
'''

import math

x, y = 0, 0

while True:
    move = input("Enter move (or press Enter to finish): ")
    if not move:
        break
    direction, steps = move.split()
    steps = int(steps)
    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "LEFT":
        x -= steps
    elif direction == "RIGHT":
        x += steps

distance = round(math.sqrt(x**2 + y**2))
print(distance)





'''
Question 11: Find the continuous occurrence of the string.
'''

s = input("Enter string: ")

result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result += s[i-1] + str(count)
        count = 1

result += s[-1] + str(count)

print(result)





'''
Question 12: Find the pair of alphabets in an alphanumeric string whose sum of numbers in between is always 9
'''

s = input("Enter alphanumeric string: ")


for i in range(len(s)):
    if s[i].isalpha():
        for j in range(i+1, len(s)):
            if s[j].isalpha():
                nums = s[i+1:j]
                total = sum(int(d) for d in nums if d.isdigit())
                if total == 9:
                    print(f"{s[i]},{s[j]}")






'''
Question 13: Find how many pairs in a binary number that starts and ends with 1
'''

s = input("Enter binary string: ")

indices = [i for i, char in enumerate(s) if char == '1']

n = len(indices)
pairs = n * (n - 1) // 2

print(pairs)






'''
Question 14: Find the minimum possible denominations for given valid currency.
'''

valid_currency = list(map(int, input("Enter valid currency denominations separated by space: ").split()))
money = int(input("Enter amount: "))

valid_currency.sort(reverse=True)

for coin in valid_currency:
    count = money // coin
    if count > 0:
        print(f"{coin}-{count}")
        money -= coin * count







'''
Question 15: There is a bus travelling from Town A to Town B. There are n stops between them and bus has to make m stops. Find the numbery of ways in the travel so that no stop is consecutive
'''

n = int(input("Enter total stops (n): "))
m = int(input("Enter stops to choose (m): "))

ways = math.comb(n - m + 1, m)

print("Output:", ways)





'''
Question 16: A gaming company wants to create an App with multiple games. The instruction of the games is given. You are asked to write the code to prepare the games, Where inputs will be taken from users. Once the gaming algorithm is prepared then it can be associated with production interface of the App.
'''

# Game rules
winning_cases = {
    ("Stone", "Scissor"): "A",
    ("Scissor", "Paper"): "A",
    ("Paper", "Stone"): "A",
    ("Scissor", "Stone"): "B",
    ("Paper", "Scissor"): "B",
    ("Stone", "Paper"): "B"
}

score_a = 0
score_b = 0

print("Enter moves for Player A and Player B")

while score_a < 5 and score_b < 5:
    a_move = input("Player A move: ")
    b_move = input("Player B move: ")
    
    if a_move == b_move:
        print("DRAW")
    else:
        winner = winning_cases.get((a_move, b_move))
        if winner == "A":
            score_a += 1
            print("Player A wins")
        else:
            score_b += 1
            print("Player B wins")

print("Final Score -> Player A:", score_a, "Player B:", score_b)






'''
Question 17: Validate Email Address: a. Check for '@' symbol, it should be only 1 b. Only lower-case letters are allowed c. Numbers are allowed e. No symbols allowed other than '.' & '_'
'''

email = input("Enter email: ")

# Check for single '@'
if email.count('@') != 1:
    print("Invalid email")
else:
    name, domain = email.split('@')

    if not all(c.islower() or c.isdigit() or c in '._' for c in name):
        print("Invalid email")
    else:
        if domain.count('.') != 1:
            print("Invalid email")
        else:
            parts = domain.split('.')
            if not all(part.islower() for part in parts):
                print("Invalid email")
            else:
                print("Valid email")







'''
Question 18: Solve the following patterns Input Description: row count
'''


# Number triangle pattern
rows = int(input("Enter rows: "))
num = 1
for i in range(1, rows+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()



# Diamond Star pattern
rows = int(input("Enter rows: "))
n = rows
for i in range(1, n+1):
    print(" "*(n-i) + "* " * i)
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "* " * i)



# Number pyramid with mirror
rows = int(input("Enter rows: "))
num = 1
for i in range(1, rows+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
for i in range(rows-1, 0, -1):
    num -= i
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()




# Print 'G'
rows = int(input("Enter rows: "))
for i in range(rows):
    if i == 0 or i == rows-1:
        print(" " + "***")
    elif i == rows // 2:
        print(" * ***")
    elif i < rows // 2:
        print(" *")
    else:
        print(" *    *")



# Cross pattern with odd rows
rows = int(input("Enter rows (odd number): "))
for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows-1 or j == rows//2:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()







'''
Question 19: Cyclic rotation: Case 1: first element moves to last and rest all the elements move one step to left Case 2: last element moves to first and rest all the element move one step to right Input 1 Description: 1 - first to last 2- last to first Input 2 Description : string Input 3 Description : no of times
'''

direction = int(input("Enter 1 for left rotation or 2 for right rotation: "))
string = input("Enter the string: ")
times = int(input("Enter number of times to rotate: "))

for _ in range(times):
    if direction == 1:
        string = string[1:] + string[0]
    else:
        string = string[-1] + string[:-1]
    print(string)





'''
Question 20: In a pathology lab test, there are n number of samples for testing the health condition of a patient, each slide has 5 components, Sugar level, Blood pressure, Heartbeat rate, weight and fat percentage, based on input as provided by the patient's blood report.
'''

# Ideal data for a healthy patient
healthy = {
    "Sugar level": 15,
    "Blood pressure": 32,
    "Heartbeat rate": 71,
    "weight": 65,
    "fat percentage": 10
}

# Get user input
print("Enter patient's test data:")
patient = {}
for key in healthy:
    patient[key] = int(input(f"{key}: "))

# Calculate difference
difference = {}
for key in healthy:
    diff = patient[key] - healthy[key]
    difference[key] = diff
    print(f"{key}: {abs(diff)}")

print("\nDifference Report:")
print(difference)

# Provide warnings
for key in healthy:
    diff = difference[key]
    if diff != 0:
        more_less = "more than" if diff > 0 else "less than"
        print(f"{key} {abs(diff)} {more_less} the ideal value")






'''
Question 21: Check whether the given number is Armstrong number or not Armstrong number: 153 => 1^3+5^3+3^3=153 (If summing each digit to the power of number of digits results to the same number then it is a Armstrong number)
'''

num = int(input("Enter a number: "))
digits = list(map(int, str(num)))
power = len(digits)
total = sum(d ** power for d in digits)

if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")





'''
Question 22: Convert Decimal to binary (Without inbuilt function)
'''

num = int(input("Enter a decimal number: "))
binary = ""

if num == 0:
    binary = "0"

while num > 0:
    binary = str(num % 2) + binary
    num = num // 2

print("Binary:", binary)






'''
Question 23: Find whether the given number is perfect number or not. Any number can be perfect number in Python, if the sum of its positive divisors excluding the number itself is equal to that number.
'''

num = int(input("Enter a number: "))
sum_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_divisors += i

if sum_divisors == num:
    print("Perfect number")
else:
    print("Not a perfect number")   
