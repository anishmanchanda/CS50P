from twttr import shorten

def test_twttr():
    assert shorten("twitter")=="twttr"
    assert shorten("What's your name?")=="Wht's yr nm?"
    assert shorten("CS50")=="CS50"
    assert shorten("PYTHON")=="PYTHN"
if __name__=="__main__":
    test_twttr()
