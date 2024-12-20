import itertools

# Example 1: Prefer a generator expression to a list comprehension for simple iterations
# Generator expression
squares_generator = (x**2 for x in range(10))  # Creates a generator
print(squares_generator)  # Output: <generator object <genexpr> at 0x...>

# Iterate over the generator (values are generated as needed)
for square in squares_generator:
    print(square)  # Output: 0 1 4 9 16 25 36 49 64 81

# Example with large dataset.
large_generator = (
    x**2 for x in range(10000000000)
)  # Will not create a list of 10 billion elements in memory
# print(len(large_generator)) # Not available for generator
for i, square in enumerate(large_generator):
    if i > 10:
        break
    print(square)
# Example 2: Use a generator to lazily load infinite sequences

# Infinite sequence of even numbers
even_numbers = (x * 2 for x in itertools.count())

# Get the first 10 even numbers
for _ in range(10):
    print(next(even_numbers), end=" ")  # Output: 0 2 4 6 8 10 12 14 16 18
print()
