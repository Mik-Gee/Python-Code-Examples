import random

password_length = int(input("How many characters in the password?: "))
password_data = "1234567890-=!@#$%^&*()_+qwertyuiop[]\{}|asdfghjkl;':zxcvbnm,./<>?QWERTYUIOPASDFGHJKLZXCVBNM"

password = ''.join(random.sample(password_data,password_length))

print(password)