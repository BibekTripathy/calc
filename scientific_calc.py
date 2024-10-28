import math

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
        return "Error! Division by zero."

def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def logarithm(x, base):
    if x > 0:
        return math.log(x, base)
    else:
        return "Error! Logarithm of non-positive number."

def main():
    print("Welcome to the Scientific Calculator!")
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square Root")
        print("6. Power")
        print("7. Sine")
        print("8. Cosine")
        print("9. Logarithm")

        choice = input("Enter choice (1-9): ")

        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if choice in ['1', '2', '3', '4', '6']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                elif choice == '6':
                    print(f"{num1} ^ {num2} = {power(num1, num2)}")

            elif choice == '5':
                num = float(input("Enter number: "))
                print(f"Square root of {num} = {square_root(num)}")

            elif choice in ['7', '8']:
                angle = float(input("Enter angle in degrees: "))
                if choice == '7':
                    print(f"Sine of {angle}° = {sine(angle)}")
                elif choice == '8':
                    print(f"Cosine of {angle}° = {cosine(angle)}")

            elif choice == '9':
                num = float(input("Enter number: "))
                base = float(input("Enter base (default is e): ") or 'e')
                print(f"Logarithm of {num} base {base} = {logarithm(num, base)}")

            else:
                print("Invalid input")
        
        else:
            print("Invalid choice, please choose a number between 1-9.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
