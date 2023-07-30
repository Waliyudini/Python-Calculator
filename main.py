def add(x, y):
        return x + y

        def subtract(x, y):
            return x - y

            def multiply(x, y):
                return x * y

                def divide(x, y):
                    if y != 0:
                            return x / y
                                else:
                                        return "Cannot divide by zero!"

                                        def calculator():
                                            print("Welcome to the Python Calculator!")
                                                print("Available operations: +, -, *, /")

                                                    while True:
                                                            num1 = float(input("Enter the first number: "))
                                                                    operator = input("Enter an operation (+, -, *, /) or 'q' to quit: ")

                                                                            if operator == 'q':
                                                                                        print("Goodbye!")
                                                                                                    break

                                                                                                            if operator not in ['+', '-', '*', '/']:
                                                                                                                        print("Invalid operator. Please try again.")
                                                                                                                                    continue

                                                                                                                                            num2 = float(input("Enter the second number: "))

                                                                                                                                                    if operator == '+':
                                                                                                                                                                result = add(num1, num2)
                                                                                                                                                                        elif operator == '-':
                                                                                                                                                                                    result = subtract(num1, num2)
                                                                                                                                                                                            elif operator == '*':
                                                                                                                                                                                                        result = multiply(num1, num2)
                                                                                                                                                                                                                elif operator == '/':
                                                                                                                                                                                                                            result = divide(num1, num2)

                                                                                                                                                                                                                                    print(f"Result: {result}\n")

                                                                                                                                                                                                                                    if __name__ == "__main__":
                                                                                                                                                                                                                                        calculator()
                                                                                                                                                                                                                                        