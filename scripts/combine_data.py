import pandas as pd
import os

def concat_files(data_dir, outfile_name):
    data_files = os.listdir(data_dir)
    df_list = []
    for file in data_files:
        df = pd.read_csv(data_dir + file)
        df_list.append(df)

    combined = pd.concat(df_list, axis=0)
    outfile = open(outfile_name, 'w')
    combined.to_csv(outfile)
    outfile.close()

if __name__ == '__main__':
    concat_files('./data/condensed/', './combined_data.csv')