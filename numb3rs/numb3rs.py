import re
import sys
def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit()

def validate(ip):
    nums=ip.split('.')
    if len(nums)!=4:
        return False
    try:

        if not(int(nums[0])>=0 and int(nums[0])<=255):
            return False
        elif not(int(nums[1])>=0 and int(nums[1])<=255):
            return False
        elif not(int(nums[2])>=0 and int(nums[2])<=255):
            return False
        elif not(int(nums[3])>=0 and int(nums[3])<=255):
            return False
        else:
            return True
    except:
        return False



if __name__=="__main__":
    main()

