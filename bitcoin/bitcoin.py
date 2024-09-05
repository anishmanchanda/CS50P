import requests
import sys
while True:
    try:
        if len(sys.argv)<2:
            print("Missing command-line argument")
            break
        else:
            n=float(sys.argv[1])
            break
    except TypeError:
        print('Command-line argument is not a number')

r=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
d=r.json()
for k in d:
    if k=='bpi':
        d1=d[k]
        for k1 in d1:
            if k1=='USD':
                d2=d1[k1]
                for k2 in d2:
                    if k2=='rate_float':
                        rate=d2[k2]
                        break

cost=n*rate
cost=round(cost,4)
cost=str(cost)
l=cost.split('.')
whole=l[0]
whole=int(whole)
whole=f"{whole:,}"
print("$"+whole+'.'+l[1])
sys.exit
