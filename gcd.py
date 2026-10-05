a=int(input("enter a first number:"))
b=int(input("enter a second number:"))
while b!=0:
    a,b=b,a%b
print("gcd=",a)

