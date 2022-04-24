# if...else Statement
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120: 
#   print("You can ride the rollercoaster!")
# else:
#   print("Sorry, you have to grow taller before you can ride")


# Odd or Even Exercise
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#   print("This is a even number.")
# else: 
#   print("This is an odd number.")

# Nested if/else
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

# Leap Year Checker
# Write a program that works out whether if a given year is a leap year.
year = int(input("Which year do you want to check? "))

if year % 4 == 0 and year % 100 != 0:
  print("Leap year")
elif year % 100 == 0 and year % 400 == 0:
  print("Leap year")
else:
  print("Not Leap Year")