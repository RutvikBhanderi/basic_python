def calculate(num1,num2,math_opratore):
    if math_opratore == '+':
        return num1 + num2
    elif math_opratore == '-':
        return num1 - num2
    elif math_opratore == '*':
        return num1 * num2
    elif math_opratore == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid oprator"

result = calculate(100,25, '/')
print("result:", result)
