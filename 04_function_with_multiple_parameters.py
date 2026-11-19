# Difficulty: Easy
# Topic: Function with multiple parameters

# Separate parameters with commas
def add(a, b):
    return a + b


def introduce(name, age):
    return f"{name} is {age} years old."


# Arguments are matched to parameters by position
print(add(3, 4))
print(introduce("Maria", 25))
