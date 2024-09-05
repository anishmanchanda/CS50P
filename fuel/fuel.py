def inputfn():
    while True:
        try:
            fuel=input("enter fuel level(fraction): ")
            x,y=fuel.split('/')
            x=int(x)
            y=int(y)
            lvl=(x/y)*100
            lvl=round(lvl)
            if lvl>100:
                pass
            else:
                return lvl
        except(ValueError,ZeroDivisionError):
            pass
def main():
    flevel=inputfn()
    if flevel<=1:
        print("E")
    elif flevel>=99:
        print("F")
    else:
        print(str(flevel)+"%")

main()
