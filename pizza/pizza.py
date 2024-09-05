import csv,sys
from tabulate import tabulate
def main():
    checksys()
    try:
        f=open(sys.argv[1],'r')
        data=csv.reader(f)
        i=0
        table=[]
        for line in data:
            if i!=0:
                table.append(line)
            else:
                header=line
            i+=1

        print(tabulate(table,headers=header,tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

def checksys():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__=="__main__":
    main()
