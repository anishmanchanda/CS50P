import random
import sys
while True:
    lvl=input("Level: ")
    try:
        lvl=int(lvl)
        if lvl<1:
            continue
        break
    except:
        continue

num=random.randrange(1,lvl+1)
while True:
    guess=input("Guess: ")
    try:
        guess=int(guess)
    except (EOFError,NameError):
        break
    except:
        continue
    else:
        if guess>num:
            print("Too large!")
            continue
        elif guess<num:
            print("Too small!")
            continue
        else:
            sys.exit("Just right!")
