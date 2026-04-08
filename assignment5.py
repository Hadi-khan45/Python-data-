#-1 print all natural numbers from 1 to n. - using while loop
n = int(input("Enter a number: "))

i = 1
while i <= n:
    print(i)
    i += 1
    
#-2 print all natural numbers in reverse (from n to 1). - using while loop
n = int(input("Enter a number: "))

i = n
while i>=1 :
    print(i)
    i -=1
    
#-3 print all alphabets from a to z. - using while loop
alphabets= "ABCDEFGHIJKLMNOPQRSTVUXYZ"
i=0
while i < len(alphabets) :
    print(alphabets[i])
    i+=1
 
#-4 print all even numbers between 1 to 100. - using while loop
i=0
while i <= 100:
    if i %2== 0:
        print(i)
    i+=1

#-5 print all odd number between 1 to 100
i=100
while i >= 0:
    if i %2!= 0:
        print(i)
    i-=1
    
#-6 find sum of all natural numbers between 1 to n
n=int(input("Enter a number :"))
i=1
sum=0

while i <= n:
    sum += i
    i+=1
print("Sum is :",sum)

#-7 find sum of all even numbers between 1 to n
n=int(input("Enter a number :"))
i=1
sum=0

while i <= n:
    if i % 2 ==0:
        sum += i
    i+=1
print("Sum of even numbers is :",sum)

#-8 find sum of all odd numbers between 1 to n.
n=int(input("Enter a number :"))
i=1
sum=0

while i <= n:
    if i % 2 !=0:
        sum += i
    i+=1
print("Sum of odd numbers is :",sum)

#-9 print multiplication table of any number
num=int(input("Enter a number for table :"))
i=1
while i< 11:
    print(f"{num} * {i} = {num * i}")
    i +=1
    
#-10 count number of digits in a number
num=input("Enter a number for count :")
print("Digits in a number:",len(num))

#-11 find first and last digit of a number
num=input("Enter a number to check first and last digit :")
print("first digit of number:",num[0])
print("Second digit of number :",num[-1])

#-12 find sum of first and last digit of a number
num=input("Enter a number to check first and last digit :")
print("first digit of number:",num[0])
print("Second digit of number :",num[-1])
sum=int(num[0]) +int( num[-1])
print("Sum of first and last digit:",sum)

#-13 swap first and last digits of a number
num=input("Enter a number for the swapping  of  first and last digit :")

first=num[0]
last=num[-1]

temp=first
first=last
last=temp 

middle=num[1:-1]

swapped = first + middle + last
print("After swapping:",swapped)

#-14 calculate sum of digits of a number
num=input("Enter a number for there digit sum :")
i=0
total=0
while i < len(num):
    total+=int(num[i])
    i+=1
print("SUM of digits:",total)

#-15 calculate product of digits of a number
num=input("Enter a number for there digit product:")
i=0
total=1
while i < len(num):
    total*=int(num[i])
    i+=1
print("PRODUCT  of digits:",total)

#-16 enter a number and print its reverse
num = input("Enter a number: ")
rev = num[::-1]
print("Reverse:", rev)

#-17 check whether a number is palindrome or not.
num=input("Enter a number to check it is palindrome :")
if num==num[::-1]:
    print("IT is a palindrome !!",num,num[::-1])
else:
    print("IT is not a palindrome :(",num,num[::-1])
    
#-18 find frequency of each digit in a given integer
num=input("Enter a number to know their frequency:")
for number in "0123456789":
    count=num.count(number)
    if count > 0:
        print(f"Digit {number} appered in {count} times  ")
    
#-19 enter a number and print it in words.
num=input("Enter a number to Get it into words :")
words=["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]

i=0
print("Number in words:", end=" ")
while i < len(num):
    digit=int(num[i])
    print(words [digit],end=" ")#end=" " it means that there is a space after every word not a new line
    i+=1
    
#-20 calculate factorial of a number  
import math

num=int(input("Enter a number for its factorial:"))
output=math.factorial(num)
print(output)

#-21 power of a number using for loop
num=int(input("Enter a number for base :"))
num2=int(input("Enter a number for power :"))
output=int(math.pow(num,num2))
print(f"number = {num} , power = {num2} : ", output)



    

