#DECLARE TOW VARIABLES AS X AND Y 
x=  6
y =  8

result  = x** y + x - y * x / y // 3 % 2
#RESULT IS 1679622.0
result1= x + y - x * y / y // 2 % 3 ** 2
#RESULT IS 11.0
result2=x + y - x * y / y // 2 % y ** 2
#RESULT IS 11.0
result3=x ** 2 + y - x * y / y // 4 % 3
#RESULT IS 43.0
result4= x + y - x * y / y // 3 % 2 ** y
#RESULT IS 12.0
result5=x ** y + y - x * y / y // 2 % 4
#RESULT IS 1679621.0
result6= x + y - x * y / y // 5 % 3 ** 2
#RESULT IS 13.0
result7= x ** 2 + y - x * y / y // 3 % 5
#RESULT IS 42.0
result8= x + y - x * y / y // 2 % 3 ** 2
#RESULT IS 11.0
result9=x ** y + y - x * y / y // 4 % 2
#RESULT IS 1679623.0

print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7) 
print(result8)
print(result9)

result33= x + y >= x-y + result5 * result7 
print(result33)

num1 = 70
num2 = 30

num1*=20
print(num1)        

no1= 5
no2=7

sum= no1 + no2 != no2 * 10 

print(sum)

sum1 = no1 **30 <= no2 **4
print(sum1)
                     
message = 'Hello'   
print(id(message))      
      
username = "Hadi"
value = " Hadi"

print(value is username)    

print("hello kaise ho ")    
      
      
      
      
      










