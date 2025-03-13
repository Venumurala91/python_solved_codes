print("Increasing pattern:")
for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()

print("Decresing pattern:")
for i in range(5):
    for j in range(5 - i):
        print("*", end=" ")
    print()

