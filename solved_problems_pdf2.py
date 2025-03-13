# Increasing pattern
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


    




'''
def decor_result(result_function):
    # This is the decorator function
    def distinction(marks):
        results = []  # List to store results for each mark
        for m in marks:
            if m >= 75:
                print("DISTINCTION")
            result = result_function([m])  # Call the decorated function
            results.append(result)  # Store the result
        return results  # Return the collected results
    return distinction  # Return the decorated function

@decor_result
def result(marks):
    # This function checks if marks are greater than or equal to 33
    for m in marks:
        if m >= 33:
            pass
        else:
            print("FAIL")
            return "FAIL"  # Return "FAIL" if any mark is less than 33
    return "PASS"  # Return "PASS" if all marks are 33 or more

# Example usage
marks = [80, 50, 20, 90, 34]
result(marks)
'''




''
'''
What are iterators in python 


An iterable is any Python objects that can be looped over or iterated .it can be tupe,string, and a collection (set,dictionary)

l1=[23,65,1,23,45,55,89]
it = iter(l1)
while True:
	try:
		print(next(it))
	except StopIteration:
		break
	
'''''''''

