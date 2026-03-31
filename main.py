def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

# check if input are numbers
def is_number(a):
    try:
        float(a)
        return True
    except ValueError:
        return False
     
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
op = input("Enter an operation you want to perform: ")

try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError: 
    print('Invalid number')
    exit()



if(num2 == 0 and op == '/'):
    print("It is illegal to divide by 0")
    exit()



if(op == '+'):
    result = add(num1, num2)

elif(op == '-'):
    result = sub(num1, num2)

elif(op == '*'):
    result = mul(num1, num2)

elif(op == '/'):
    result = div(num1, num2)

# print the result
print("The result is: ", result)
