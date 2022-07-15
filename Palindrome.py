def palindrome(x):
    return x == x[::-1]

x = "Palindrome"

if palindrome(x):
    print("True")
else:
    print("False")