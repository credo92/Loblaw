import pandas as pd
import cv2
from termcolor import colored
import time


def start_calculating_score_elapsed(images_csv_df):
    score_list, elapsed_list = get_score_elapsed_info_lists(images_csv_df)
    output_dict = {
        "Image1": images_csv_df['image1'].tolist(),
        "Image2": images_csv_df['image2'].tolist(),
        "similar": score_list,
        "elapsed": elapsed_list
    }
    output_df = pd.DataFrame(output_dict)
    return output_df


def get_score_elapsed_info_lists(images_csv_df):
    score_list = []
    elapsed_list = []

    for index, row in images_csv_df.iterrows():
        score_elapsed_list = calculate_similarity_sift_score_elapsed(row)
        print(colored(score_elapsed_list, color='blue'))
        score_list.append(score_elapsed_list[0])
        elapsed_list.append(score_elapsed_list[1])

    return score_list, elapsed_list


def calculate_similarity_sift_score_elapsed(row):
    start_time = time.time()
    orb = cv2.ORB_create()
    img_1 = cv2.imread(row['image1'])
    img_2 = cv2.imread(row['image2'])
    if img_1.shape != img_2.shape:
        score = 1
        elapsed_time = round(time.time() - start_time, 2)
        return [score, elapsed_time]

    key_points_1, descriptors_1 = orb.detectAndCompute(img_1, None)
    key_points_2, descriptors_2 = orb.detectAndCompute(img_2, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors_1, descriptors_2)
    similar_regions = [i for i in matches if i.distance < 80]  # D.lowe paper

    if len(matches) == 0:
        score = 1
        elapsed_time = round(time.time() - start_time, 2)
        return [score, elapsed_time]
    else:
        score = round(1-len(similar_regions) / len(matches), 2)
        elapsed_time = round(time.time() - start_time, 2)
        return [score, elapsed_time]
