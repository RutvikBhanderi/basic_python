class Calculator:
    def additon(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

calculator = Calculator()

print(calculator.additon(10, 5))       
print(calculator.subtract(10, 5))  
print(calculator.multiply(10, 5)) 
print(calculator.divide(10, 5))   
print(calculator.divide(10, 0))    