#HCF
# 13 39 - 13
# 12 18 - 6
a=int(input("Enter a num"))
b=int(input("Enter another num"))

if a>b:
    for i in range(1,a):
        if(a%i==0 and b%i==0):
            c=i
else:
    for i in range(1,b):
        if (a % i == 0 and b % i == 0):
            c = i

print(c)

