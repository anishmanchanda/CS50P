def shorten(str):
    nstr=""
    length = len(str)
    lis=['A','E','I','O','U','a','e','i','o','u']
    for i in range(length):
        if(str[i] not in lis):
            nstr=nstr+str[i]
    return nstr

if __name__=="__main__":
    s=input("enter string: ")
    print(shorten(s))
