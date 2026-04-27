#PYTHON data types 

#SIMPLE TYPES
name : str="hadi"
num : int=1213
num :float=12.34
isadmin: bool=True

#GENERIC TYPES

#list
names : list[str] =["hadi","ali","ahmad"]
names1 :list[int] =[1,2,3,4,5]
names2 : list[float]= [12.34 , 145.6  , 56.434]

#tuple and set
names3 :tuple[str]=("hadi","ali","ahmad")
names4 :set[str]={"hadi","ali","ahmad"}

#dict
names5 :dict[str,int]={"name":"hadi","email":"hadi@gmail.com"}

#USED IN FUNCTIONS
def show1(first_name : str  , last_name : str  ) -> str:
    return first_name + last_name

#UNION TYPES
name6 :str | int ="hadi4539"   
names7 :list[str | int | float]=["hadi" , 3435 , 435.435]
names8 : dict[str , str | int | float]={"name":"hadi" , "age":23 , "height" : 53.6}

#UNION TYPE USED IN FUNCTIONS
def show2(first_name : str | int , last_name : str | int ) -> str | int:
    return first_name + last_name

print(show2("hadi4539" , "khan4539"))

#UNION TYPE USED IN NESTED LIST ,  DICTIONARY  AND BOTH 

#NESTED LIST 
names9 : list[list[int | str | float]] =[["hadi","ali"] , [1,2,3] , [34.45] ,["HADI",43.6 ,43]]
print(names9)

#NESTED DICTIONARY
names10 : dict[str,dict[str,int | float | str]]={"names" : {"name1":"hadi4539","name2":3425, "name3":45.45}}
print(names10)

#BOTH NESTED LIST AND DICTIONARY
names11 : dict[str,list[int | str |float ]] ={"student1":["hadi khan",19,5.6] , "student":["subhan khan",17,5.7]}

print(names11)
