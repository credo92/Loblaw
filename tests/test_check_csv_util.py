import pandas as pd
from os import getcwd
from utils import is_csv_good

# good test data
good_test_dict = {
              'image1': [getcwd()+'/resources/Image1.png'],
              'image2': [getcwd()+'/resources/Image2.png']
             }

# bad test data
bad_test_dict = {
              'image1': [getcwd()+'/resources/Image1-ERR.png'],
              'image2': [getcwd()+'/resources/Image2-ERR.png']
             }

# convert to df
good_test_data_df = pd.DataFrame(good_test_dict)
bad_test_data_df = pd.DataFrame(bad_test_dict)

is_good = is_csv_good(good_test_data_df)
is_bad = is_csv_good(bad_test_data_df)


def test_is_csv_good():
    assert is_good is True


def test_is_csv_bad():
    assert is_bad is False




