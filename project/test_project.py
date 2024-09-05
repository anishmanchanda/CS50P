from project import get_requests, convert_to_usd,convert_to_currout

def main():
    test_get_requests()
    test_convert_to_usd()
    test_convert_to_curout()


def test_get_requests():
    assert type(get_requests("https://api.exchangerate-api.com/v4/latest/USD"))==dict
    assert type(get_requests("https://api.coindesk.com/v1/bpi/c`  urrentprice.json"))==dict

def test_convert_to_usd():
    assert convert_to_usd('USD')==1
    assert convert_to_usd('INR')==83.93
    assert convert_to_usd('EUR')==0.904
    assert convert_to_usd('CHF')==0.851

def test_convert_to_currout():
    assert convert_to_currout("USD")==1
    assert convert_to_usd('INR')==83.93
    assert convert_to_usd('EUR')==0.904
    assert convert_to_usd('CHF')==0.851

if __name__=="__main__":
    main()
