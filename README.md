# Fannie Mae Loan Default Prediction

## Overview:
The goal of this project is to analyse the Fannie Mae Single-Family Loan Data.

What question am I trying to answer?
The main question -

1. Predict if a loan will be foreclosed on in the future.

### Where did the data come from?
All of the data came from Fannie Mae's datahousing website: https://capitalmarkets.fanniemae.com/tools-applications/data-dynamics
The data is broken up by quarters from 2000 through 2020. 

### How was the data sampled?
Data from 2017 to 2019 was used for this project.

### The data pipeline

1. Data Acquisition: Data downloadeed from Fannie Mae in .csv format.
2. Explatoratory Data Analysis:
  - Getting a better understanding of data
  - Identifying various data patterns
  - Getting a better understanding of the problem statement
3. Data PreProcessing: 
  - Identify missing values and either eiliminate those rows or fill them in
  - Determine if there are inconsisten values
  - Identify duplicated values
  - Feature aggregation if needed
  - Feature encoding
4. Save our clean file and get ready to start modeling.
