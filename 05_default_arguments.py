# Difficulty: Intermediate
# Topic: Default arguments

# A parameter with "=" has a default value, used if no argument is given
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet("Alice")            # Uses the default greeting
greet("Bob", "Good day")  # Overrides the default


# Default parameters must come after non-default ones
def power(base, exponent=2):
    return base ** exponent


print(power(5))     # 25 (default exponent of 2)
print(power(2, 5))  # 32
