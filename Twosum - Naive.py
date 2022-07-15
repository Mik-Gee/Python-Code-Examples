# From an unsorted list and number, find all pairs of numbers in the list that their sum equals a number

def twosum(num,array):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i] + num[j] == array:
                print(f"Pairs with sum {array} is ({num[i]}, {num[j]})")

num = [4,5,1,8]
array = 9

twosum(num,array)