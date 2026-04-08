print(" checking the nested function and return type :")

def SUM(a,b ):
    num2 = 35
    num1= 45
    result = num1 + num2 + a + b 
    print(result)
    return result 

def SUM1(a=60,b= 45):
     num1 = 25
     num2= 35
     result = num1 * num2 + a + b 
     return SUM(result,20)

 


def multiply(a=40,b=30):
    result = a  * b
    return result


def subtract( a = 45, b= 40):
    result = a - b * 5
    return result

def main():
    multiply(30,20)
    subtract(40,60)
    result = multiply()+subtract()
    return multiply(result,20 )

result = main()
print(result)
    



def SUM(a=45,b=60):
    result= a + b 
    print(result)
    def SUM2(a=45,b=65):
        result= a-b
        return result
    SUM2(result,10)   
    


