#RANDOM MODULE IS USED TO GENRATE RANDOM NUMBERS
#MATH MODULE IS USED TO PERFORM MATHEMATICAL CALCULATIONS
#OS (OPERATING SYSTEM) MODULE IS USED TO INTERACT WITH THE OPERATING SYSTEM

import random 
import math
import os 

#RANDOM MODULE :
ans=random.randint(1,100)
print(ans)

output=random.random()
print(output)

list=[1,2,3,4,5]
random.shuffle(list)
print(list)

sand="%&$#@%&&%$#@"
input = str(int(random.random()*1000332244)) + sand[random.randint(0, len(sand)-1)]
print(input)

#MATH MODULE :
num=int(math.sqrt(144))
print(num)

num1=math.factorial(12)
print(num1)

num2=math.pow(4,3)
print(num2)

num3=math.ceil(4.3424243) #IT increases the number after round off
print(num3)

num4=math.floor(4.3424243) #IT decreases the number after round off
print(num4)

#OS MODULE :
file=os.getcwd()
print(file)

file1=os.listdir()
print(file1)

#____________________________________________
#file2=os.makedirs("main13.py")
#print(file2)
#____________________________________________

#file3=os.rmdir("main13.py")
#print(file3)

#file4=os.remove("main13.py")
#print(file4)

#file5=os.rename("main12.py","main13.py")
#print(file5)

#file5=os.rename("main13.py","main12.py")
#print(file5)

#file6=os.path.exists("main12.py")
#print(file6)

#file7=os.environ
#print(file7)