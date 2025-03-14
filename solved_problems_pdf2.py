n = 5

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
