a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
if b != 0:
    print("Division:", a / b)
    print("Remainder:", a % b)
else:
    print("Cannot divide by zero")
    
print("power:", a ** b)
print("First number is greater:", a > b)
print("Both numbers are equal:", a == b)
