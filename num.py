import sys

def main():
    
    num1 = 20
    num2 = 10

    
    if len(sys.argv) == 3:
        try:
            
            num1 = int(sys.argv[1])
            num2 = int(sys.argv[2])
            print("User provided inputs:", num1, num2)
        except ValueError:
            print("Invalid input: Please provide two integer values.")
            return
    else:
        print("Using default values:", num1, num2)

    
    if num2 == 0:
        print(f"Cannot divide by zero (num2 = {num2}).")
        return

    if num1 % num2 == 0:
        print(f"'{num1}' is divisible by '{num2}'")
    else:
        print(f"'{num1}' is not divisible by '{num2}'")


