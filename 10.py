# Write a pythone program to sum of three given integers .However if two values are a equal sum will be zero.

x = int(input("enter a first no."))
y = int(input("enter a second no."))
z = int(input("enter a third no."))
sum= x+y+z
if x==y or y==z or z==x:
    print("sum of the three no is zero:")
else:
    print("sum of the three no is:",sum)
