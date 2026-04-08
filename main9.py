#Check the loops in table and array 
usernumber=int(input("Enter a number for  table:"))
tablelength=int(input("Enter the length of table:"))
i=1
while i<=tablelength:
    print(f"{usernumber} * {i} = {usernumber * i}")
    i+=1  
#---------------------------------------------------      
 
# reverse condition of loop
i = 10
while i>1:
    print(i)  
    i-=1   
#--------------------------------------------------   
  
#CHECK array function in loop
inputlist=[10,20,30,35,45,60,79]
outputlist=[]
i=0
while i<len(inputlist):
    outputlist.append(inputlist[i] * 2)
    i+=1
print(outputlist)  
#--------------------------------------------------

#Check array in loop with if or else    
inputlists=[10,20,30,35,45,60,79]
outputlists=[]
y=0
while y <len(inputlists):
    if inputlists[y]%2==0:
        result=inputlists[y]*2
        outputlists.append(result)
    else:
        result=inputlists[y]
        outputlists.append(result)
    y+=1
print(outputlists)  
#-------------------------------------------------

#CHECK the dictionary function 
car= {"name":"corolla" ,
    "company":"Toyata" ,
    "year":"2021",
    "engine":"1300 CC"}


# CRUD ( CREATE , READ , UPDATE , DELETE)

print(car)    
print(car["engine"])

car["tyres"]="4 new"
print(car)

car["year"]="2022"
print(car)

#car.popitem()
#print(car)

del car["name"]
print(car)

#car.pop("year")
#print(car)

print(car.get("brand","Key not found "))
print(car["brand"])      

#____________________________________________________

user_info = {
    "Name": input("Enter your name: "),
    "Email": input("Enter your email: "),
    "Address": input("Enter your address: "),
    "Phone": input("Enter your phone number: "),
    "Age": input("Enter your age: ")
}

print(user_info)

#----------------------------------------------------

myinfo={}
name=input("Enter your name :")
age=input("Enter your age:")
email=input("Enter your email:")
phone=input("Enter your number:")
address=input("Enter your address:")

myinfo["name"]=name
myinfo["age"]=age
myinfo["address"]=address
myinfo["phone"]=phone
myinfo["email"]=email

print(myinfo) 

#------------------------------------------------

#FOR LOOP  AND WHILE LOOP  IN PYTHON 

for value in range(1,45,1):
    print("Number is ", value )
    
i=1
while i <45:
    print("Number is ",i)
    i+=1
      
# for loop example
items = ['apple', 'banana', 'cherry']
for item in items:
    print(item)

# another for loop using range
for i in range(5):
    print(i) 

#---------------------------------------------------------    
#MAP loop
usernames=["hadi","abdullah","subhan","ali","ahmad","hamza","umer","hassan","usman","bilal"]

def test(value):
    return " Hello "+ value

result = list(map(test,usernames))
print(result)

#-------------------------------------------------
#FILTER loop
numbers=[1,2,3,4,5,6,7,8,9,10]

def result(value):
    if value%2!=0:
        return value*2

result=list(filter(result,numbers))
print(result) 


#CHECK the enumerate function in loop
numbers=[56 , 35 ,54 ,43 ,15 ,67 ,43 ,32 ,77,97,45 , 23, 12, 34, 56, 78, 90]
evennumbers=[]
oddnumbers=[]
for index, value in enumerate(numbers):
    print(index , value)
    if value %2==0:
        evennumbers.append(value)
    else:
        oddnumbers.append(value)

print(evennumbers)
print(oddnumbers)                

# CHECK THE DIFFERENT FUNCTIONS IN PYTHON
duplicate_values= [20,30,30,40,50,60,70,80,90,20,40,80,90,100]
values=[]


i = 0
while i < len(duplicate_values):
    if duplicate_values[i] not in values:
        values.append(duplicate_values[i])
    i += 1


         
print(values)

name=("hadi","ali","ahmad","zuhaib")
print(name)

print(name.count("ali"))
print(name.index("hadi"))


names=["hadi","ali","ahmad","zuhaib"]
print(names)


output=name[1:4]
print(output)


#____________________________________________________________________
 
# IT is an BY deafault sets 
num={10,30,20,50,20,30,40,40,50,60,40,60,50,40,30,20,30,40,50,60,50,40,30,20,10}\
# IT is an put a sets function on an array 
num2=[20,30,40,40,50,50]
num2new=list(set(num2))

print(num2)
print(num2new)
print(num)
