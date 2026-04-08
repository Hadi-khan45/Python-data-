print("Input is used  to get the output or values from the user ")

userinput= input("Enter your number:")
print(userinput )
print(float(userinput))

print ( " concept of return awnser: ")
def parent():
    
    def child():
        y = 20
        return y   # 🔥 return
    
    value = child()   # 🔥 store
    print(value)

parent()     



print("concept of nested/parent and child functions:") 

def parent():
    
    def child():
        result = 10 + 5
        print("Child ke andar result:", result)  # ✅ yahan accessible hai
        print(result * 2)  # ✅ yahan bhi use kar sakte ho
        return result
    
    child()

parent()  