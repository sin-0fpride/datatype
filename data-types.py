# TUPLES (Immutable)
print("=== Tuple Example ===")
coordinates = (10, 20)
print("X:", coordinates[0])
print("Y:", coordinates[1])
# coordinates[0] = 30  # Uncommenting this will raise an error

print()

#  LISTS (Mutable)
print("=== List Example ===")
fruits = ['apple', 'banana', 'cherry']
print("Original:", fruits)

fruits.append('orange')
fruits[1] = 'blueberry'
fruits.remove('apple')

print("Modified:", fruits)

print()

# RANGES (Immutable sequence generator)
print("=== Range Example ===")
for i in range(5):
    print(i)

numbers = list(range(3, 10, 2))
print("Odd numbers from 3 to 9:", numbers)

print()

# MUTABILITY vs IMMUTABILITY
print("=== Mutability Demo ===")
a = [1, 2, 3]
b = a
b.append(4)
print("a after modifying b:", a)  # a is also changed

x = (1, 2, 3)
y = x
y += (4,)  # This creates a new tuple
print("x:", x)
print("y:", y)