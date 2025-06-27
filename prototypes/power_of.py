import sys
def power_of_numbers(num1, num2):
    try:
        result = float(num1) ** float(num2)
        print(f"{num1} raised to the power of {num2} is {result}.")
    except ValueError:
        print("Error: Please provide valid numeric arguments.")