#LCM


a=int(input("Enter a num"))
b=int(input("Enter another num"))
c=1
if a>b:
    for i in range(1,a):
        if(a%i==0 and b%i==0):
            c=i*c
else:
    for i in range(1,b):
        if (a % i == 0 or b % i == 0):
            c = i*c
            a = a / i
            b = b / i

print(c)

