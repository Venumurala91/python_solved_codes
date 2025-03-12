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


str = "geeksforgeeks"
l = 102
r = 111


c=[]

for i in str:
    check_range=ord(i)
    if l <= check_range <= r: 
        c.append(i)
        

print(c)
        



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





