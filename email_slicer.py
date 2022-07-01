email = input("What is your email address?: ")

username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f'Your USERNAME is {username} and DOMAIN is {domain}')