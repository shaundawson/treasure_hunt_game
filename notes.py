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
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120: 
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride")
  