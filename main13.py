print("HEllo World before the error")
try:
    loading = True
    result = 10 / 5
    print(result)
except Exception as e:
    print("Error Occured", e)
else:
    print("No error Occured")
finally:
    loading = False
    print("This will always execute")
    

print("HEllo World after the error")
print("2nd exception occurd")  
print("HEllo World after the error")
print("HEllo World after the error")
print("HEllo World after the error")