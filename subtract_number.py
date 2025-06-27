import sys

def subtract(num1, num2):
    try:
        result = float(num1) - float(num2)
        print(f"The difference between {num1} and {num2} is {result}.")
    except ValueError:
        print("Error: Please provide valid numeric arguments.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python subtract_number.py <num1> <num2>")
        sys.exit(1)
    subtract(sys.argv[1], sys.argv[2])