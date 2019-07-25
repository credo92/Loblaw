from os import getcwd
from utils import get_score_elapsed_info_lists, calculate_similarity_sift_score_elapsed
import pandas as pd

# good test data
test_dict = {
              'image1': [getcwd()+'/resources/Image1.png'],
              'image2': [getcwd()+'/resources/Image2.png']
             }

test_data_df = pd.DataFrame(test_dict)

score_list, elapsed_list = get_score_elapsed_info_lists(test_data_df)
score_elapsed_list = calculate_similarity_sift_score_elapsed(test_data_df.iloc[0, :])


def test_get_score_elapsed_info_lists():
    assert len(score_list) is 1 and score_list[0] == 0.0


def test_calculate_similarity_sift_score_elapsed():
    assert score_elapsed_list[0] == 0.0
