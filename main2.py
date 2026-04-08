 # checking operators of python 
  
  
box = {'shoes','socks','perfume'}


print('banana' not in box)
print('shoes'in box)



a = [1 , 2 ,3 ]
x = 2
print(x is a )
print (a is not x)

#functions   

print("before the values print")
def add(a  , b):
    print("value of a is ",a , "value of b is", b)
    num1 = 45
    num2 = 67
    result = num1 + num2 + a + b
    print (result)
    def abc():
        print("nested function")
        
add(34,56)
print("print after the function")
add(98,87)    

print("Hello")

# for loop example
items = ['apple', 'banana', 'cherry']
for item in items:
    print(item)

# another for loop using range
for i in range(5):
    print(i)

