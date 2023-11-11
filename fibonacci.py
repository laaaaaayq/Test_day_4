n=int(input("Enter the number : "))
sum1=1
sum2=0
sum3=0
for i in range(n+1):
    if i==0:
        sum2=0
    elif i==1:
        sum1=1
    else:
        sum3=sum1+sum2
        sum2=sum1
        sum1=sum3
if n==0:
    print(0)
elif i==1:
    print(1)
else:
    print(sum3)



