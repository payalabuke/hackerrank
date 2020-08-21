num=int(input("Enter a number"))
c=1
while(num>1):
    if(num%2==0):
        num=num/2
        c=c+1
    else:
        num=3*num+1
        c=c+1
print(c)
