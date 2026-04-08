# using CRUD (Create, Read, Update, Delete) operations to manage student data

dataofstudents=[
    {   "id":1,
        "name":"hadi",
        "email":"hadikh5493@gmail.com",
        "phone":"3242525345",
        "course":"python"},
    {   "id":2,
        "name":"ali",
        "email":"alishk34@gmail.com",
        "phone":"37535835786",
        "course":"java"},
    {   "id":3,
        "name":"sara",
        "email":"sarakh23@gmail.com",
        "phone":"3847564756",
        "course":"javascript"}
    ]

# CREATE DATA 
username=input("Enter your name :")
useremail=input("Enter your email:")
phone=input("Enter your phone number:")
course=input("Enter your course name :")

userdata={
    "id":len(dataofstudents) +1,
    "name":username,
    "email":useremail,
    "phone":phone,
    "course":course
}

dataofstudents.append(userdata)
print(dataofstudents)

# READ DATA 
for student in dataofstudents:
    print("id :",student["id"])
    print("name :",student["name"])
    print("email :",student["email"])
    print("phone :",student["phone"])
    print("course :",student["course"])
    
# DELETE DATA
id_delete=int(input("Enter the id of student you want to delete :"))

def delete(student):
      if  student["id"] != id_delete:
        return student



output=list(filter(delete,dataofstudents))
print(output)

#UPDATE DATA 
update_id=int(input("Enter the id you want to update : "))
update_phone=input("Enter the new phone number :")

def update(student):
    if student["id"] == update_id:
        return{
            "id":student["id"],
            "name":student["name"],
            "email":student["email"],
            "phone":update_phone,
            "course":student["course"]
        }
    else:
        return student
    
result=list(map(update,dataofstudents))
print(result)

