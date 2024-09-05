import datetime
import sys
import inflect
p = inflect.engine()
def main():

    date=input("Date of Birth: ")
    if date.count('-')!=2:
        sys.exit("Invalid date")
    else:
        datelis=date.split('-')
        yr=int(datelis[0])
        mnth=int(datelis[1])
        day=int(datelis[2])
    dt2=datetime.date(yr,mnth,day)
    op=minutes(dt2)
    print(op.capitalize(),"minutes")

def minutes(dob):
    dt=datetime.date.today()
    if dob>dt:
        days=(dob-dt).days
    else:
        days=(dt-dob).days
    mins=days*24*60
    words = p.number_to_words(mins,andword="")
    return words
if __name__=="__main__":
    main()
