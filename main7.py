userinput = int(input("Enter a Number :) --> "))
if userinput %2 == 0 :
    print(f'IT is a  even number {userinput} :)')
    if userinput >= 50 :
        result = userinput + 10
        print(f'Your number {userinput} is even ', result)

if userinput %2 != 0:
    print(f'IT is a  odd number {userinput} :)')
    if userinput < 50:
        result = userinput - 10 
        print(f'Your number {userinput} is odd :)',result)
        
        
        
 
# SOME functins used in python :)
#Concatation:
studentnames=["hadi","ahmad","ali","abdullah"]
numbers=[32,554,656,757]
result=studentnames + numbers
print(result)
   
   
#length() function  is used to  know the length of an array and any word
length=len(studentnames)
length2=len("Abdullah")
print(length,studentnames,length2)


# NESTED list is used to store an arrays in the array 
list=["hadi","ahmad",[34,45,464],[434,43,34534,53454,5435]]
print(list)
result1=list[3]
result2=list[2][2]
print(result1)
print(result2)


# REPITITION function is used to repeat the values 
check=[1 , 2,3,4,5,6]
result3=[check]*5
print(result3)











    
