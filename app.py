'''import random
print(f"Random number: {random.randint(1, 100)}")
'''
'''
import calendar


year = int(input("Enter year: "))
month = int(input("Enter month: "))
cal = calendar.month(year, month)
print(cal)


'''


# import math
# print(math.sqrt(50))
'''
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
'''



'''year = int(input("Enter a year: "))
 # divided by 100 means century year (ending with 00)
 # century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))
    

'''

'''
num = int(input("Display multiplication table of: "))
for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")
    
    '''
'''a = 0
b = 1
n = 10  # Number of Fibonacci terms you want to print

for i in range(n):
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp


'''

'''n=153

l=len(str(n))
print(l)
c=0
d=0
b=n
while c<=l:
    a=b%10
    d+=a**3
    b//=10
    c+=1
    
    
print(d)

    '''


# ASCII code - American standard code for information interchange 


'''str = "geeksforgeeks"
l = 102
r = 111


c=[]

for i in str:
    check_range=ord(i)
    if l <= check_range <= r: 
        c.append(i)
        

print(c)
        '''



# 0 1 1 2 3 5


# Recursion : Fucntion calls itself is known as recursion 

'''def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
 nterms = int(input("Enter the number of terms (greater than 0): "))
 # check if the number of terms is valid
 if nterms <= 0:
    print("Plese enter a positive integer")
 else:
    print("Fibonacci sequence:")
 for i in range(nterms):
    print(recur_fibo(i)
'''
'''

def add_matrices(mat1, mat2):
    # Check if the matrices have the same dimensions
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Matrices must have the same dimensions for addition"
        
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result
 # Input matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
 ]
 # Call the add_matrices function
result_matrix = add_matrices(matrix1, matrix2)
 # Display the result
if isinstance(result_matrix, str):
    print(result_matrix)
    print("True")
else:
    print("Sum of matrices:")
for row in result_matrix:
    print(row)

'''

'''
def multiply_matrices(mat1, mat2):
    # Determine the dimensions of the input matrices
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    rows2 = len(mat2)
    cols2 = len(mat2[0])

    # Check if multiplication is possible
    if cols1 != rows2:
        return "Matrix multiplication is not possible. Number of columns in mat1 must be equal to the number of rows in mat2."

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
 
    # result = []
    # for i in range(rows1):
    #     row = []
    #     for j in range(cols2):
    #         row.append(0)
    #     result.append(row)
    

    
    print(result)

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]
                print(result)

    return result


# Example matrices
matrix1 = [[1, 2, 3],
           [4, 5, 6]]
matrix2 = [[7, 8],
           [9, 10],
           [11, 12]]

# Multiply the matrices
result_matrix = multiply_matrices(matrix1, matrix2)

# Display the result
if isinstance(result_matrix, str):
    print(result_matrix)
else:
    print("Result of matrix multiplication:")
    for row in result_matrix:
        print(row)


'''



'''a="Hello!!!, he said ---and went"
# p=list(a.split(","))
# print(p)


c=[]
d=''
for i in a:
    if i.isalpha():
        d+=i
    elif d!='':
        c.append(d)
        d=''
    else:
        continue
c.append(d)
    
        
print(c)'''



'''

def is_happy_number(num):
    seen = set()  # To store previously seen numbers
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(i) ** 2 for i in str(num))
        
    return num==1

# Test the function with a number
num = int(input("Enter a number: "))
print(is_happy_number(num))
if is_happy_number(num):
    print(f"{num} is a Happy Number")
else:
    print(f"{num} is not a Happy Number")
'''


'''

def find_n_largest_elements(lst, n):
    # Sort the list in descending order
    sorted_lst = sorted(lst, reverse=True)
    # Get the first N elements
    print(sorted_lst)
    largest_elements = sorted_lst[:n]
    return largest_elements

# Number of largest elements to find
N = int(input("Enter the value of N: "))

# Sample list of numbers
numbers = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34]

# Find the N largest elements from the list
result = find_n_largest_elements(numbers, N)

# Print the N largest elements
print(f"The {N} largest elements in the list are:", result)
'''

'''

def is_binary_str(input_str):
    # Iterate through each character in the input string
    for i in input_str:
        # Check if the character is not '0' or '1'
        if i not in '01':
            return False  # If any character is not '0' or '1', it's not a binary string
    return True  # If all characters are '0' or '1', it's a binary string

# Input string to check
input_str = "1001110"

# Check if the input string is a binary string
if is_binary_str(input_str):
    print(f"'{input_str}' is a binary string.")
else:
    print(f"'{input_str}' is not a binary string.")
'''


# TO find duplicates eliments
'''
a=[1,2,3,2,6,10,11,3]

dic={}
c=[]
for i in a:
    dic[i]=dic.get(i,0)+1


for key,value in dic.items():
    if value >=2:
        c.append(key)


print(dic)
print("Duplicates elements are",c)'''
'''

dictionary built in methods

dic.key , dic.value,dic.update(dic2)
key 
value 
update
from keys
copy
pop
popitem
fromkeys
clear
'''


'''

from collections import OrderedDict

def check_order(string, reference):
    # Create OrderedDicts for both strings
    string_dict = OrderedDict.fromkeys(string)
    print(string_dict)
    reference_dict = OrderedDict.fromkeys(reference)
    
    # Check if the OrderedDict for the string matches the OrderedDict for the reference
    
    return string_dict == reference_dict

# Input strings
input_string = "hello world"
reference_string = "helo wrd"

# Check if the order of characters in input_string matches reference_string
if check_order(input_string, reference_string):
    print("The order of characters in the input string matches the reference string.")
else:
    print("The order of characters in the input string does not match the reference string.")



'''

'''

ordereddict built in methods


move_to_end(key, last=True): Move an item to the end or start.
popitem(last=True): Remove and return an item (from the end or start).
clear(): Remove all items.
copy(): Return a shallow copy of the OrderedDict.
fromkeys(iterable, value=None): Create an OrderedDict with specified keys and values.
update([other]): Update dictionary with key-value pairs from another dictionar'''

'''
import re

# Function to check if a password is valid
def is_valid_password(password):
    # Check the length of the password
    print(password)
    if 6 <= len(password) <= 12:
        # Check if the password matches all the criteria using regular expression
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])", password):
            return True
    return False
    
# re.match(r"^(?=*[a-z])(?=.*[A-Z]))
# Initialize a list to store valid passwords
valid_passwords = []

# Accept input from the user as comma-separated passwords
passwords = input("Enter passwords separated by commas: ").split(',')

# Iterate through the passwords and check their validity
for psw in passwords:
    if is_valid_password(psw.strip()):  # strip() removes extra spaces
        valid_passwords.append(psw.strip())
        print(valid_passwords)

# Print the valid passwords separated by commas
print(','.join(valid_passwords))
'''

'''

def binary_search(arr, k, f, l):
    while f <= l:  # Search as long as f is less than or equal to l
        m = (f + l) // 2  # Correctly calculate the middle index
        
        if arr[m] == k:  # If the middle element is the target
            return m
        
        elif arr[m] > k:  # If the target is smaller, narrow the search to the left half
            l = m - 1
        else:  # If the target is larger, narrow the search to the right half
            f = m + 1
            
    return -1  # If the element is not found, return -1

# Example array
arr = [2, 6, 15, 5, 10, 22, 1, 4]
arr = sorted(arr)  # Sort the array

k = 10  # Target element

# Perform the binary search
index = binary_search(arr, k, f=0, l=len(arr) - 1)

# Check the result
if index != -1:
    print("True")
else:
    print("False")
'''

'''
def even_numbers(n):
    # Generate even numbers from 0 to n
    for num in range(n + 1):
        if num % 2 == 0:
            yield num
          
try:
    # Take input from the user
    n = int(input("Enter a value for n: "))
    
    # Get the generator for even numbers
    result = even_numbers(n)
    print(result)
    
    # Convert the result to a list and join them as a string
    print(','.join(map(str,result)))

except ValueError:
    # Handle invalid input
    print("Invalid input. Please enter a valid integer for n.")
'''


'''



def extract_username(email):
    # Split the email address at '@' to separate the username and domain
    parts = email.split('@')
    print(parts)
    
    # Check if the email address has the expected format (i.e., one '@' symbol)
    if len(parts) == 2:
        return parts[0]  # The username is the first part
    else:
        return "Invalid email format"  # Return an error message if the format is incorrect

try:
    # Accept the email address from the user
    email = input("Enter an email address: ")
    
    # Call the function to extract the username
    username = extract_username(email)
    
    # Print the extracted username or error message
    print(username)

except Exception as e:
    # Handle unexpected errors and invalid input
    print(f"An error occurred: {e}")






def filter_list(lst):
    # Use a list comprehension to filter out integers
    return [x for x in lst if isinstance(x, int)]

# Example usage
result = filter_list([1, 2, 3, "a", "b", 4])
print(result)
'''
'''
def filter_list(1st):
    return [x for x in 1st if isinstance(x, int)]

result = filter_list([1,2,3,4,5,'a','b',4])
print(result)
'''



