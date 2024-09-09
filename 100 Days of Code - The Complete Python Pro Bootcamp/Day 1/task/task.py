# Write your code below this line 👇
# print("Hello World!")
# print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
# print(" 2. Knead the dough for 10 minutes.")
# print("3. Add 3g of Salt.")
# print("4. Leave to rise for 2 hours.")
# print("5. Bake at 200 degrees C for 30 minutes.")

#Input function
# print("Hello " + input("What is your name ?"+" !")

# # Variables
# name = "Shubham"
# print(name)
# name = "Kumar"
# print(name)
#
# # length of a string
# print(len(name))
#
# test_input = input("Enter any string :-")
# print(len(test_input))
# _Shubham = 5
# print(_Shubham)

# # Band name Generator
# Pat_name = input("Enter your pat's name :-")
# City_name = input("Enter you city name :-")
#
# print(City_name+Pat_name)

# # Subscripting
# print("Hello"[-1])
# # Type checking
# print(type(45))

# # Type Conversion
# print(int("123")+ int("234"))
# print(bool(34))
# print("Number of letters in your name:" + str(len(input("Enter your name"))))

# # F-string
# age = 20
# print(f"My age is = {age}.")

# Tip Calculator
print("Welcome to tip calculator\n")
Total_bil = int(input("What was the  total bil :- "))
tip_percentage = int(input("How much tip would you like to give 10, 12, or 15? "))
Number_of_people = int(input("How many people to split the bill? "))

tip_each_person = round((Total_bil + Total_bil*(tip_percentage/100))/Number_of_people , 2)
print(f"Each person should pay: ${tip_each_person}")





