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

# Information about the data

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

