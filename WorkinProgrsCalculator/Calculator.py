# This program performs basic arithmetic operations by Nathanael Theseira
# Reason for this code is to practice using Python

#Calculations of the users choice
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# While true is to loop back here infinitly until the user chooses choice 5(line 30)
while True:
    print("===================")
    print("Select operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    print("===================")

    choice = input("Enter choice (1/2/3/4/5): ")

# Choice 5 is to stop the loop when the condition is met which is the input of int 5
    if choice == '5':
        print("Exiting the program.")
        break

# Num1 and Num2 are defined variables( a container that holds a value)
# The input() function takes the user’s input as a string.
# float() converts that string into a floating-point number,
# (a number that can have decimals) and stores it in the variable
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

# Choice 4 is placing conditions that neither num1 or num2 is equal to 0
# If one of them are or both, the following print will show
        if choice == '4':
            if num1 == 0 and num2 == 0:
                print("Both numbers cannot be zero for division. Please enter non-zero numbers.")
            elif num1 == 0:
                print("Cannot divide zero. Please enter a non-zero first number.")
            elif num2 == 0:
                print("Cannot divide by zero. Please enter a non-zero second number.")
            else:
                print(num1, "/", num2, "=", divide(num1, num2))
# Choice 1-3 is already calculated from line 4
# the print is just displaying the num1 and num2
# e.g add(num, num2)) is taking the result from above to the print statement
        else:
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

# If all choices 1-5 are not selected. Then any other input will result as invalid
    else:
        print("Invalid input. Please choose a number between 1 and 5.")

# This allows the user to continue after getting their result
# If not the user can put any other input string besides the word "yes" and the program will terminate
# (whether is upper or lower case e.g "yes","YES","Yes","yEs"(.lower which returns the input to lower case by default)
    continue_choice = input("Do you want to perform another calculation? (yes/no): ").lower()
    if continue_choice != 'yes':
        print("Exiting the program.")
        break