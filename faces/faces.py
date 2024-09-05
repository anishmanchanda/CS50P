def convert(str):
    str=str.replace(":)",'🙂')
    str=str.replace(":(",'🙁')
    print(str)

s=input("enter string: ")
convert(s)
