# Customer Segmentation with RFM

## Business Problem
FLO wants to segment its customers and determine marketing strategies based on these segments. For this purpose, customer behavior will be defined and groups will be formed according to these behavioral clusters.

## Data Set Story
The data set consists of information obtained from the past shopping behavior of customers who made their last purchases in 2020 - 2021 as OmniChannel (both online and offline shopping).

## Tasks
1. **Understanding and Preparing the Data**:
   - Loaded the `flo_data_20K.csv` dataset and created a copy of the dataframe
   - Defined functions to identify and handle outliers in the data
   - Handled the outliers in specific columns
   - Created new variables to represent the total number of purchases and total spending for each customer
   - Converted date-related variables to the appropriate date format

2. **Creating the CLTV Data Structure**:
   - Determined the analysis date as 2 days after the date of the last purchase in the dataset
   - Created a new dataframe `cltv` containing the variables `customer_id`, `recency_cltv_weekly`, `T_weekly`, `frequency`, and `monetary_cltv_avg`
   - Calculated the monetary value as the average value per purchase, and the recency and tenure values were expressed in weekly terms

3. **Establishment of BG/NBD, Gamma-Gamma Models, Calculation of CLTV**:
   - Fitted the BG/NBD (Betag-Geometric/NBD) model to the data
   - Estimated the expected purchases from customers within 3 months and 6 months, and added the results to the `cltv` dataframe
   - Fitted the Gamma-Gamma model to the data
   - Estimated the average value the customers will leave and added it to the `cltv` dataframe
   - Calculated the 6-month CLTV and added it to the `cltv` dataframe
   - Identified the 20 customers with the highest CLTV value

4. **Creating Segments According to CLTV**:
   - Divided all customers into 4 groups (segments) based on their 6-month CLTV
   - Added the segment information as a new column `cltv_segment` to the dataframe
   - Provided short action recommendations for the management for the next 6 months, focusing on 2 of the 4 segments
