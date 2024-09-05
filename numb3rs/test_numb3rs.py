from numb3rs import validate
def test_validate():
    assert validate("255.255.255.255")==True
    assert validate("512.512.512.512")==False
    assert validate("1.2.3.1000")==False
    assert validate("car")==False
    assert validate("000.000.000.000")==True
    assert validate("0.0.0.0") == True
    assert validate("0.256.256.256") == False
if __name__=="__main__":
    test_validate()
