def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That is not a valid number. Try again.")


def main():
    while True:
        print("\nCalculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        operation = input("Choose an option (1-5): ")

        if operation == "5":
            print("Goodbye!")
            break
        if operation not in ("1", "2", "3", "4"):
            print("\nOption not available. Try again.")
            continue

        first_number = read_number("Enter the first number: ")
        second_number = read_number("Enter the second number: ")

        if operation == "1":
            result = add(first_number, second_number)
        elif operation == "2":
            result = subtract(first_number, second_number)
        elif operation == "3":
            result = multiply(first_number, second_number)
        else:
            while second_number == 0:
                second_number = read_number("Enter a non-zero second number: ")
            result = divide(first_number, second_number)

        print("Result:", result)


if __name__ == "__main__":
    main()
    