import sys
def multiply_numbers(num1, num2):
    try:
        result = float(num1) * float(num2)
        print(f"The product of {num1} and {num2} is {result}.")
    except ValueError:
        print("Error: Please provide valid numeric arguments.") 
if __name__ == "__main__":
    # Check if the correct number of command line arguments are provided

    if len(sys.argv) != 3:
        print("Usage: python multiplying_numbers.py <num1> <num2>")
        sys.exit(1)
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    result = multiply_numbers(sys.argv[1], sys.argv[2])  