import sys
def main():
    checksys()
    try:
        f=open(sys.argv[1],'r')
        lines=f.readlines()
        f.close()
    except FileNotFoundError:
        sys.exit("File does not exist")
    count=0
    for line in lines:
        if checkline(line)==True:
            count+=1
    print(count)

def checksys():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def checkline(line):
    if line.lstrip().startswith("#"):
        return False
    if line.isspace():
        return False
    return True

if __name__=="__main__":
    main()
