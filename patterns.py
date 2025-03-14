'''n = 5

# First half of the butterfly
for i in range(n): 
    for j in range(i + 1):
        print("*", end="")
    
    for j in range(i, n - 1):
        print(" ", end="")
    
    for j in range(i, n - 1):
        print(" ", end="")
    
    for j in range(i + 1):
        print("*", end="")
    
    print()

# Second half of the butterfly
for i in range(n): 
    for j in range(i, n - 1):
        print("*", end=" ")
    
    for j in range(i + 1):
        print(" ", end="")
    
    for j in range(i + 1):
        print(" ", end=" ")
    
    for j in range(i, n - 1):
        print("*", end=" ")
    
    print()




n = 5  # You can change n to any other number for a larger or smaller butterfly

# First half of the butterfly
for i in range(n):
    # Print the first set of stars
    for j in range(i + 1):
        print("*", end="")
    
    # Print spaces
    for j in range(2 * (n - i - 1)):
        print(" ", end="")
    
    # Print the second set of stars
    for j in range(i + 1):
        print("*", end="")
    
    # Move to the next line
    print()

# Second half of the butterfly (reverse)
for i in range(n - 1):
    # Print the first set of stars
    for j in range(n - i - 1):
        print("*", end="")
    
    # Print spaces
    for j in range(2 * (i + 1)):
        print(" ", end="")
    
    # Print the second set of stars
    for j in range(n - i - 1):
        print("*", end="")
    
    # Move to the next line
    print()

'''



char=97

for i in range(5):
    for j in range(i+1):
        print(chr(char),end=" ")
    
    char+=1
    
    print()



