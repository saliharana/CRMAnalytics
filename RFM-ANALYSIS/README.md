# Project Overview

This project focuses on customer segmentation for the e-commerce company FLO using the RFM (Recency, Frequency, Monetary) analysis approach. The key tasks involved in this project are:

1. **Understanding and Preparing the Data**:
   - Reading the customer data from the `flo_data_20K.csv` file
   - Exploring the data to understand the variables, descriptive statistics, missing values, and data types
   - Creating new variables to calculate the total number of purchases and total spending for each customer
   - Converting date-related variables to the appropriate data type
   - Examining the distribution of customers, average purchases, and average expenditure across sales channels
   - Identifying the top 10 customers by revenue and order count

2. **Calculating RFM Metrics**:
   - Calculating the Recency, Frequency, and Monetary (RFM) metrics for each customer

3. **Calculating RF and RFM Scores**:
   - Calculating the RF (Recency and Frequency) and RFM scores for each customer

4. **Defining RF Segments**:
   - Defining customer segments based on the RF scores

5. **Actionable Insights**:
   - Examining the RFM metric averages for each segment
   - Identifying two target customer profiles:
     - Customers who are loyal, spend over 250 TL, and are interested in women's shoes
     - Customers who are good past customers but have not shopped recently, dormant customers, and new customers interested in relevant categories
   - Saving the customer IDs for the target profiles to CSV files
