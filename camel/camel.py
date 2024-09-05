camel=input("enter name in camel case: ")
snake=""
length=len(camel)
for i in range(length):
    char=camel[i]
    if char.isupper():
        snake=snake+"_"+char.lower()
    else:
        snake=snake+char
print(snake)
