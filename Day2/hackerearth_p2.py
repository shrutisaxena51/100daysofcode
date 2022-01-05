'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

Problem
You are provided an array  of size  that contains non-negative integers. Your task is to determine whether the number that is formed by selecting the last digit of all the N numbers is divisible by .
'''

N = int(input())
data = [int(x) for x in input().split()]
 
lastDigit = data[N - 1] % 10;
 
    # Number formed will be divisible by 10
if (lastDigit == 0) :print("Yes")
else:print("No")    
