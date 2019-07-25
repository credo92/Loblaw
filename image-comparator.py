import pandas as pd
import sys
import time
from os import path, getcwd, name
from termcolor import colored
from colorama import init
from utils import is_csv_good, start_calculating_score_elapsed


if name == 'nt':
    init()


def init(input_file_name):
    if not path.exists(input_file_name):
        print(colored('ERR!! Path doesnt exists : '+input_file_name, 'red'))
        return

    output_file_name = getcwd()+'/results.csv'
    images_csv_df = pd.read_csv(input_file_name)

    if is_csv_good(images_csv_df):
        output_df = start_calculating_score_elapsed(images_csv_df)
        output_df.to_csv(output_file_name, sep=",", index=False)
        print(colored('score and elapsed results written to '+output_file_name, 'green'))

    else:
        err_input_file_name = getcwd() + '/dumps/-Test' + str(int(time.time())) + '.csv'
        images_csv_df.to_csv(err_input_file_name, sep=",", index=False)
        print(colored("ERRs in CSV! Incorrect File paths labeled in " + err_input_file_name, 'red'))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print(colored('ERR! Please enter a path | ex: python image-comparator.py <CSV_FILE_PATH>', 'red'))
    else:
        init(str(sys.argv[1]))
