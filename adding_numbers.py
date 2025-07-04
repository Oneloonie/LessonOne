import sys

def add_numbers(num1, num2):
    try:
        result = float(num1) + float(num2)
        print(f"The sum of {num1} and {num2} is {result}.")
    except ValueError:
        print("Error: Please provide valid numeric arguments.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python adding_numbers.py <num1> <num2>")
        sys.exit(1)
    add_numbers(sys.argv[1], sys.argv[2])
