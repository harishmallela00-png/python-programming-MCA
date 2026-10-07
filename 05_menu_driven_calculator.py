print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter Choice : "))
a=float(input("Enter First Number : "))
b=float(input("Enter Second Number : "))

if choice==1:
    print("Addition =",a+b)
elif choice==2:
    print("Subtraction =",a-b)
elif choice==3:
    print("Multiplication =",a*b)
elif choice==4:
    if b!=0:
        print("Division =",a/b)
    else:
        print("Division by Zero Not Possible")
else:
    print("Invalid Choice")
