def GCD(x,y):
    while(y):
        x,y= y, (x%y)
    return x


tester1=input("Enter the first number:")
tester2=input("Enter the second number:")

tester1=int(tester1)
tester2=int(tester2)



print("The greatest common denominator using the Euclidian algorithm is", GCD(tester1,tester2))

