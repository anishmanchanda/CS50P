grocery={}
sortgrocery={}
while True:
    try:
        item=input()

        if item in grocery:
            grocery[item]+=1
        else:
            grocery[item]=1
    except(EOFError,NameError):
        break
sortgrocery=dict(sorted(grocery.items()))
print()
for item in sortgrocery:
    print(str(grocery[item])+" "+item.upper())
