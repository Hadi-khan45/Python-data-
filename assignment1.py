# Arthimetic operators(+,-,*,%,/,**,//)

num1 = 25
num2 = 30
result = num1 + num2 * 8 - 23    #242
result2 = num1 - num2 **2 % 4    #25
result3 = num1 /num2 +78 * num1  #1950.8333333333333
result4 = num2 // num1 * 56      # 56
result5=num1 ** num2 + 34        #867361737988403547205962240695953369140659

print(result)
print(result2)
print(result3)
print(result4)
print(result5)


# Assignment Operators(=,+=,-=,/=,*=,**=,//=,%=)

num3 = 25
num4 = 30

result6 = num3
result6 += num4 * 4 - 3      # 25 + (120 - 3) = 142

result7 = num4
result7 -= num3 // 5 + 4     # 30 - (5 + 4) = 21

result8 = num3
result8 *= num4 % 4 + 3      # 25 * (2 + 3) = 125

result9 = num4
result9 /= num3 - 15 + 4     # 30 / 14 = 2.142857142857143

result10 = num3
result10 **= 3 + 4           # 25 ** 7 = 6103515625


print(result6)
print(result7)
print(result8)
print(result9)
print(result10)


#Comparision operators (==, !=,<,>,<=,>=)

num5 = 25
num6 = 30

result11 = num5 + 5 > num6 - 2          # 30 > 28 → True
result12 = num6 // 3 == num5 - 15       # 10 == 10 → True
result13 = num5 * 2 != num6 + 20        # 50 != 50 → False
result14 = num6 % 7 >= num5 // 6        # 2 >= 4 → False
result15 = num5 - 5 <= num6 / 2         # 20 <= 15 → False


print(result11)
print(result12)
print(result13)
print(result14)
print(result15)


#Logical operators(and, or , not)

num7 = 25
num8 = 30

result16 = (num7 + 5 > 20) and (num8 - 10 < 25) or (num7 == 25)
# (True and True) or True → True

result17 = not (num8 // 3 == 10) or (num7 * 2 > 40) and (num8 % 4 == 2)
# not(True) or (True and True) → False or True → True

result18 = (num7 - 5 < 15) and not (num8 / 2 >= 15) or (num7 != 30)
# (False and not(True)) or True → (False and False) or True → True


print(result16)
print(result17)
print(result18)


#Membership operators(in,not in)

list1 = [10, 20, 25, 30, 40]
text = "Hadi Khan"

result19 = 25 in list1 and 50 not in list1
# True and True → True

result20 = "Hadi" in text and "Ali" not in text
# True and True → True


print(result19)
print(result20) 

#Identity operators(is , is not)

num9 = 25
num10 = 25
num11 = [1, 2, 3]
num12 = [1, 2, 3]

result21 = num9 is num10
# Same immutable value → mostly True

result22 = num11 is not num12
# Different objects in memory → True


print(result21)
print(result22)