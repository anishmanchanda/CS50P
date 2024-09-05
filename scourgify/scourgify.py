import csv,sys
def main():
    checksys()
    try:
        f1=open(sys.argv[1],'r')
        data=csv.reader(f1)
        i=0
        datalis=[]
        for rec in data:
            if i!=0:
                datalis.append(rec)
            i+=1

        #seperating old data
        newdata=[["first","last","house"]]
        for rec in datalis:
            name=rec[0]
            house=rec[1]
            last,first=name.split(", ")
            newrec=[first,last,house]
            newdata.append(newrec)

        f2=open(sys.argv[2],'w',newline='')
        csvwriter=csv.writer(f2)
        csvwriter.writerows(newdata)
        f1.close()
        f2.close()

    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")

def checksys():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
if __name__=="__main__":
    main()
