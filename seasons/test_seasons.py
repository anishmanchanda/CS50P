import pytest
import datetime
from seasons import minutes
today=datetime.date.today()
def test_seasons():

    assert minutes(today)=="zero"

if __name__=="__main__":
    test_seasons()
