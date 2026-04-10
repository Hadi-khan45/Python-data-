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


try:
    # Code that may raise an exception
    result = int(input("Enter a number: "))
except ValueError:
    # Handle ValueError
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    # Handle any other exception
    print("An error occurred:", e)