def my_function():
    print("Function is running!")
    print(f"This script has been imported. Its name is: {__name__}")

# The interpreter checks if this file is the 'main' program
if __name__ == "__main__":
    print("This script is being run directly!")
    my_function()