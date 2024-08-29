def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

def main():
    while True:
        print("Please select operation -\n" \
              "1. Add\n" \
              "2. Subtract\n" \
              "3. Multiply\n" \
              "4. Divide\n" \
              "5. Exit\n")

        try:
            select = int(input("Select operation (1, 2, 3, 4, or 5): "))

            if select == 5:
                print("Exiting the program.")
                break

            if select in [1, 2, 3, 4]:
                number_1 = float(input("Enter first number: "))
                number_2 = float(input("Enter second number: "))

                if select == 1:
                    result = add(number_1, number_2)
                    print(f"{number_1} + {number_2} = {result}")

                elif select == 2:
                    result = subtract(number_1, number_2)
                    print(f"{number_1} - {number_2} = {result}")

                elif select == 3:
                    result = multiply(number_1, number_2)
                    print(f"{number_1} * {number_2} = {result}")

                elif select == 4:
                    result = divide(number_1, number_2)
                    print(f"{number_1} / {number_2} = {result}")

            else:
                print("Invalid input. Please select a valid operation.")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()