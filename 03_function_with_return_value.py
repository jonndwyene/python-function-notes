# Difficulty: Easy
# Topic: Function with return value

# "return" sends a value back to the code that called the function
def square(number):
    return number * number


# Store the returned value in a variable
result = square(5)
print("5 squared is", result)

# The returned value can also be used directly
print("9 squared is", square(9))
