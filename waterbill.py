# x=int(input("Litres of water used : "))
# amount=0
# for i in range(1,101):
#     if i==x:
#         amount=x*15
# for i in range(101,201):
#     if i==x:
#      amount=(15*100)+((x-100)*14)
# for i in range(201,10000000):
#     if i==x:
#         amount=(15*100)+(14*100)+((x-200)*12)
# print(amount)

x=int(input("Enter the litre of water used : "))
a=0
if 1<=x<=100:
    a=x*15
    print(a)
elif 101<=x<=200:
    a=(15*100)+((x-100)*14)
    print(a)
else:
    a=(15*100)+(14*100)+((x-200)*12)
    print(a)


