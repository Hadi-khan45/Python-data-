#-1 Light bulb Experiment 
button = int(input("To on bulb enter 1 :)   or   To off bulb enter 0 :(  --> Enter number :"))
if button ==1:
    print("BULB is ON! :)")
elif button ==0:
    print("BULB is OFF! :(")
else :
    print("INVALID INPUT :(")
    
#--------------------------------------------------------------------------
    
#-2 Traffic light simulator 
lights={"Red","yellow","Green"}
traffic=(input(f"Enter {lights} your colour from those :) -->"))
if traffic =="Red":
    print("STOP !!!")
elif traffic =="yellow":
    print("SLOW DOWN :(")
elif traffic == "Green":
    print("GO :)")
else:
    print("INVALID COLOUR ")    

#----------------------------------------------------------------------------

#-3 Water temprature checker 
temprature=int(input("Give temprature of water in celcius:"))
if temprature <=0 :
    print("Freezing ;(")
elif temprature > 0 and temprature  <= 15:
    print("COLD !!! ")
elif temprature > 15 and temprature  <=30:
    print("WARM !!!")
elif temprature >30 :
    print("HOT !!!")
    
 #--------------------------------------------------------------------------
    
#-4 Rock , paper , scissors game 
tools={"Rock","Paper","Scissor"}
player1 = (input(f"Player 1 {tools } choose your tool :"))
player2 = (input(f"Player 2 {tools } choose your tool :"))

if player1 == player2 :
    print("IT is a TIE match :(")
elif (player1 == "Rock" and player2 =="Scissor" or 
      player1 == "Paper"and player2 =="Rock"or 
      player1 == "Scissor"and player2 =="Paper"):
    print("player 1 wins !!!! :)")
    
else :
    print("player 2 wins !!!! :)")
    
#------------------------------------------------------------------------------

#-5 Simple alarm system 
Check={"ENTER ":"Yes/No" }
awnser1=input(f"IS the DOOR OPEN {Check} ? ")
awnser2=input(f"IS motion dectected{Check} ?")
if awnser1 == 'Yes'or'yes' or  awnser2=='Yes'or'yes':
    print("Alarm Triggered :(")
else:
    print("ALL safe :)")
    
#------------------------------------------------------------------------------

#-6 Maximum of Two Numbers
number1=int(input("Enter first numbers:"))
number2=int(input("Enter second number:"))
if number1 > number2:
    print(f"{number1} is larger :)")
elif number2 > number1:
    print(f"{number2} is larger :)")
else :
    print("Numbers are equal to each other :(")

#---------------------------------------------------------------------------------

#-7 Eligibility for Voting
voter_age=int(input("Enter your age :"))
if voter_age >=18:
    print("You are eligible for vote :)")
else:
    print("You are not eligble for vote :(")
    
#---------------------------------------------------------------------------------

#-8 Weather suggestion Experiment
seasons={"Sunny","Rainy","Cold"}
awnser=(input(f"Enter {seasons} your Weather from those :) -->"))
if awnser =="Sunny":
    print("Wear sunglasses :) !!!")
elif awnser =="Rainy":
    print("Take an umbrella :(")
elif awnser == "Cold":
    print(" Wear a jacket :)")
else:
    print("INVALID WEATHER !!!")    
    
#---------------------------------------------------------------------------------

#-9 Simple Temperature Conversion
choice=int(input("Choose conversion type : || 1-Celcius to fahrenheit || 2-Fahrenheit to Celcius || Choose 1 or 2:"))
temp=float(input("Enter your temprature:"))
if choice==1:
    #Convertion from celcius to fahrenheit 
    F=(temp * 9/5)+32
    print("Your temprature in Fahrenheit:",F)
elif choice==2:
    #Conversion from fahrenheit to Celcius 
    C=(temp -32 )* 5/9
    print("Your temprature in Celcius :",C)
else:
    print("Invalid input Plz Choose from the choices 1 or 2 :)")

#________________________________________________________________________________

    