dict={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def main():
    sum=0
    while True:
        try:
            item=input("Item: ")
            item=item.title()
            for k in dict:
                if item==k:
                    value=dict[k]
                    sum+=value
                    l=str(sum).split('.')
                    num=l[0]
                    deci=l[1]
                    if(len(deci)==1):
                        deci=deci+'0'
                    print("Total: "+"$"+num+"."+deci)
        except EOFError:
            break

main()
