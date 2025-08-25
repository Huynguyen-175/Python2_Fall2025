# Review for python chapters 3 - 5 
# get user input for average and calculate the grade
average = float(input("Enter the average:"))
if average >= 90:
    letter_grade = 'A'
elif average >= 80:
    letter_grade = 'B'
elif average >= 70:
    letter_grade = 'C'
elif average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'
print(f'Your final grade is {letter_grade}')

# match case
login_status = 1
match login_status:
    case 1: print('Invalid user name')
    case 2: print('Invalid password')
    case 3: print('Successfully login')
    case _: print('Invalid input')

# Another way to write match case
match login_status:
    case 1 | 2 : print('Invalid user name / password')
    case login_status if login_status !=3: print('Invalid input')
    case 3: print('Successfully login')

# Random number/character
import random
num1 = random.randint(1,10)
num2 = random.randrange(1,10)     #last number not included
print(f'Randomly generated numbers: {num1} {num2}')

ch = chr(random.randint(ord('a'),ord('z')))
print(f'The random character is {ch}')

# Check vowel
ch = input('Enter a character: ')
if ch.upper() in 'AEIOU': 
    print(f'{ch} is vowel')

# count vowel
word = input('Enter a word:')
count = 0 
for ch in word.strip():  #strip : remove the space in front and back of strings
    if ch.upper() in 'AEIOU':
        count +=1
print(f'There are {count} vowels in {word}')

# Loops
# Sentinel value controlled loop
SENTINEL = -99
total = 0
count = 0 
num = float(input('Enter a grade (or -99 to end):'))
while num != SENTINEL:
    if num >= 0 and num <= 100:
        total += num
        count += 1
    else:
        print('Invalid grade, enter again')
    num = float(input('Enter a grade (or -99 to end):'))

if count > 0:
    average = total / count
    print(f'The average is {average:.2f}')
