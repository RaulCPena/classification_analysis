import pandas as pd
import numpy as np
import os
from col_discard import col_discard
from headers import col_headers

def import_file(filename):
    '''
    takes a file name to 1 file of Fannie Mae data
    relative path is hard coded in data_path and extracted_data_path
    returns a dataframe containing 1 file worth of data
    '''
    data_path = './data/'
    print(f'Loading {filename}')
    
    return pd.read_csv(data_path + filename, delimiter='|', names=col_headers, usecols = [i for i in col_headers if i not in col_discard])


def impute_nulls(df):
    print('Imputing has started!!')

    df['Home Ready Program Indicator'].fillna('N', inplace=True)
    df['Current Loan Delinquency Status'] = df['Current Loan Delinquency Status'].replace('XX', np.NaN)
    df['Borrower Assistance Plan'].fillna('7', inplace=True)
    
    df[[
    'Maturity Date', 
    'Current Loan Delinquency Status',
    'Current Interest Rate', 
    'Loan Age',
    'Modification Flag']]  = df[[
                'Maturity Date', 
                'Current Loan Delinquency Status',
                'Current Interest Rate', 
                'Loan Age',
    'Modification Flag']].ffill()
    print('File Imputed!')
    return df



if (__name__ == '__main__'):
    print('Saving File......')
    data_files = os.listdir('./data/')
    df_list = []
    for f in data_files:
        df = import_file(f)
        impute_nulls(df)

        condensed = df.drop_duplicates(subset=['Loan Identifier'], keep='last', ignore_index=True)
        df_list.append(condensed)
        print(f'{f} Finished Loading')
        outfile = open('data/condensed/' + f, 'w')
        condensed.to_csv(outfile)
        outfile.close()
        print('Saved File!!!')
    
   
 




