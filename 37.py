a = [10, 25, 7, 40, 15]

largest = a[0]
smallest = a[0]

for i in a:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

diff = largest - smallest

print("Largest:", largest)
print("Smallest:", smallest)
print("Difference:", diff)