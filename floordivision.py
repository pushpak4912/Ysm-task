# Program to perform floor division and modulo operations


num1 = int(input("Enter the first number (dividend): "))
num2 = int(input("Enter the second number (divisor): "))

if num2 != 0:
    
    floor_div = num1 // num2
    remainder = num1 % num2

    print(f"Floor division result ({num1} // {num2}) = {floor_div}")
    print(f"Modulo result ({num1} % {num2}) = {remainder}")
else:
    print("Error: Division by zero is not allowed.")
