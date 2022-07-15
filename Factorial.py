def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = int(input("Enter a Number: "))

result = factorial(num)

print(f"The factorial of {num} is {result}")