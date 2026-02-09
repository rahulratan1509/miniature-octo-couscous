def calculator(a, b, operation):
    """
    Simple calculator function.
    
    Args:
        a: First number
        b: Second number
        operation: Operation as string ('+', '-', '*', '/', '//', '%', '**')
    
    Returns:
        Result of the operation
    """
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b if b != 0 else "Error: Division by zero"
    elif operation == '//':
        return a // b if b != 0 else "Error: Division by zero"
    elif operation == '%':
        return a % b if b != 0 else "Error: Division by zero"
    elif operation == '**':
        return a ** b
    else:
        return "Error: Invalid operation"


# Example usage
if __name__ == "__main__":
    print(calculator(10, 5, '+'))   # 15
    print(calculator(10, 5, '-'))   # 5
    print(calculator(10, 5, '*'))   # 50
    print(calculator(10, 5, '/'))   # 2.0