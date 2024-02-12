num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
operator = input('Enter the operator (+, -, *, /): ')

if operator == '+':
    res = num1 + num2
    print(num1, "+", num2, "=", res)
elif operator == '-':
    res = num1 - num2
    print(num1, "-", num2, "=", res)
elif operator == '*':
    res = num1 * num2
    print(num1, "*", num2, "=", res)
elif operator == '/':
    res = num1 / num2
    print(num1, "/", num2, "=", res)
else:
    print("operator is not valid")        

