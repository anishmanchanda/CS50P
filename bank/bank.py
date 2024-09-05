greet=input("enter greeting: ")
greet=greet.lower()
greet=greet.strip()
c1=greet.startswith("hello")
c2=greet.startswith("h")

if c1:
    print("$0")
elif (c2 and not c1):
    print("$20")
else:
    print("$100")
