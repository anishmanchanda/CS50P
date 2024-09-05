import requests
from pyfiglet import Figlet


def main():
    figletfunc("CURRENCY CONVERTER")
    currin = input("ENTER INPUT CURRENCY CODE(INR/EUR/AUD): ")
    amt = int(input("ENTER AMOUNT: "))
    val1 = convert_to_usd(currin.upper())
    usdval = amt/val1
    usdval = round(usdval, 2)
    currout = input("ENTER OUTPUT CURRENCY CODE(USD/CAD/AED): ")
    val2 = convert_to_currout(currout.upper())
    outamt = val2*usdval
    outamt = round(outamt, 2)
    print(outamt)


# function to print project title in FIGlet font
def figletfunc(string):
    figlet = Figlet()
    figlet.setFont(font="standard")
    print(f" \n{figlet.renderText(string)}")


# function to get currency rate exchangedata in
# dictionary format using requests module from provided url
def get_requests(url):
    r = requests.get(url)
    d = r.json()
    return d


# function to convert input currency into USD(considered as primary currency)
def convert_to_usd(inp):

    D = get_requests('https://api.exchangerate-api.com/v4/latest/USD')
    for k in D:
        if k == 'rates':
            dmain = D[k]
    val1 = dmain[inp]
    return val1

# function to finally convert USD to output currency
def convert_to_currout(out):
    D = get_requests('https://api.exchangerate-api.com/v4/latest/USD')
    for k in D:
        if k == 'rates':
            dmain = D[k]
    if out == 'USD':
        return 1
    else:
        val2 = dmain[out]
        return val2


if __name__ == "__main__":
    main()
