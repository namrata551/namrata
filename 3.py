# Check whether the user input number is even or odd and display it to user.

x =int(input("enter a number:"))
y =x%2
if y ==0:
    print("number is even")
else:
    print("number is odd")