lis=[]
greet="Adieu, adieu, to "
while True:
    try:
        name=input("Name: ")
        lis.append(name)
    except(EOFError,NameError):
        break

length=len(lis)
print('')
print(greet,end='')
for i in range(length):
    if length==1:
        print(lis[0])
        break
    elif length==2:
        print(lis[0],'and',lis[1])
        break
    elif i==(length-1):
        print('and '+lis[i])
    else:
        print(lis[i]+', ',end='')
