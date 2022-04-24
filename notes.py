# IF/ELSE STATEMENT
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120: 
#   print("You can ride the rollercoaster!")
# else:
#   print("Sorry, you have to grow taller before you can ride")



# ODD OR EVEN EXERCISE
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#   print("This is a even number.")
# else: 
#   print("This is an odd number.")




# NESTED IF/ELSE STATEMENTS
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120: 
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age?"))
#   if age <= 18:
#     print("Please pay $7.")
#   else:
#     print("Please pay $12.")
# else:
#   print("Sorry, you have to grow taller before you can ride")

# if / elif / else
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120: 
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age?"))
#   if age < 12:
#      print("Please pay $5.")
#   elif age <= 18:
#     print("Please pay $7.")
#   else:
#     print("Please pay $12.")
# else:
#   print("Sorry, you have to grow taller before you can ride")



# BMI Calculator
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = round(weight/(height **2))

# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print (f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f" Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")



# ** LEAP YEAR CHECKER EXERCISE
# Write a program that works out whether if a given year is a leap year.
# year = int(input("Which year do you want to check? "))

# if year % 4 == 0 and year % 100 != 0:
#   print("Leap year")
# elif year % 100 == 0 and year % 400 == 0:
#   print("Leap year")
# else:
#   print("Not Leap Year")

# year = int(input("Which year do you want to check? "))
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year")


# MULTIPLE IF STATEMENTS IN SUCCESSION
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120: 
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age?"))
#   if age < 12:
#      bill = 5 
#      print("Child tickets are $5.")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7.")
#   else:
#     bill = 12
#     print("Adult tickets are $12.")

#   wants_photo = input("Do you want a photo taken? Y or N.")
#   if wants_photo == "Y":
#     bill += 3
#   print(f"Your final bill is ${bill}")
# else:
#   print("Sorry, you have to grow taller before you can ride")


# PIZZA ORDER EXERCISE
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0

# if size == "S" :
#   bill = 15
#   if add_pepperoni == "Y":
#     bill += 2
# elif size == "M":
#   bill = 20
#   if add_pepperoni == "Y":
#     bill += 3
# elif size == "L":
#   bill = 25
#   if add_pepperoni == "Y":
#     bill += 3
# if extra_cheese == "Y":
#   bill += 1
# print(f"Your final bill is: ${bill}")

# if size == "S" :
#   bill += 15
# elif size == "M":
#   bill += 20
# elif size == "L":
#   bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3

# if extra_cheese == "Y":
#   bill += 1

# print(f"Your final bill is: ${bill}")



# LOGICAL OPERATORS (AND, OR, NOT)
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120: 
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age?"))
#   if age < 12:
#      bill = 5 
#      print("Child tickets are $5.")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7.")
#   elif age >= 45 and age <= 55:
#     print("Everything is going to be ok. Have a free ride on us!")
#   else:
#     bill = 12
#     print("Adult tickets are $12.")

#   wants_photo = input("Do you want a photo taken? Y or N.")
#   if wants_photo == "Y":
#     bill += 3
#   print(f"Your final bill is ${bill}")
# else:
#   print("Sorry, you have to grow taller before you can ride")

# ** LOVE CALCULATOR EXERCISE
#  Write a program that tests the compatibility between two people.
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Combine the names
name3 = (name1 + name2).lower()
# Find Number of times the letters in the word TRUE occurs
count_true = name3.count("t") + name3.count("r") + name3.count("u") + name3.count("e")
# Check for the number of times the letters in the word LOVE occurs
count_love = name3.count("l") + name3.count("o") + name3.count("v") + name3.count("e")
# Combine those numbers to make a 2 digit number
score = int(str(count_true) + str(count_love))

if score <= 10 or score >= 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")