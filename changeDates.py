def change_dates(df):

    df[['Monthly Reporting Period',
        'Origination Date', 
        'Maturity Date']]  = df[['Monthly Reporting Period',
                                    'Origination Date', 
                                    'Maturity Date']].ffill()

    df[['Monthly Reporting Period',
        'Origination Date', 
        'Maturity Date', 
        'Foreclosure Date']]  = df[['Monthly Reporting Period',
                                    'Origination Date', 
                                    'Maturity Date', 
                                    'Foreclosure Date']].astype('str')

    df['Origination Date'] = df['Origination Date'].str[:-2]
    df['Maturity Date'] = df['Maturity Date'].str[:-2]


    df['Monthly Reporting Period'] = pd.to_datetime(df['Monthly Reporting Period'],format='%m%Y')

    df['Origination Date'] = pd.to_datetime(df['Origination Date'],format='%m%Y')

    df['Maturity Date'] = pd.to_datetime(df['Maturity Date'], format='%m%Y')