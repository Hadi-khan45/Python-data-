# STRING BUILT IN FUNCTIONS:


# LENGTH FUNCTION:
name="   Abdul hadi khan    ."
print(len(name))

num=str(242424)

print(type(name))


print(type(num))

print(name + num)
print(name * 5)
print(name[0])
print(name[0:16])

print(name[0:16:2])
print(name[0:len(name):1])

#FUNCTIONS for STRINGS:

print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.title())

print(name.strip())
print(name.lstrip())
print(name.rstrip())

print(name.find("ahmad"))
print(name.index("hadi"))

print(name.count('a'))
 
print(name.replace("hadi","HADI "))

print(name.split())

names=["hadi","ahmad","ali"]
print("  ".join(names))

print(name.startswith('m'))
print(name.endswith('.'))
print("hadi"in name)

name1="hadikhan"
name2="hadi4539"
name3="2423525"
name4="            "
print(name1.isalpha())
print(name3.isdigit())
print(name2.isalnum())
print(name4.isspace())


