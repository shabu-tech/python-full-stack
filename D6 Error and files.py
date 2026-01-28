#Handling errors with try/except We use try to test a block of code
try:
    x = 10 / 0  
except ZeroDivisionError:
    print("Cannot divide by zero!")
#division example
try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    result = x / y
    print(f"The result is {result}")
except ValueError:
    print("Please enter a valid number")

#File reading example
try:
    filename = input("Enter filename to read: ")
    with open(filename, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("File not found! Check the filename.")
#age calculation
try:
    name = input("Enter your name: ")
    year_born = int(input("Year you were born: "))  # convert input to integer
    current_year = 2026
    age = current_year - year_born
    print(f"You are {name}, and your age is {age}.")
except ValueError:
    print("Please enter a valid number for year!")
#multiple operation
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Addition:", x + y)
    print("Division:", x / y)
except ValueError:
    print("You must enter a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

