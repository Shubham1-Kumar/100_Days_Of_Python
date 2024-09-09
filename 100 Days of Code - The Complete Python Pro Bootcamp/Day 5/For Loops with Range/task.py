# Range Function with for loop
# sum = 0
# for number in range(1,101):
#     sum += number
# print(sum)
#
# for number in range(1,11,3):
#     print(number)

for number in range(1,101):
    if number%15 == 0:
        print("FizzBuzz")
    elif number%5 == 0:
        print("Buzz")
    elif number%3 ==0:
        print("Fizz")
    else:
        print(number)