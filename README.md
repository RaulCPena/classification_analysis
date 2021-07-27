# Fannie Mae Loan Default Prediction

[GithubPages](https://raulcpena.github.io/classification_analysis/)

## Overview:
The goal of this project is to analyze the Fannie Mae Single-Family Loan Data.

What question am I trying to answer?
The main question -

1. Predict if a loan will be foreclosed on in the future.

## Where did the data come from?
All of the data came from Fannie Mae's data housing [website]( https://capitalmarkets.fanniemae.com/tools-applications/data-dynamics)
The data is broken up by quarters from 2000 through 2020. 

## How was the data sampled?
Data from 2017 to 2019 was used for this project.

## The data pipeline

1. Data Acquisition: Data downloaded from Fannie Mae in .csv format.
2. Data Preprocessing: 
   * Identify missing values and either eliminate those rows or imputation
   * Determine if there are inconsistent values
   * Identify duplicated values
   * Feature aggregation if needed
   * Feature encoding
3. Exploratory Data Analysis:
   * Perform the initial investigations so to discover patterns, spot anomalies, test hypothesis and check assumptions, using visualizations
4. Save our clean file and get ready to start modeling.

# Information about the original data

Originally, Fannie Mae has all of their data in csv format and the total size is roughly **370gb**. Each quarter starting from 2000 has about **104million rows** of data, so all together that would have required a massive amount of computing power. I decided on using data from 2016 through 2019 for my project. 

The compiled data had **108** columns however, most of them were added in 2017 and would not start reporting reporting data until June 2020, so I decided not use keep those rows for this project.

# Pre-Processing the data

| Null breakdown for all the columns:                          |
| :----------------------------------------------------------- |
| Loan Identifier: total of 0 nulls- 0.0%                      |
| Monthly Reporting Period: total of 0 nulls- 0.0%             |
| Original Interest Rate: total of **41** nulls- 0.0%          |
| Current Interest Rate: total of 0 nulls- 0.0%                |
| Original UPB: total of **41** nulls- 0.0%                    |
| Original Loan Term: total of **41** nulls- 0.0%              |
| Origination Date: total of **41** nulls- 0.0%                |
| Loan Age: total of 0 nulls- 0.0%                             |
| Maturity Date: total of 0 nulls- 0.0%                        |
| Original Loan to Value Ratio (LTV): total of **41** nulls- 0.0% |
| Number of Borrowers: total of **41** nulls- 0.0%             |
| Debt-To-Income (DTI): total of **668** nulls- 0.01%          |
| Borrower Credit Score at Origination: total of **6114** nulls- 0.07% |
| Co-Borrower Credit Score at Origination: total of **4373161** nulls- 52.79% |
| First Time Home Buyer Indicator: total of **41** nulls- 0.0% |
| Amortization Type: total of 0 nulls- 0.0%                    |
| Current Loan Delinquency Status: total of 0 nulls- 0.0%      |
| Modification Flag: total of 0 nulls- 0.0%                    |
| Foreclosure Date: total of **8279621** nulls- 99.95%         |
| Home Ready Program Indicator: total of 0 nulls- 0.0%         |
| High Balance Loan Indicator: total of 0 nulls- 0.0%          |
| Borrower Assistance Plan: total of 0 nulls- 0.0%             |
| Minimum Credit Score: total of **4185** nulls- 0.05%         |

You can see that **`Foreclosure`**  has **99.95%** missing data and **`Co-Borrower Credit Score at Origination`** has **52.79%** missing. 

**Data Table**

|  #   |                 Column                  |  Dtype  |
| :--: | :-------------------------------------: | :-----: |
|  0   |             Loan Identifier             |  int64  |
|  1   |        Monthly Reporting Period         |  int64  |
|  2   |         Original Interest Rate          | float64 |
|  3   |          Current Interest Rate          | float64 |
|  4   |              Original UPB               | float64 |
|  5   |           Original Loan Term            | float64 |
|  6   |            Origination Date             | float64 |
|  7   |                Loan Age                 | float64 |
|  8   |              Maturity Date              | float64 |
|  9   |   Original Loan to Value Ratio (LTV)    | float64 |
|  10  |           Number of Borrowers           | float64 |
|  11  |          Debt-To-Income (DTI)           | float64 |
|  12  |  Borrower Credit Score at Origination   | float64 |
|  13  | Co-Borrower Credit Score at Origination | float64 |
|  14  |     First Time Home Buyer Indicator     | object  |
|  15  |            Amortization Type            | object  |
|  16  |     Current Loan Delinquency Status     |  int64  |
|  17  |            Modification Flag            | object  |
|  18  |            Foreclosure Date             | float64 |
|  19  |      Home Ready Program Indicator       | object  |
|  20  |       High Balance Loan Indicator       | object  |
|  21  |        Borrower Assistance Plan         | object  |

## Data Manipulation

The following was completed:

1. Created a new column called **`Minimum Credit Score`** by taking comparing the following two columns:

   - Borrow Credit Score at Origination
   - Co-Borrower Credit Score at Origination

   Fannie Mae provided guidelines on creating new features and with this specific one I had to look at both columns and if anyone was missing I would take the `mean` of that column and enter it for the value, however should both columns have a value only the lowest of the two was kept. 

2. Feature **`On Assistance PLan`** was mapped using the following code snippet:

   ```python
   # F T R to be on plan
   def check_plan(x):
       if x in ['F', 'T', 'R']:
           return 1
       return 0
   ```

3. Dropped the following columns after creating new ones `'Borrower Credit Score at Origination', 'Co-Borrower Credit Score at Origination',  'Borrower Assistance Plan'`

4. Set new conditions to fill in the null values of **`Foreclosed`** using the following methods:

   ```python
   # df['Current Loan Delinquency Status'] >= 4 and not on df['On Assistance Plan'], foreclosed = 1 (True)
   # create a list of our conditions
   conditions = [
       (df['Current Loan Delinquency Status'] >= 4) &
       (df['On Assistance Plan'] == 0), 
       (df['Foreclosure Date'].notnull())
       ]
   # create a list of the values we want to assign for each condition
   values = [1,1]
   # create a new column and use np.select to assign values to it using our lists as arguments
   df['Foreclosed'] = np.select(conditions, values)
   ```

   with the final output of 

   ```python
   0    8260646
   1      22843
   Name: Foreclosed, dtype: int64
   ```

5. The feature columns  that were dates needed to be strings so we could format them correctly:

   ```Python
   df[['Monthly Reporting Period',
           'Origination Date', 
           'Maturity Date']]  = df[['Monthly Reporting Period',
                                       'Origination Date', 
                                       'Maturity Date']].astype('str')
   ```

   After imputation from float to string the string retained its '.' ,  so to resolve this a few cells were created:

   ​		**Origination Date**

   ```python
   # new data frame with split value columns
   df['Origination Date'] = df['Origination Date'].str.split(".", n = 1, expand = True)
   
   df['Origination Date'] = pd.to_datetime(df['Origination Date'],format='%m%Y')
   ```

   ​		**Maturity Date**

   ```python
   # new data frame with split value columns
   df['Maturity Date'] = df['Maturity Date'].str.split(".", n = 1, expand = True)
   
   df['Maturity Date'] = pd.to_datetime(df['Maturity Date'], format='%m%Y')
   ```

   ​		**Monthly Reporting Period**

   ```python
   df['Monthly Reporting Period'] = pd.to_datetime(df['Monthly Reporting Period'],format='%m%Y')
   ```

6. Finally, dropped the following null values within these columns:

   ```Python
   Original Interest Rate: total of 41 nulls- 0.0%
   Original UPB: total of 41 nulls- 0.0%
   Original Loan Term: total of 41 nulls- 0.0%
   Origination Date: total of 41 nulls- 0.0%
   Original Loan to Value Ratio (LTV): total of 41 nulls- 0.0%
   Number of Borrowers: total of 41 nulls- 0.0%
   Debt-To-Income (DTI): total of 668 nulls- 0.01%
   First Time Home Buyer Indicator: total of 41 nulls- 0.0%
   Minimum Credit Score: total of 4185 nulls- 0.05%
   Foreclosed: total of 0 nulls- 0.0%
   ```

   Our final shape of the data **(8,278,657, 19)**

# Exploratory Data Analysis

Here is a look at our final data information table:

|  #   |               Column               |     Dtype      |
| :--: | :--------------------------------: | :------------: |
|  0   |          Loan Identifier           |     int64      |
|  1   |      Monthly Reporting Period      | datetime64[ns] |
|  2   |       Current Interest Rate        |    float64     |
|  3   |            Original UPB            |     int64      |
|  4   |         Original Loan Term         |     int64      |
|  5   |          Origination Date          | datetime64[ns] |
|  6   |              Loan Age              |     int64      |
|  7   |           Maturity Date            | datetime64[ns] |
|  8   | Original Loan to Value Ratio (LTV) |     int64      |
|  9   |        Number of Borrowers         |     int64      |
|  10  |        Debt-To-Income (DTI)        |     int64      |
|  11  |  First Time Home Buyer Indicator   |     int64      |
|  12  |         Modification Flag          |     int64      |
|  13  |    Home Ready Program Indicator    |     int64      |
|  14  |    High Balance Loan Indicator     |     int64      |
|  15  |        Minimum Credit Score        |     int64      |
|  16  |             Foreclosed             |     int64      |

One major concern was the imbalance within our target feature **Foreclosed** 

![distro_of_target](../classification_analysis\Notebook_images\distro_of_target.png)

