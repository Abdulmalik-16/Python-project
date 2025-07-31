def calculator():
    print("Welcome to the Python Calculator!")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        # Take input from the user
        choice = input("Enter the number of the operation you'd like to perform (1/2/3/4): ")
        
        # Check if the choice is valid
        if choice in ['1', '2', '3', '4']:
            try:
                # Get numbers from the user
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                # Perform the operation
                if choice == '1':
                    print(f"The result of {num1} + {num2} is {num1 + num2}")
                elif choice == '2':
                    print(f"The result of {num1} - {num2} is {num1 - num2}")
                elif choice == '3':
                    print(f"The result of {num1} * {num2} is {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"The result of {num1} / {num2} is {num1 / num2}")
                    else:
                        print("Error: Division by zero is not allowed.")
            
            except ValueError:
                print("Error: Invalid input. Please enter numeric values.")
        else:
            print("Invalid choice. Please select a valid operation.")
        
        # Check if the user wants to continue
        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calculation != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

# Run the calculator
calculator()
