# Given three integers ,print the smallest one .(Three integer should be user input)

p =int(input("enter a first no."))
q = int(input("enter a second no."))
r =int(input("enter a third no."))
if p<q and p<r:
    print("p is the smallest no.")
elif q<p and q<r:
    print("q is smallest no.")
else:
    print("r is smallest no.")