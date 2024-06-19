Data Preparation:
Loaded the flo_data_20K.csv dataset and created a copy of the dataframe.
Defined functions to identify and handle outliers in the data.
Handled the outliers in specific columns, such as order_num_total_ever_online, order_num_total_ever_offline, customer_value_total_ever_offline, and customer_value_total_ever_online.
Created new variables to represent the total number of purchases and total spending for each customer, considering both online and offline channels.
Converted date-related variables to the appropriate date format.
Creating the CLTV Data Structure:
Determined the analysis date as 2 days after the date of the last purchase in the dataset.
Created a new dataframe cltv containing the variables customer_id, recency_cltv_weekly, T_weekly, frequency, and monetary_cltv_avg.
The monetary value was calculated as the average value per purchase, and the recency and tenure values were expressed in weekly terms.
Establishment of BG/NBD, Gamma-Gamma Models, Calculation of CLTV:
Fitted the BG/NBD (Betag-Geometric/NBD) model to the data.
Estimated the expected purchases from customers within 3 months and 6 months, and added the results to the cltv dataframe.
Fitted the Gamma-Gamma model to the data.
Estimated the average value the customers will leave and added it to the cltv dataframe.
Calculated the 6-month CLTV and added it to the cltv dataframe.
Identified the 20 customers with the highest CLTV value.
Creating Segments According to CLTV:
Divided all customers into 4 groups (segments) based on their 6-month CLTV.
Added the segment information as a new column cltv_segment to the dataframe.
Provided short action recommendations for the management for the next 6 months, focusing on 2 of the 4 segments.
This summary covers the main tasks performed in the code, which can be useful when you want to document the project or share it on GitHub. Let me know if you need any clarification or have additional questions!
