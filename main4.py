def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero."
        return num1 / num2
    else:
        return "Invalid operator."

def main():
    print("=== Simple Calculator ===")

    while True:
        try:
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        print("\nSelect operation:")
        print(" + for Addition")
        print(" - for Subtraction")
        print(" * for Multiplication")
        print(" / for Division")

        operator = input("Enter your choice: ")

        result = calculate(num1, num2, operator)
        print("Result:", result)

        again = input("\nDo you want to calculate again? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for using the calculator!")
            break

main()

