import random
def main():
    lvl=get_level()
    count=1
    ecount=0
    score=0
    for i in range (10):
        x,y=generate_integer(lvl)
        s=x+y
        attempts=0
        while attempts<3:
            try:
                inp = int(input(f"{x} + {y} = "))
                if s==inp:
                    score+=1
                    break
                else:
                    print("EEE")
                    attempts+=1
            except ValueError:
                attempts+=1
        if attempts==3:
            print(f"{x} + {y} = {s}")
    print("Score:",score)
def get_level():
    while True:
        try:
            n=int(input("Level: "))
            if n not in [1,2,3]:
                continue
            else:
                break
        except (EOFError,NameError):
            break
        except:
            continue
    return n
def generate_integer(level):
    if level==1:
        a=random.randint(0,9)
        b=random.randint(0,9)
        return a,b
    elif level==2:
        a=random.randint(10,99)
        b=random.randint(10,99)
        return a,b
    elif level==3:
        a=random.randint(100,999)
        b=random.randint(100,999)
        return a,b
    else:
        print("cryin")
        return 1,2

if __name__ == "__main__":
    main()
