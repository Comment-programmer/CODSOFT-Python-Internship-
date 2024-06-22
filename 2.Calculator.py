# TASK-2-Calculator

'''
Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result 
'''

# Define the calculator function
def calculator():
    # Prompt for the user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Display the operation choices
    print("Choose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Prompt the user to choose an operation
    operation = input("Enter the number corresponding to the operation: ")
    
    # Perform the calculation based on the chosen operation
    if operation == '1':
        result = num1 + num2
        operation_sign = '+'
    elif operation == '2':
        result = num1 - num2
        operation_sign = '-'
    elif operation == '3':
        result = num1 * num2
        operation_sign = '*'
    elif operation == '4':
        # Handle division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        operation_sign = '/'
    else:
        print("Invalid operation choice.")
        return
    
    # Display the result
    print(f"The result of {num1} {operation_sign} {num2} is: {result}")

# Run the calculator
calculator()
