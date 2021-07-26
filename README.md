# Fannie Mae Loan Default Prediction





[GithubPages](https://raulcpena.github.io/classification_analysis/)

## Overview:
The goal of this project is to analyze the Fannie Mae Single-Family Loan Data.

What question am I trying to answer?
The main question -

1. Predict if a loan will be foreclosed on in the future.

### Where did the data come from?
All of the data came from Fannie Mae's data housing [website]( https://capitalmarkets.fanniemae.com/tools-applications/data-dynamics)
The data is broken up by quarters from 2000 through 2020. 

### How was the data sampled?
Data from 2017 to 2019 was used for this project.

### The data pipeline

1. Data Acquisition: Data downloaded from Fannie Mae in .csv format.
2. Exploratory Data Analysis:
   * Getting a better understanding of data
   * Identifying various data patterns
   * Getting a better understanding of the problem statement

3. Data Preprocessing: 
   * Identify missing values and either eliminate those rows or fill them in
   * Determine if there are inconsistent values
   * Identify duplicated values
   * Feature aggregation if needed
   * Feature encoding

4. Save our clean file and get ready to start modeling.

# Information about the original data

Originally, the downloaded data had **108** columns however, most of them were implemented in 2017 and only recently started reporting data as of June 2020 so at the time of this capstone they were not used.

### Pre-Processing the data

**Here we have a null breakdown for all the columns:**

- Loan Identifier: total of 0 nulls- 0.0%
- Monthly Reporting Period: total of 0 nulls- 0.0%
- Original Interest Rate: total of **41** nulls- 0.0%
- Current Interest Rate: total of 0 nulls- 0.0%
- Original UPB: total of **41** nulls- 0.0%
- Original Loan Term: total of **41** nulls- 0.0%
- Origination Date: total of **41** nulls- 0.0%
- Loan Age: total of 0 nulls- 0.0%
- Maturity Date: total of 0 nulls- 0.0%
- Original Loan to Value Ratio (LTV): total of **41** nulls- 0.0%
- Number of Borrowers: total of **41** nulls- 0.0%
- Debt-To-Income (DTI): total of **668** nulls- 0.01%
- Borrower Credit Score at Origination: total of **6114** nulls- 0.07%
- Co-Borrower Credit Score at Origination: total of **4373161** nulls- 52.79%
- First Time Home Buyer Indicator: total of **41** nulls- 0.0%
- Amortization Type: total of 0 nulls- 0.0%
- Current Loan Delinquency Status: total of 0 nulls- 0.0%
- Modification Flag: total of 0 nulls- 0.0%
- Foreclosure Date: total of **8279621** nulls- 99.95%
- Home Ready Program Indicator: total of 0 nulls- 0.0%
- High Balance Loan Indicator: total of 0 nulls- 0.0%
- Borrower Assistance Plan: total of 0 nulls- 0.0%
- Minimum Credit Score: total of **4185** nulls- 0.05%

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
