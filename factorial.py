def factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        return "Error: Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result 


if __name__ == "__main__":
    # Test the factorial function
    test_numbers = [0, 1, 5, 10, 15]
    
    for num in test_numbers:
        result = factorial(num)
        print(f"Factorial of {num} is: {result}")
    
    # Interactive input
    print("\n--- Calculate Factorial ---")
    try:
        user_input = int(input("Enter a number to calculate factorial: "))
        print(f"Factorial of {user_input} is: {factorial(user_input)}")
    except ValueError:
        print("Please enter a valid integer.")
