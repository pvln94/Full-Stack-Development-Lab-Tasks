class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero!"

def get_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Invalid input! Numbers must be numeric.")
        return None, None

def main():
    calc = Calculator()
    while True:
        print("\nCalculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '5':
            print("Exiting...")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please try again.")
            continue
        
        a, b = get_numbers()
        if a is None or b is None:
            continue
        
        if choice == '1':
            result = calc.add(a, b)
        elif choice == '2':
            result = calc.subtract(a, b)
        elif choice == '3':
            result = calc.multiply(a, b)
        elif choice == '4':
            result = calc.divide(a, b)
        
        print(f"Result: {result}")

if __name__ == "__main__":
    main()