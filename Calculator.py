def add(x,y):
    return(x + y)
def subtract(x,y):
    return(x - y)
def multiply(x,y):
    return(x * y)
def divide(x,y):
    return(x / y)
    
print("Select Operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    user_input = input("Enter a Choice (1,2,3,4): ")
    if user_input in ('1','2','3','4'):
        num1=float(input("Enter Number 1: "))
        num2=float(input("Enter Number 2: "))
        
        if user_input == '1':
            print(num1,'+',num2,'=',add(num1,num2))
            
        elif user_input == '2':
            print(num1,'-',num2,'=',subtract(num1,num2))
                
        elif user_input == '3':
            print(num1,'*',num2,'=',multiply(num1,num2))
                
        elif user_input == '4':
            print(num1,'/',num2,'=',divide(num1,num2))
            
        another_calculation = input("Let's enter another calculation? (Yes/No): ")
        if another_calculation == "No":
            break
        
    else:
        print("Invalid Input")
                    