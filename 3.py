'''CALCULATOR'''

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("Give command as +,-,*,/")
g=input("Command: ")
while g == "+" and g == "-" and g == "*" and g == "/":
    if ("+"== g):
        print(a+b)
    elif ("-" == g):
        print(a-b)
    elif ("*" == g):
        print(a*b)
    elif ("/" == g):
        print(a/b)
    else:
        print("INVALID COMMAND")
