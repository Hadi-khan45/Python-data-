#-1  check which number is maximum between two numbers
num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
if num1 > num2:
    print(f"{num1} is larger number :)")
elif num2 > num1:
    print(f"{num2} is larger number :)")    
else :
    print("Both numbers are equal :(")
        
#------------------------------------------------------------------------------

#-2  check which number is maximum between three numbers
num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
num3=int(input("Enter third number :"))

if num1 > num2 and num1 > num3:
    print(f"{num1} is larger number :)")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is larger number :)")    
elif num3 > num1 and num3 > num2:
    print(f"{num3} is larger number :)")
else :
    print("ALl  numbers are equal :(")

#------------------------------------------------------------------------------

#-3 check whether the number is positive, negative or zero
num=int(input("Enter a number :"))
if num > 0:
    print(f" IT is a  positive number {num} ")
elif num < 0:
    print(f"IT is a negative number {num}")
else :
    print("IT is a zero number :(")   
          
#------------------------------------------------------------------------------

#-4 check whether the number is even or odd
num=int(input("Enter a number :"))
if num % 2 == 0:
    print("IT is an even number :)")
else :
    print("IT is an odd number :(")

#------------------------------------------------------------------------------

#-5 CHECK THAT number is divisible by 5 , 11 or not 
num=int(input("Enter a number :"))
if num % 5 == 0 :
    print(f"{num} is divisible by 5 :)")
elif num % 11 == 0 :
    print(f"{num} is divisible by 11 :)")
else :
    print(f"{num} is not divisible by 5 and 11 BOTH  :(")

#------------------------------------------------------------------------------

#-6 CHECK THAT it  is leap year or not 
year=int(input("Enter the number of days in a year :"))
if year ==365:
    print("IT is a common year :)")
elif year ==366:
    print("IT is a leap year :)")
else:
    print("hey!! blud you dont know the number of days in a year :(")
    
#------------------------------------------------------------------------------

#-7 CHECK THAT the character is alphabet or not 
alpha=input("Enter a character :")
if alpha.isalpha():
    print(f"{alpha} is an alphabet :)")
else:
    print(f"{alpha} is not an alphabet :(")
    
#------------------------------------------------------------------------------

#-8 CHECK THAT the character is vowel or conconant
letter=input("Enter a character")
if letter in "aeiouAEIOU":
    print(f"{letter} is a vowel :)")
else:
    print(f"{letter} is a consonant :)") 
    
#------------------------------------------------------------------------------

#-9 CHECK THAT the character is alphabet or digit or special character
char=input("Enter a character :")
if char.isalpha():
    print("IT is an alphabet :)")
elif char.isdigit():
    print("IT is a digit :)")
else:
    print("IT is a special character :(")
    
#------------------------------------------------------------------------------

#-10 CHECK THAT the character is uppercase or lowercase
char=input("Enter a character :")
if char.isupper():
    print("IT is an uppercase letter")
elif char.islower():
    print("IT is a lowercase letter")
else:
    print("IT is not a alphabet :(")

#------------------------------------------------------------------------------

#-11 INPUT week number and print a week day 
weekdays = int (input("ENTER A NUMBER FOR WEEKDAYS :)"))     
match weekdays : 
    case 0 :
        print("Monday :)")
    case 1 :
        print("Tuesday :)")
    case 2 :
        print("Wednesday :)")
    case 3 :
        print("Thurday :)")
    case 4 :
        print("Friday :)")
    case 5 :
        print("Saturday :)")
    case 6 :
        print("Sunday :)")
    case _:
        print("IT is a inalid weekday number :()")   
    
#------------------------------------------------------------------------------

#-12  INPUT month number and print number of days in that month
month=int(input("Enter a month number : "))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("IT has 31 days :)")
elif month==4 or month==6 or month==9 or month==11:
    print("IT has 30 days :)")
elif month==2:
    print("IT has 28 or 29 days :)")
else:
    print("IT is an invalid month number :(")
    
#------------------------------------------------------------------------------

#-13 CHECK THAT triangle through angles is valid or not 
A=int(input("Enter the 1st angle  of triangle :"))
B=int(input("Enter the 2nd angle of triangle :"))
C=int(input("Enter the 3rd angle of triangle :"))
if A + B + C == 180:
    print("IT is an VALID triangle :)")
else:
    print("IT is an INVALID triangle :(")
    
#------------------------------------------------------------------------------

#-14 CHECK that triangle through sides is valid or not
a=int(input("Enter the 1st side of triangle :"))
b=int(input("Enter the 2nd side of triangle :"))
c=int(input("Enter the 3rd side of triangle :"))
if a + b > c and b +c > a and c + a > b:
    print("IT is an VALID triangle :)")
else:
    print("IT is an INVALID triangle :(")
    
#------------------------------------------------------------------------------

#-15 CHECK that triangle is equilateral, isosceles or scalene
a=int(input("Enter the 1st side of triangle :"))
b=int(input("Enter the 2nd side of triangle :"))
c=int(input("Enter the 3rd side of triangle :"))
if a==b==c:
    print("IT is an equilateral triangle")
elif a==b or b==c or c==a:
    print("IT is an isosceles triangle")
else:
    print("IT is an scalene triangle")
    
#------------------------------------------------------------------------------

#-16 CHECK GRADES of subjects 
physics = float(input("Enter marks of Physics: "))
chemistry = float(input("Enter marks of Chemistry: "))
biology = float(input("Enter marks of Biology: "))
math = float(input("Enter marks of Mathematics: "))
computer = float(input("Enter marks of Computer: "))

total = physics + chemistry + biology + math + computer
percentage = total / 5

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print("Total Marks =", total)
print("Percentage =", percentage)
print("Grade =", grade)

#------------------------------------------------------------------------------

#-17 
    