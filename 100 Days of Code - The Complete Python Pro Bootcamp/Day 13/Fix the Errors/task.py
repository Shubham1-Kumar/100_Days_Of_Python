try:
   age = int(input("How old are you?"))

except ValueError:
    print("Enter a valid number")
    age = int(input("How old are you?"))
if age > 18:
 print("You can drive at age" , age)
