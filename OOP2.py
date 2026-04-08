# FOUR PILLARS OF OOP (Object Oriented Programming):
#-1 Inheritance (Multiple Inheritance , Multilevel Inheritance )
#-2 Encapsulation
#-3 Abstraction
#-4 Polymorphism

#-1 CHECKING THE INHERITANCE IN OOP():
class Principal:
    def __init__(self,name,email,rank):
        self.name=name
        self.email=email
        self.rank=rank
        
class Teacher (Principal):
    def __init__(self,degree,name,email,rank):
        super().__init__(name,email,rank)
        self.degree=degree
        
class Student(Teacher):
    def __init__(self,Class,degree,name,email,rank):
        super().__init__(degree,name,email,rank)
        self.Class=Class
 
# Principal Class working        
principal=Principal("Subhan Khan","subhan44@gmail.com","18 grade")
print(principal)
print(principal.email,principal.name,principal.rank)

# Teacher Class Inherited with Principal Class        
teacher=Teacher("MPHIL","Hadi khan","hadi23@gamil.com","16 grade")
print(teacher)
print(teacher.degree,teacher.email,teacher.name,teacher.rank)

# Student Class Inherited with Teacher Class
student=Student("10 class","Matric","Ahmad Khan","Ahmad45@gmail.com","no rank")
print(student)
print(student.Class,student.degree,student.name,student.email,student.rank)

#THIS is for student 2
student2=Student("10 class","Matric","Ali khan","Ali45@gmail.com","no rank")
print(student2)
print(student2.Class,student2.degree,student2.email,student2.name,student2.rank)


#-2 CHECKING THE ENCAPSULATION IN OOP():
class Company1:
    def __init__(self,modelno,quantity,code):
        self.modelno=modelno
        self.quantity=quantity
        self.__code=code
        
    def mycode(self):
        print("My code :",self.__code)
        
class Company2(Company1):
    def __init__(self,product,modelno,quantity,code):
        super().__init__(modelno,quantity,code)
        self.product=product
        
data=Company1("Honda125",125,4539)
print(data.modelno,data.quantity)

data2=Company2("Bikes",23323,67,6789)
print(data2.modelno,data2.quantity,data2.product)

#THIS is how we access private member of class by making another function for it calling it 
data.mycode()  
data2.mycode() 

#-3 CHECKING THE ABSTRACTION IN OOP():
class Abstract:   
    def update_name(self):
        pass
    
    def delete_name(self):
        pass
    
    def new_name(self):
        pass
    
class Student(Abstract):
    def __init__ (self,Name, Class):
        self.Name=Name
        self.Class=Class
        
    def update_name(self):
        print("name updated successfully")
        
    def delete_name(self):
        print("name deleted successfully")
        
    def new_name(self):
        print("new name added successfully")
        
output=Student("hadi",19)
print(output)

print(output.Name,output.Class)

output.update_name()

#-4 CHECKING THE POLYMORPHISM IN OOP():
class sound:   
    def sound(self):
        pass

class Dog(sound):
    def sound(self):
        return "Woof !"

class Cat(sound):
    def sound(self):
        return "Meow !"
    
def make_sound(animal):
    print(animal.sound())

dog = Dog()
print(dog)
cat = Cat()   
print(cat)  

make_sound(dog)
make_sound(cat)


        
    
