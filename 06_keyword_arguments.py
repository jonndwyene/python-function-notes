# Difficulty: Intermediate
# Topic: Keyword arguments

def describe_pet(name, animal, age):
    print(f"{name} is a {age}-year-old {animal}.")


# Keyword arguments name the parameter, so order doesn't matter
describe_pet(name="Buddy", animal="dog", age=3)
describe_pet(age=2, name="Whiskers", animal="cat")

# Positional and keyword arguments can be mixed
# (positional ones must come first)
describe_pet("Goldie", animal="fish", age=1)
