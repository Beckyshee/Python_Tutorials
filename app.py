import math
import convertors
from utils import find_max
from ecommerce.shipping import calc_shipping
import random
from pathlib import Path

#print('Hi I am Becky Kariuki')
#print('I have a daughter and her name is Peyson')
#print('*' * 10)

#VARIABLES - used to temporarily store data in a comps memory
#price = 10
# #resetting price to new value
# price = 20
# rating = 4.8
# name = 'Becky'
# is_female = True
# #print(price)
# #exercise 1
# name = 'John Smith'
# age = 20
# is_new_patient = True
#print("Hi i am " + name + "and I am" + age)

#RECEIVING INPUT FROM USER -----> input function always returns a string
#birth_year = input('Birth year: ')
#age = 2023 - int(birth_year)
#print(age)
#exercise 2
#weight_pounds = input('weight in pounds: ')
#weight_kgs = int(weight_pounds) * 0.45
#print(weight_kgs)

#course = 'Python for Beginners'
#another = course[:]
#print(course[-3])
#print(course[0:5])
#print(course[:3])
#print(course[:])
#print(another)
# exercise 3
#name = 'Jessica'
#print(name[1:-1])

#FORMATTED STRINGS
#first = 'John'
#last = 'Doe'
#message = first + '[' + last + '] is a nurse'
#msg = f'{first} [{last}] is a nurse' #the formatted string
#print(msg)
#print(message)

#STRING METHODS
#course = 'python for beginners'
#print(len(course))  #object size usin the general purpose function len
#print(course.upper()) #using the upper method
#print(course.lower())
#print(course.find('beg'))
#print(course.replace('beginners', 'Absolute beginners'))
#print(course) #OG method
#print('python' in course) #using the in operator to check if python is in the course variable answer for this expression is a boolean

#ARITHMETIC OPERATORS
#print(10+3)
#print(10/3)
#print(10//3) #division in int value
#print(10%3) #modulus
#print(10**3) #power/exponent
#x = 10
#x = x + 3 # another way to write it below
#x -= 3 #enhanced / argumented assignment operator ans = 7 delete the one above to get accurate ans.
#print(x)

#OPERATOR PRECEDENCE
#x = 10 + 3 * 2 ** 2 #we used BODMAS sort of (the order parenthesis exponential multiplication then add and sub)
#x = (10 + 3) * 2 ** 2
#x = (2 + 3) * 10 - 3 # exercise 4
#print(x)

#MATH FUNCTIONS
#x = 5.7
#print(round(x))
#print(abs(-5.7)) #builtin function absolute you can import math module if you need to perform multiple complex math functions. imported at the top
#print(math.ceil(5.7))
#print(math.floor(5.7)) #google python 3 math module documentation

#IF STATEMENTS... CONDITIONS
#scenario: if its hot its a hot day so drink plenty of water otherwise if its cold its a cold day wear warm clothes otherwise its a lovely day
#is_hot =False
#is_cold = True
#if is_hot:
    #print("it's a hot day")
    #print('drink plenty of water')#the indented prints only print if condition is true
#elif is_cold:
    #print("it.s a cold day")
    #print('wear warm clothes')
#else:
    #print("It's a lovely day") #will be true if both conditions are false

#print('enjoy your day')
#Exercise 5: price of a house 1M, if buyer has a good credit they need to put down 10% otherwise they need to put down 20% of the payment
#how i did it
#is_good_credit = True
#if is_good_credit:
    #print('you need to put down 10 % of the payment')
#else:
   # print('you need to put down 20% of the payment')
#THE SOLUTION
#price = 1000000
#has_good_credit = True
#if has_good_credit:
    #down_payment = 0.1 * price
#else:
    #down_payment = 0.2 * price
#print(f"down payment: ${down_payment}")

#LOGICAL OPERATORS
#has_high_income = True
#has_good_credit = False
#if has_high_income and has_good_credit: #logical AND operator where both conditions must be true
    #print('Eligible for loan')

#has_high_income = True
#has_good_credit = False
#if has_high_income or has_good_credit:  # logical OR operator where only 1  conditions needs to be True
        #print('Eligible for loan')
#has_good_credit = True
#has_criminal_record = True
#if has_good_credit and not has_criminal_record: #using logical NOT operator
    #print('Eligible for loan')

#COMPARISON OPERATORS - used when we want we want to compare a variable with a value
#Scenario: if temp is greater than 30 its a hot day otherwise if its less than 10 its a cold day otherwise its neither hot nor cold
#temperature = 30
#if temperature > 30:
    #print("it's a hot day")
#else:
    #print("it's not a hot day") #evaluates to this coz 30 is not greater than 30
#temperature = 35
#if temperature > 30:
    #print("it's a hot day")
#else:
    #print("it's not a hot day")
#temperature = 10
#if temperature < 10:
    #print("it's a cold day")
#else:
    #print("it's not a cold day")
#temperature = 37  #putting all the conditions in one loop done in this code below
#if temperature > 30:
   # print("it's a hot day")
#elif temperature < 10:
   # print("it's a cold day")
#else:
   # print("It's neither hot or cold")
#exercise 6
#scenario: if name is less than 3 characters long name must be name must be atleast 3 characters long otherwise if its more than 50 chars long name can be a max of 50 chars otherwisse name looks good
#1:14:08 How i did it
#name_character = 14
#if name_character < 50:
   # print('name can only have a max of 50 characters')
#elif name_character < 3:
   # print('name must be atleast 3 characters long')
#else:
    #print('name looks good!')

# solution
# name = "jasss"
# if len(name) < 3:
#     print('Name must be at least 3 characters long')
# elif len(name) > 50:
#     print('name must be a max of 50')
# else:
#     print('name looks good!')
# [[[[ctrl+/ to comment in multiple lines on pycharm]]]]
# PROJECT: WEIGHT CONVERTOR:
# weight = int(input('weight: '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"you are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"you are {converted} pounds")

# WHILE LOOPS - USED TO EXECUTE A BLOCK OF CODE SEVERAL TIMES. while statement followed by conditions
# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i+1
# print('done')
# GUESSING GAME
# secret_num = 7
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_num:
#         print('you won!')
#         break
# else:
#     print('Sorry you failed')

# CAR GAME
# command = ""
# started = "False"
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print('car is already started')
#         else:
#             started = True
#         print('car started...')
#     elif command == "stop":
#         if not started:
#             print('car already stopped')
#         else:
#             started = False
#         print('car stopped.')
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("sorry i don't understand that")
# FOR LOOPS
# for item in 'python':
#     print(item)
# for item in range(10):
#     print(item)
# exercise 7: calcualate total cost of an items in a shopping cart
# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price #total = total + price
# print(f"total: {total}")

# NESTED LOOPS - adding a loop in another loop
# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')
# challenge: drawing an f with  xxxx's'
# numbers = [5, 2, 5, 2, 2]
# for item in numbers:  # print('x' * item)
#     output = ''
#     for count in range(item):
#         output += 'x'
#     !!!!!    print(output) REDO SINCE OUTPUT SUCKS!!!!!

# LISTS
# names = ['John', 'doe', 'becky', 'sarah', 'andrew']
# print(names[-2])
# print(names[2:4])
# print(names[:3])
# print(names[4:])
# print(names)
# exercise 8: program to find the largest number in alist
# numbers = [5, 7, 8, 25, 15, 12, 32]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
#     print(max)
# print(len(numbers))
# 2D LISTS - Each item in a list is another list - matrix list
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
#
# ]
# for row in matrix:
#     for item in row:
#         print(item)

# LISTS METHODS/FUNCTIONS - Operations that can be performed on a list
# numbers = [5, 2, 3, 7, 9]
# numbers2 = numbers.copy()
# numbers.append(10)
# # numbers.sort()
# # numbers.reverse()
# print(numbers2)
# print(numbers.sort()) return none to show absence of a value
# print(numbers.count(5))
# print(50 in numbers)
# print(numbers.index(5))
# numbers.pop() removes the last item in a list
# numbers.clear()
# numbers.remove(5)
# numbers.insert(0, 10)
# numbers.append(20)
# Exercise 9: program to remove the duplicate in a list
# numbers = [5, 2, 9,  3, 5, 7, 9] lists use square brackets
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# TUPLES USED TO STORE A LIST OF ITEM BUT UNLIKE LISTS YOU CANT MODIFY THEM. THEY ARE IMMUTABLE CANT BE CHANGED
# numbers = (1, 2, 3) #only get info about a tuple .index and .count from those 2 methods.
# print(numbers[0])
# print(numbers.count(2))
# coordinates = (1, 2, 3) tuples use curly braces
# x, y, z = coordinates #unpacking
# print(z)

# DICTIONARIES - used to store info that comes as key value pairs eg customer email name phone address etc
# customer = {
#     "name": "John Doe",
#     "age": 52,
#     "is_verified": True
# }
# customer["name"] = "Jahn Doe"
# # print(customer.get("birthdate", "jan 1 1980")) using the get method to pass a none specified value
# print(customer["name"])
#Exercise 10
# input("phone: ")
# # defining the dictionary
# phone = input("phone: ")
# digits_mapping = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
# }
# # looping through the phone string
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "
#     print(output) ...still in the working not outputting correctly
# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": "😊",
#     ":(": "😕😔"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output) the output for this one was fun i love it

# FUNCTIONS - Container for a few lines of codes that perform specific tasks they are small reusable and manageble chunks
# def greet_user(): colon means we are defining a block of code
#     print('Hi there')
#     print('welcome to the team')
#
#
# print("start")
# greet_user() execution happens only if we call the function start from line above
# print("Finish")
# How To Pass Information To the Function
# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard')
# # parameters are placeholders that we define in our func for receiving info
# # arguments the actual pieces info that we supply to the functions
#
#
# print("start")
# greet_user("Becky", "shee")
# greet_user("Pete", "mcguire")
# print("finish")

# RETURN STATEMENTS
# def square(number):
#     return number * number
# print(square(4))
# result = square(4) you can print this way as well
# print(result)

# exercise 11: convert the emoji code above to a function


# def emoji_converter(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": "😊",
#         ":(": "😕😔"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# message = input(">")
# print(emoji_converter(message))

# EXCEPTIONS - error handling in python
# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income/age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0.')
# except ValueError:
#     print('Invalid value')

# CLASSES - blueprint upon which objects are founded
# object is an instance of a class
# Constructors a function that gets called at the time of creating an object
# class Point:
#     def __init__(self, x, y): #the magic method here is a constructor
#         self.x = x #this is how we initialize our objects
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
# point = Point(10, 20)
# point.x = 11
# print(point.x)
# Exercise 11: create a class called person with name attribute and talk methods
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Hi, I am {self.name}")
#
#
# john = Person("John Smith")
# john.talk()
#
# bob = Person("Bob Smith")
# print(bob.talk())

#INHERITANCE - Mechanism for reusing code
# class Mammal:
#     def walk(self):
#         print("walk")
#
# class Cat(Mammal):
#     def be_cute_annoying(self):
#         print("annoyingly cute")
# cat1 = Cat()
# cat1.be_cute_annoying()
#
#
# class Dog(Mammal):
#     def be_loyal(self):
#         print("Loyalty")
# dog1 = Dog()
# dog1.be_loyal()

#MODULES - A file with some code and they help us reuse our code
#import convertors ...from convertors import kg_to_lbs or as shown above...import convertors
# print(convertors.kgs_to_lbs(70))

#exercise 12 find max function takes list and returns max num in the list
# from utils import find_max
# numbers = [10, 2, 6, 2]
# # max = find_max(numbers)
# print(max(numbers)) another way to do it since max is actually a builtin function


# PACKAGES - A container for multiple modules -- directory or folder
# -are basically another way to organize our code
# from package.module import e.g. calc_shipping...from ecommerce.shipping import calc_shipping
# from package import specific module ...from ecommerce import shipping
# calc_shipping()

# GENERATING RANDOM VALUES
# for i in range(3):
#     print(random.randint(10,20))
#     print(random.random())

# members = ['Becky', 'Jane', 'Jack', 'Peter','Peyson','Rayleigh']
# leader = random.choice(members)
# print(leader)
#
# exercise 13: random dice roller with a tuple of 2 random values
# class Dice:
#
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1,6)
#         return first, second
#
#
# dice = Dice()
# print(dice.roll())

# FILES AND DIRECTORIES
# path = Path("ecommerce")
# print(path.exists())
path = Path()
# path = Path("emails")
# print(path.rmdir())
# print(path.mkdir())
# for file in (path.glob('*')):
# for file in (path.glob('*.py')):
#     print(file)