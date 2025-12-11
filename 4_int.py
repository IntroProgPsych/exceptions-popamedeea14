# Exercise 4: Validating input within a numeric range using try / except / finally
# --------------------------------------------------------------------------------------
# Write a function named read_input which:
# - repeatedly asks the user for input using the given prompt
# - attempts to convert the input to an integer
# - checks whether the number falls between the given lower and upper bounds
# - if the input is not an integer, prints an error message
# - if the number is outside the allowed range, prints an error message
# - only returns when the user enters a valid integer within the required range
# - always prints a message in the finally block for each attempt
# 

# Sample Input:
# Please type in a number: seven
# Please type in a number: -3
# Please type in a number: 8
#
# Sample Output:
# You must type a valid integer!
# Attempt processed.
# The number must be between 5 and 10.
# Attempt processed.
# Attempt processed.
# You typed in: 8

prompt = "Please type in a number: "
lower = 5
upper = 10
def read_input(prompt, lower, upper):
    while True:
        try:
            value = int(input(prompt))
            
            if value < lower or value > upper:
                print(f"The number must be between {lower} and {upper}.")
            else:
                return value

        except ValueError:
            print("You must type a valid integer!")
        
        finally:
            print("Attempt processed.")

result = read_input("Please type in a number: ", 5, 10)
print(f"You typed in: {result}")