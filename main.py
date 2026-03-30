def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter an operation you want to perform: ")

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
