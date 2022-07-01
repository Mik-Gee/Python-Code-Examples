user_input = input("Enter a phrase: ")

phrase = (user_input.replace('of','')).split()

a=''

for word in phrase:
    a = a + word[0]
    
print(f'The acronym of {user_input} is {a}')