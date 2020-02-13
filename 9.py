# check whether the given year is leap year or not.if year is leap print'LEAP YEAR' else print'COMMON YEAR'
x =int(input("enter a year:"))
if x%4 ==0 and x%100 ==0 and x%400 ==0:
    print("year is a leap year")
elif x%4 ==0 and x%100 ==0 !=0:
    print("year is a leap year")
else:
    print("year is a common year")