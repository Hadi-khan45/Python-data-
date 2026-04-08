  
# program of checkng number it is even or odd or zero   
userinput = int(input("Enter a number :"))

if userinput == 0:
    print("IT is a ZERO :(") 
    
    
elif userinput  %2 ==0 :
    print("IT is a even number :) ")
    
else :
    print("IT is a odd number :)")
    
#------------------------------------------------------------------------------------------------------------- 
 
#program of printing weekdays using if , elif , else conditions 
   
hell= int (input("Enter a Number :) "))
if hell == 0 :
    print("Sunday :)")
    
elif hell==1 :
    print("Monday :)")
    
elif hell == 2:
    print("Tuesday :)")
    
elif hell == 3:
    print ("Wednesday :)")
    
elif hell == 4:
    print ("Thursday :)")
    
elif hell == 5 :
    print ("Friday  :)")
    
elif hell == 6:
    print (" Saturday  :)")
    
else : 
    print("Invalid NUmber !!!!! :(")        

# ----------------------------------------------------------------------------------------------------------------------
#program of printing weekdays using MATCH case it is the alternative of using else , elif , if satements in same program 

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
        

#---------------------------------------------------------------      
# if , elif , else / match condition kaha per suitable hai :) 

       
# Maths comparison                             if
# Range checking                               if
# Complex logic	                               if 
# Fixed options menu	                       match
# Clean readable multiple equal values	       match         

#---------------------------------------------------------  
   
# 2 separate if or elif ka concept 

#2 Separate if              --     	if + elif
#_________________________________________________________
#Dono check honge	        --       Ek hi chalega
#Multiple output aa sakte	--      Sirf ek output
#Independent conditions	    --       Connected conditions
#Slow thoda	                --      Thoda efficient


