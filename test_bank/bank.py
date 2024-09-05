def main():
    greet=input("enter greeting: ")
    print("$"+str(value(greet)))
def value(greeting):
    greeting=greeting.lower()
    greeting=greeting.strip()
    c1=greeting.startswith("hello")
    c2=greeting.startswith("h")
    if c1:
        return 0
    elif (c2 and not c1):
        return 20
    else:
        return 100

if __name__=="__main__":
    main()
