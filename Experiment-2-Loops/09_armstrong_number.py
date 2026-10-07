num=int(input("Enter Number : "))
temp=num
total=0
while temp>0:
    digit=temp%10
    total=total+digit**3
    temp=temp//10
if total==num:
    print("Armstrong")
else:
    print("Not Armstrong")
