def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    c1=False
    c2=False
    c3=False
    length=len(s)
    if (2<=length<=6):
        c2=True
    if(c2):
        firstwo=s[0]+s[1]
        if firstwo.isalpha():
            c1=True
    #c3 and c4 and c5
    c4=True
    c5=True
    nstr=""
    for i in range(length):
        if (s[i] in['.',' ','!','?']):
            c4=False
        if s[i].isnumeric():
            if s[i]=='0':
                c5=False
            for j in range(i,length):
                nstr=nstr+s[j]
            break
    if nstr.isnumeric():
        c3=True
    if(c1 and c2 and c3 and c4 and c5):
        return True
    else:
        return False
if __name__=="__main__":
    main()
