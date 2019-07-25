from os import path


def is_csv_good(images_csv_df):
    is_good = True

    for index, row in images_csv_df.iterrows():
        if not path.exists(row['image1']) or not path.exists(row['image2']):
            if not path.exists(row['image1']):
                row['image1'] = row['image1'] + ' ERR! File Path doesnt exists'
            if not path.exists(row['image2']):
                row['image2'] = row['image2'] + ' ERR! File Path doesnt exists'
            is_good = False

    return is_good
