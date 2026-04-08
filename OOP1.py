class Student_data:
    def __init__(self,name,email,phone,rollno):
        self.name=name
        self.email=email
        self.phone=phone
        self.rollno=rollno
        
    def changephone(self,newphone):
        self.phone=newphone
        print(f"NEW phone Number:{self.phone}")
        

output=Student_data("hadi khan","hadi45@gmail.com","534546463","456789")
 #IT gives the id of class where the class data is saved
print(output)

#FOR access data from the  class we have to write it as
print(output.name,output.rollno,output.email,output.phone)

#IF we have to change the data in class we have to make a function in class and call it like as
output.changephone("83578376348768")


#NEW CLASS OF GUEST 
class Guest:
    def __init__(self , guest_id , guest_name , contact , email , address):
        self.guest_id= guest_id
        self.guest_name= guest_name
        self.contact= contact
        self.email= email
        self.address= address
        
    def addGuest(self,Guest):
        print(f"New Guest {Guest} added Successfully!!")

    def removeGuest(self,removeguest):
        print(f"GUEST removed{removeguest} Successfully")
        
    def showdetails(self,details):
        print(f"Details of GUEST {details}")
        
    def updateinfo(self,update):
        print(f"GUEST DATA {update} Successfully!!")


data=Guest(345,"hadi khan","03156629475","hadikh45@gmail.com","Razabad") 
print(data.guest_id,data.guest_name,data.contact,data.email,data.address)

data2=Guest(346,"subhan khan","034566778295","subhankh5@gmail.com","FAISLABAD") 
print(data2.guest_id,data2.guest_name,data2.contact,data2.email,data2.address)

data.removeGuest("hadi khan")
data.addGuest("Ali khan")
data.showdetails("hadi khan ")
data.updateinfo("hadi khan ")

print(data.guest_id,data.guest_name,data.contact,data.email,data.address)


#CORECT FORM OF GUEST  CLASS
class Guest:
    def __init__(self, guest_id, guest_name, contact, email, address):
        self.guest_id = guest_id
        self.guest_name = guest_name
        self.contact = contact
        self.email = email
        self.address = address

    def addGuest(self):
        print(f"New Guest {self.guest_name} added successfully!")

    def removeGuest(self):
        print(f"Guest {self.guest_name} removed successfully!")

    def showDetails(self):
        print("Guest Details:")
        print("ID:", self.guest_id)
        print("Name:", self.guest_name)
        print("Contact:", self.contact)
        print("Email:", self.email)
        print("Address:", self.address)

    def updateInfo(self, name, contact, email, address):
        self.guest_name = name
        self.contact = contact
        self.email = email
        self.address = address
        print("Guest information updated successfully!")


# Objects
data = Guest(345, "Hadi Khan", "03156629475", "hadikh45@gmail.com", "Razabad")
data2 = Guest(346, "Subhan Khan", "034566778295", "subhankh5@gmail.com", "Faisalabad")

# Methods call
data.addGuest() 
data.showDetails()

data.updateInfo("Ali Khan", "03000000000", "ali@gmail.com", "Lahore")
data.showDetails()

data.removeGuest() 
