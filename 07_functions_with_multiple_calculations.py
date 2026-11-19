# Difficulty: Hard
# Topic: Functions with multiple calculations

# A function can perform several calculations and return several values
def circle_stats(radius):
    pi = 3.14159
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    diameter = 2 * radius
    return diameter, circumference, area  # Returns a tuple


# Unpack the returned values into separate variables
diameter, circumference, area = circle_stats(5)
print(f"Diameter:      {diameter}")
print(f"Circumference: {circumference:.2f}")
print(f"Area:          {area:.2f}")


# Another example: statistics for a list of numbers
def number_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average, min(numbers), max(numbers)


total, average, smallest, largest = number_stats([4, 8, 15, 16, 23, 42])
print(f"\nTotal: {total}, Average: {average:.2f}, "
      f"Min: {smallest}, Max: {largest}")
