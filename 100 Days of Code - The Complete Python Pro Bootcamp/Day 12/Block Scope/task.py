# def is_prime(num):
#     if num == 1 or num == 0:
#         return False
#     if num == 2:
#         return True
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
#
# num = int(input())
# print(is_prime(num))

a = 1
def func(b):
    global a
    a += a
    print(a)
func(a)
print(a)