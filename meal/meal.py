def main():
    strtime=input("enter time: ")
    time=convert(strtime)
    if (time>=7 and time <=8 ):
        print("breakfast time")
    elif(time >=12 and time <=13):
        print("lunch time")
    elif (time >=18 and time <=19):
        print("dinner time")

def convert(strtime):
    lis=strtime.split(':')
    hour=int(lis[0])
    min=int(lis[1])

    minutes=min/60
    time=hour+minutes
    time=float(time)
    return time

if __name__ == "__main__":
    main()
