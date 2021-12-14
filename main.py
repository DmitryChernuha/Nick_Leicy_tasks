# 1
name = input('Enter your firstname, please: ')
print(f'Hi, {name}')

# 2
firstname = input('Enter your firstname, please: ')
lastname = input('Enter your lastname, please: ')
print(f'Hi, {firstname} {lastname}')

# 3
print('What do you call a bear with no teeth\nA gummy bear')

# 4
num_1, num_2 = int(input('Enter first number: ')), int(input('Enter second number: '))
print(f'The total is: {num_1 + num_2}')

# 5
num_1, num_2, num_3 = int(input('Enter first number: ')),\
                      int(input('Enter second number: ')),\
                      int(input('Enter third number: '))
print(f'The answer is: {(num_1 + num_2) * num_3}')

# 6
pizza_start = int(input('How many peaces of pizza do you have? '))
pizza_eat = int(input('How many peaces of pizza do you eat? '))
pizza_finish = pizza_start - pizza_eat
print(f'Now you have {pizza_finish} peaces of pizza')

# 7
name, age = input('Please enter your name: '), int(input('Please enter your age: '))
print(f'{name}, next birthday you will be {age + 1}')

# 8
all_price = float(input('Enter all price: $'))
peoples = int(input('How many peoples: '))
people_to_pay = all_price / peoples
print('Each man need to pay: $%.2f' % people_to_pay)

# 9
day = int(input('Enter day: '))
hours = day * 24
minutes = hours * 60
seconds = minutes * 60
print(f'{day} days includes: {hours} hours, {minutes} minutes and {seconds} seconds.')

# 10
POUND_IN_KG = 2.204
kg = float(input('Enter you weight in kg: '))
foot = kg * POUND_IN_KG
print('Your weight in pounds: %.2f' % foot)

# 11
num_1 = int(input('Enter number > 100: '))
num_2 = int(input('Enter number < 10: '))
num = num_1 // num_2
print(f'{num_2} in {num_1} {num}')

# 12
num_1, num_2 = int(input('Enter first num: ')), int(input('Enter second num: '))
if num_1 > num_2:
    print(num_2, num_1)
else:
    print(num_1, num_2)

# 13
num = int(input('Enter first num < 20: '))
if num >= 20:
    print('Too High')
else:
    print('Thank you')

# 14
num = int(input('Enter num from 10 to 20: '))
if num >= 10 and 20 >= num:
    print('Thank you')
else:
    print('Incorrect answer')

# 15
colour = input('Enter your favorite colour: ').lower()
if colour == 'red':
    print('I like red too')
else:
    print(f'I dont like {colour}, I like red')

# 16

answer_1 = input('It is rainy now? (yes/no): ').lower()
if answer_1 == 'yes':
    answer_2 = input('It is windy? (yes/no): ').lower()
    if answer_2 == 'yes':
        print('It is to windy for an umbrella')
    else:
        print('Take answer_1 umbrella')
else:
    print('Enjoy your day')

# 17
age = int(input('Enter your age: '))
if age >= 18:
    print('You can vote')
elif age == 17:
    print('You can learn to drive')
elif age == 16:
    print('You can by a lottery ticket')
elif age < 16:
    print('You can go Trick')

# 18
num = int(input('Enter number: '))
if num < 10:
    print('Too low')
elif num >=10 and num <=20:
    print('Correct')
else:
    print('Too high')

# 19
num = input('Enter 1 or 2 or 3: ')
if num == '1':
    print('Thank you')
elif num == '2':
    print('Well done')
elif num == '3':
    print('Correct')
else:
    print('Error message')

# 20
name = input()
print(len(name))

# 21
first_name, last_name = input('Enter first name: '), input('Enter last name: ')
fool_name = first_name + ' ' + last_name
length = len(fool_name)
print(fool_name)
print(length)

# 22
first_name, last_name = input('Enter first name: '), input('Enter last name: ')
fool_name = first_name.title() + ' ' + last_name.title()
print(fool_name)

# 23
phrase = input('Enter phrase: ')
print(f'Length of this phrase {len(phrase)} letters')
start, stop = int(input('Enter start slice: ')), int(input('Enter stop slice: '))
print(phrase[start:stop + 1])

# 24
name = input('Enter your name: ')
print(name.upper())

# 25
first_name = input('Enter your name: ')
if len(first_name) < 5:
    last_name = input('Enter your lastname: ')
    fool_name = first_name + last_name
    print(fool_name.upper())
elif len(first_name) >= 5:
    print(first_name.lower())

# 26
word = input('Enter word: ').lower()
if word[0] in 'euioa':
    word_1 = word + 'way'
    print(f'{word} in pig {word_1}')
else:
    word_2 = word[1:] + word[0] + 'ay'
    print(f'{word} in pig {word_2}')

# 27
num = float(input('Enter a float num: '))
res = num * 2
print(round(res, 2))

# 28
import math
print(round(math.pi, 5))

# 29
from math import sqrt
print(round(sqrt(int(input('Enter a num other 500: ')))))

# 30
import math
r, h = float(input('Enter radius: ')), float(input('Enter high: ')),
volume = math.pi * r ** 2 * h
print(round(volume, 2))

num = int(input('Enter 1 or 2: '))
if num == 1:
    sq_line = float(input('Enter square line: '))
    sq_area = sq_line * sq_line
    print(f'Square area: {round(sq_area, 2)}')
elif num == 2:
    tr_line = float(input('Enter triangle line: '))
    tr_height = float(input('Enter triangle hight: '))
    tr_area = 0.5 * tr_line * tr_height
    print(f'Triangle area: {round(tr_area, 2)}')
else:
    print('Enter error')

# 35
name = input('Enter your name: ')
for i in range(1, 4):
    print(name)

# 36
count = int(input('Enter count: '))
name = input('Enter your name: ')
for i in range(1, count + 1):
    print(f'{i}. {name}')

# 37
name = input('Enter your name: ')
count = int(input('Enter count: '))
for i in range(0, count):
    for letter in name:
        print(letter)

# 38
for i in range(1, 10):
    print()
    for j in range(1, 10):
        print(f'{i} x {j} = {i * j}')

# 39
num = int(input('Enter num: '))
for i in range(1, 11):
    print(f'{i} x {num} = {i * num}')

# 40
num = int(input('Enter num below 50: '))
for i in range(50, num - 1, -1):
    print(i)

# 41
num = int(input('Enter num: '))
name = input('Enter your name: ')
if num < 10:
    for i in range(1, num + 1):
        print(name)
else:
    for i in range(1, 4):
        print('Too high')

# 42
total = 0
for i in range(1, 6):
    num = int(input('Enter num: '))
    word = input('Do you want consist this num to total (y/n): ')
    if word == 'y':
        total += num
print(total)

# 43
direction = input('In what direction you enter (u/d): ')
if direction == 'u':
    num = int(input('Enter num: '))
    for i in range(1, num + 1):
        print(i)
elif direction == 'd':
    num = int(input('Enter num below 20: '))
    for i in range(20, num + 1, -1):
        print(i)
else:
    print('I dont understand')

# 44
question = int(input('How many people on your party: '))
if question < 10:
    for i in range(1, question + 1):
        name = input('Enter guest name: ')
        print(f'{name.title()}, has been invited')
else:
    print('To many people')

# 45
total = 0
while total < 50:
    num = int(input('Enter num: '))
    total += num
    print(f'The total is {total}')

# 46
num = int(input('Enter num: '))
while num < 5:
    num = int(input('Enter num: '))
else:
    print(f'Last number enter was {num}')

# 47
first_num = int(input('Enter first num: '))
second_num = int(input('Enter second num: '))
total = first_num + second_num
ques = input('Do you want continue (y/n): ')
while ques == 'y':
    num = int(input('Enter cont num: '))
    total += num
    ques = input('Do you want continue (y/n): ')
print(f'Total is {total}')

# 48
count = 0
answer = input('Do yo want to invite? (y/n) ')
while answer == 'y':
    name = input('Enter guest name: ')
    print(f'{name} has invited')
    answer = input('Do yo want to invite? (y/n) ')
    count += 1
print(f'Yo invite {count} guest')

# 49
compnum = 50
count = 1
num = 0
while num != compnum:
    num = int(input('Enter num: '))
    if num < compnum:
        print('Too low')
    elif num > compnum:
        print('Too high')
        num = int(input('Enter num: '))
    elif num == compnum:
        print('Well done')
    count += 1
print(f'Well done. You took {count} attempts')

# 50
import random
x = 0
num = random.randint(1, 1000)
count = 0
while True:
    x = int(input('Enter num: '))
    if x < num:
        print('Too low')
    elif x > num:
        print('Too high')
    elif x == num:
        print('You win')
        break
    count += 1
print(f'You play {count}')

# 69
country_tuple = ('USA', 'Germany', 'Great Britain', 'France', 'Sweden', 'USA')
print(*country_tuple, sep=', ')
country = input('Enter country from this tuple: ')
print(country_tuple[int(country)])
print(country_tuple.index(country_tuple[int(country)]))
print(country_tuple.count(country_tuple[int(country)]))
print(len(country_tuple))

# 70
sport_lst = ['Tennis', 'Diving', 'Kitesurfing', 'Subbording']
sport = input('Enter your favorite kind of sport: ')
sport_lst.append(sport)
print(*sport_lst, sep=', ')
sport_lst.remove('Tennis')
print(*sport_lst, sep=', ')
sport_lst.append('Caving')
print(*sport_lst, sep=', ')
sport_lst.insert(3, 'Snowbording')
print(*sport_lst, sep=', ')
sport_lst[3] = 'Trekking'
print(*sport_lst, sep=', ')
print(sport_lst[0])
print(*sport_lst, sep=', ')
del sport_lst[0]
print(sport_lst, sep=', ')
sport_lst.sort()
print(sport_lst, sep=', ')
sport_lst.reverse()
print(*sport_lst, sep=', ')
sport_string = ', '.join(sport_lst)
print(sport_string.upper())
num_arr = [num for num in range(1, 101, 5)]
# print(num_arr)
lst = input().split(',')
lst_1 = []
for l in lst:
    lst_1.append(l)
print(lst_1)

# 73
food_dict = {}
food_dict[1] = input('Enter your favorite foods first: ')
food_dict[2] = input('Enter your favorite foods second: ')
food_dict[3] = input('Enter your favorite foods third: ')
food_dict[4] = input('Enter your favorite foods fourd: ')
print(food_dict)
del_food = int(input())
del food_dict[del_food]

# 74
colour_lst = ['red', 'blue', 'white', 'grey', 'black', 'yellow', 'pink', 'green', 'orange', 'purple']
print(*colour_lst)
num_start, num_emd = int(input('Enter start num (0-4): ')), int(input('Enter end num (5 -9): '))
print(colour_lst[num_start:num_emd + 1])

# 75
num_lst = list(i for i in range(125, 859, 200))
print(num_lst)
print(num_lst[0])
print(num_lst[1])
print(num_lst[2])
print(num_lst[3])
num_user = int(input('Enter num three digit: '))
if num_user in num_lst:
    print(num_lst.index(num_user))
else:
    print(f'{num_user} is not in the list')

# 76
name_1 = input('Enter name of your friends: ')
name_2 = input('Enter name of your friends: ')
name_3 = input('Enter name of your friends: ')
names = [name_1, name_2, name_3]
n = 3
answ = input('Do you want to invite another friends (y/n): ')
while answ == 'y':
    name = names.append(input('Enter name of your friends: '))
    answ = input('Do you want to invite another friends (y/n): ')
print(f'You invite {len(names)} friends on your party')
print(names)
name_search = input('Enter name of your friends: ')
print(names.index(name_search))
question = input(f'Do you want {names.index(name_search)} be on your parti (y/n): ?')
if question == 'n':
    names.remove(name_search)
print(names)

# 77
tv = ['RenTV', 'TV 3', 'ORT', '1 + 1']
for i in tv:
    print(i)
tv_add = input('Enter your favorite TV: ')
position_tv_add = int(input('Enter your favorite TV position: '))
tv.insert(position_tv_add, tv_add)
print(tv)
for i in tv:
    print(i)

# 79
nums = list()
n = 1
while n <= 3:
    num = input('Enter num: ')
    nums.append(num)
    n += 1
num_del = input('Do you want to dell last nun (y/n): ')
if num_del == 'y':
    del nums[-1]
print(nums)

# 80
first_name = input('Enter your name: ')
print(len(first_name))
last_name = input()
print(len(last_name))
full_name = f'{first_name} {last_name}'
print(full_name)
print(len(full_name))

# 81
subject = input('Enter your favorite subject: ')
subj_letters = []
for letter in subject:
    subj_letters.append(letter)
print(*subj_letters, sep='-', end='-')

# 82
text = input('Enter your favorite string: ')
start = int(input('Enter start slice: '))
finish = int(input('Enter finish slice: '))
print(text[start:finish])

# 82
name = input('Enter your name in upper case: ')
tryagain = False
while tryagain == False:
    if name.isupper():
        print('Thank you!')
        try = True
    else:
        print('Try agayn')
        name = input('Enter your name in upper case: ')

# 84
postcode = input()
start = postcode[0:2].upper()
print(f'{start} {postcode[2:]}')

# 85
name = input('Enter your name: ').lower()
name_lst_vovels = []
for let in name:
    if let in 'uioae':
        name_lst_vovels.append(let)
print(len(name_lst_vovels))

# 86
password = input('Enter password: ')
password_again = input('Enter password: ')
if password == password_again:
    print('Correct psw')
elif password.lower() == password_again.lower():
    print('Enter in lover case')
elif password != password_again:
    print('Incorect')

# 87
text = input('Enter word: ')
text_1 = text[::-1]
print(text_1)
for let in text_1:
    print(let)

# 88
file = open('countries.txt', 'w')
file.write('Italy\n')
file.write('Germany\n')
file.write('Spain\n')
file.write('Great britain\n')
file.write('Italy\n')
file.write('Germany\n')
file.write('Spain\n')
file.write('Great britain\n')
file.write('Italy\n')
file.write('Germany\n')
file.write('Spain\n')
file.write('Great britain\n')
file.close()

file = open('countries.txt', 'r')
print(file.read())

file = open('countries.txt', 'a')
file.write('France\n')

file = open('countries.txt', 'r')
print(file.read())


file = open('Names.txt', 'w')
file.write('Dmitry\n')
file.write('Ivan\n')
file.write('Petro\n')
file.write('Sirco\n')
file.write('Stepan\n')

file = open('Names.txt', 'r')
print(file.read())

name = input('Enter new name: ')
file = open('Names.txt', 'a')
file.write(name)

file = open('Names.txt', 'r')
print(file.read())

file = open('pi_digit.txt', 'w')
file.write('3.1415926535\n')
file.write('8979323846\n')
file.write('2643383279\n')

file = open('pi_digit.txt', 'r')
print(file.read())

name = input('Enter your name: ')
file = open('name.txt', 'w')
file.write(f'{name}\n')

file = open('name.txt', 'w')
name = input('Enter your name: ')
while name != 'y':
    name = input('Enter your name: ')
    file = open('name.txt', 'a')
    file.write(f'{name}\n')
file = open('name.txt', 'r')
print(file.read())
subject = open('subject.txt', 'w')
subject.write('Computer science\n')
subject = open('subject.txt', 'r')
print(subject.read())
num = int(input('Enter num (1, 2, 3): '))
if num == 1:
    sub = input('Enter your favorite subject: ')
    subject = open('subject.txt', 'w')
    subject.write(f'{sub}')
elif num == 2:
    subject = open('subject.txt', 'r')
    print(subject.read())
elif num == 3:
    subj = input('Enter your favorite subject: ')
    subject = open('subject.txt', 'a')
    subject.write(f'{subj}\n')
    subject = open('subject.txt', 'r')
    print(subject.read())


# 118
def get_num():
    num = int(input('Enter num: '))
    return num


def get_num_sum(num):
    num_lst = list(i for i in range(1, num + 1))
    print(sum(num_lst))
    return sum(num_lst)


get_num_sum(num=get_num())


def get_name():
    name = input('Enter name: ')
    return name


def get_message(name):
    print(f'Hello {name}')


def main():
    name = get_name()
    get_message(name)

main()

# 119
import random


def get_number():
    num_start = int(input('Enter start number: '))
    num_finish = int(input('Enter finish number: '))
    comp_num = random.randint(num_start, num_finish)
    print(comp_num)
    return comp_num


def find_number(comp_num):
    print('I am thinking of a number: ')
    your_num = int(input('Enter comp number: '))
    while your_num != comp_num:
         if your_num == comp_num:
           print('You win!!!')
         elif your_num < comp_num:
            print('Too low')
         elif your_num > comp_num:
            print('Too high')
        your_num = int(input('Enter comp number: '))



find_number(comp_num=get_number())

# 139
# import sqlite3 as sq
#
# # with sq.connect('phones.db') as con:
# #     cur = con.cursor()
# #     cur.execute("""CREATE TABLE IF NOT EXISTS phones (
# #     ID INTEGER PRIMARY KEY AUTOINCREMENT,
# #     First_Name TEXT NOT NULL,
# #     Surname TEXT NOT NULL,
# #     Phone Number INTEGER NOT NULL
# #     )""")

import sqlite3

with sqlite3.connect('phones.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS phones (
    ID INTEGER PRIMARY KEY,
    First_Name TEXT NOT NULL,
    Surname TEXT NOT NULL,
    Phone_Number INTEGER NOT NULL
    )""")


new_id = int(input('Enter ID: '))
new_first_name = input('Enter first name: ')
new_last_name = input('Enter last name: ')
new_phone_number = int(input('Enter phone_number: '))

cur.execute("""INSERT INTO phones (ID, First_Name, Surname, Phone_Number)
    VALUES(?, ?, ?, ?)""", (new_id, new_first_name, new_last_name, new_phone_number))
con.commit()
cur.close()
cur.execute("""INSERT INTO phones (ID, First_Name, Surname, Phone_Number)
    VALUES (10, 'Grigir', 'Scovoroda', 79785696367)""")
con.commit()
con.close()

