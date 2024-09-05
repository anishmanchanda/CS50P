expression=input("Expression: ")
lis=expression.split()
x=int(lis[0])
y=lis[1]
z=int(lis[2])
if y=="+":
    print(float(x+z))
elif y=="-":
    print(float(x-z))
elif y=="*":
    print(float(x*z))
elif y=="/":
    print(float(x/z))
