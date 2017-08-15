# ORIGINAL CHALLENGE

# n = 150
# print("Fizz buzz counting up to {0}".format(n))
# i = 1
# while i <= n:
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
#     i += 1
    
    
# EXTRA CHALLENGE

import sys

try:
    n = int(input("Enter a positive integer: "))
except ValueError:
    n = int(input("That was not an integer! Try again: "))

while n <= 0:
    n = int(input("That's not positive! Try again: "))
print("Fizz buzz counting up to {0}".format(n))

i = 1
while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1