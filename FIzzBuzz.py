# FizzBuzz: Print numbers from 1 to 100.
# Print "Fizz" for multiples of 3, 
# "Buzz" for multiples of 5,
#  and "FizzBuzz" for multiples of both.
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")