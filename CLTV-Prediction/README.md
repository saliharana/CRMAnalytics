# Customer Lifetime Value (CLTV) Analysis

## Overview
This project performs a comprehensive analysis of customer lifetime value (CLTV) for a dataset of 20,000 customers. The main steps of the analysis are:

1. Data Preparation
2. Creating the CLTV Data Structure
3. Establishment of BG/NBD, Gamma-Gamma Models, Calculation of CLTV
4. Creating Segments According to CLTV

## Data Preparation
1. Loaded the `flo_data_20K.csv` dataset and created a copy of the dataframe.
2. Defined functions to identify and handle outliers in the data.
3. Handled the outliers in specific columns, such as `order_num_total_ever_online`, `order_num_total_ever_offline`, `customer_value_total_ever_offline`, and `customer_value_total_ever_online`.
4. Created new variables to represent the total number of purchases and total spending for each customer, considering both online and offline channels.
5. Converted date-related variables to the appropriate date format.

## Creating the CLTV Data Structure
1. Determined the analysis date as 2 days after the date of the last purchase in the dataset.
2. Created a new dataframe `cltv` containing the variables `customer_id`, `recency_cltv_weekly`, `T_weekly`, `frequency`, and `monetary_cltv_avg`.
3. The monetary value was calculated as the average value per purchase, and the recency and tenure values were expressed in weekly terms.

## Establishment of BG/NBD, Gamma-Gamma Models, Calculation of CLTV
1. Fitted the BG/NBD (Beta-Geometric/NBD) model to the data.
2. Estimated the expected purchases from customers within 3 months and 6 months, and added the results to the `cltv` dataframe.
3. Fitted the Gamma-Gamma model to the data.
4. Estimated the average value the customers will leave and added it to the `cltv` dataframe.
5. Calculated the 6-month CLTV and added it to the `cltv` dataframe.
6. Identified the 20 customers with the highest CLTV value.

## Creating Segments According to CLTV
1. Divided all customers into 4 groups (segments) based on their 6-month CLTV.
2. Added the segment information as a new column `cltv_segment` to the dataframe.
3. Provided short action recommendations for the management for the next 6 months, focusing on 2 of the 4 segments.

This analysis provides valuable insights into the customer lifetime value for the given dataset, enabling better-informed business decisions and targeted customer retention strategies.
