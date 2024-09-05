from plates import is_valid

def test_plates():
    assert is_valid("CS50")==True
    assert is_valid("CS05")==False
    assert is_valid("CS50P")==False
    assert is_valid("PI3.14")==False
    assert is_valid("H")==False
    assert is_valid("OUTATIME")==False
    assert is_valid("1CS50")==False
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid(" 2") == False


if __name__=="__main__":
    test_plates()

