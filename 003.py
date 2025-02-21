for i in range(26):
 print(chr(i+65))

n=int(input("Enter a number:"))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

input_string = input("Enter the value:")
alphabets = 0
digits =0
for char in input_string:
 if char.isalpha():
 alphabets += 1
 elif char.isdigit():
 digits += 1
print(“Alphabets :”,alphabets, ”Digits:”, digits)

num = int(input('Enter:'))
print('the entered number is',num)
if(num == 1):
 print("it is not a prime num.")
elif(num%2 and num%3 != 0):
 print('it is a prime num')
else:
 print('it is not a prime number')

side1 = int(input("Enter the first side:"))
side2 = int(input("Enter the second side:"))
side3 = int(input("Enter the third side:"))
if((side1**2)+(side2**2)==(side3**2) or (side3**2)+
(side2**2)==(side1**2) or (side1**2)+(side3**2)==(side2**2)):
 print("It is a triplets of pythogorean")
else:
 print("Not")

for h in range(24):
 if h== 0:
 print("12:00 Midnight")
 elif h== 12:
 print("12:00 Noon")
 elif h< 12:
 print(f"{hour}:00 AM")
 else:
 print(f"{hour - 12}:00 PM")

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))
n_fact = 1
for i in range(1, n + 1):
 n_fact *= i
r_fact = 1
for i in range(1, r + 1):
 r_fact *= i
n_r_fact = 1
for i in range(1, n - r + 1):
 n_r_fact *= i
nCr = n_fact // (r_fact * n_r_fact)
nPr = n_fact // n_r_fact
print("The nCr is",nCr)
print("The nPr is",nPr)

n = int(input("Enter the number:"))
fact = 1
for i in range(1,n+1):
 fact *= i
print("The factorial of n is:",fact)

n = int(input("Enter the number:"))
for i in range(n,0,-1):
 print(i)

N = int(input("Enter the number : "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(N):
 print(a, end=" ")
 a, b = b, a + b

import math
x = float(input("Enter x in radians: "))
sin_x = math.sin(x)
print(f"sin({x}) = {sin_x}")
