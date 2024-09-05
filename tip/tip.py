def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
   length=len(d)
   nd=""
   for i in range(1,length):
       nd=nd+d[i]
   nd=float(nd)
   return nd


def percent_to_float(p):
    length=len(p)
    np=""
    for i in range(0,length-1):
        np=np+p[i]
    np=float(np)
    np=np/100
    return np
main()
