#PARAMETRS :
            #1- Default arguments
            #2- Keyword arguments
            #3- Positional or Required arguments
            #4- Keyword-only arguments 
            #5- Positional-only arguments
            #6- Arbitary and variable length arguments 
        
        

print("start checking function and parametrs ")
def check(a=30 , b=45):
    num1 = 45
    num2 = 30
    result = num1 + a + num2 + b 
    print("awnser of main function: ",result)
    print("1st function ends here ")
    def check2(b=30,a=45):
        num3= 30
        num4 = 20
        result1= a + num3 + b + num4 + result
        print("awnser of  1st nested function:",result1)
        print("2nd function ends here ")
        return result1
    check2(90,35)
    def check3(b=46,a=34):                                
        num1= 37
        num2= 78
        result= num1 + a + b + num2 
        print ( "Awnser of 2nd nested function: ",result)
        print("3rd function ends here ")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    check3(result,5)        
        
check()     


print( "checking prositional-only arguments:" )
def arm(a ,b=39,/):
    num1 = 45
    num2= 35
    result= num1 + num2  + a + b 
    print(result)

arm( 34 ,45 )

print("Checking Keyword-only arguments:")
def arm2(a,*, b):
    num1 = 60
    num2 = 50
    result= num1 + num2 + a + b 
    print(result)

arm2(34, b=56)

print("Checking arbitary and variable length arguments :")
def arm3(*Values):
    print("Values: ",Values)

arm3(10 , 40 , 50 , 34, 45 ,4534 ,43 )

def arm4(**Values):
    print("Values :",Values)

arm4(a= "Abdul hadi khan",b= 4539, c= 344)


