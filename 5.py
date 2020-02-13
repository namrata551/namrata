# For a given integer x,print 'true' if it is positive ,print'false' if it is negative and print'zero'if it is 0.

a= int(input("enter a no to check to whether"))
b=a/2
if b>0:
    print("true")
elif b<0:
    print("false")
else:
    print("zero")