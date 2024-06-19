
##############################################################
#CLTV Prediction with BG-NBD and Gamma-Gamma
##############################################################

###############################################################
#Business Problem
###############################################################
#FLO wants to determine a roadmap for its sales and marketing activities.
#In order to make a medium-long term plan, the company needs to estimate the potential value that existing customers will provide to the company in the future.

###############################################################
#Data Set Story
###############################################################
#The data set consists of information obtained from the past purchasing behaviors of customers who made their last purchases in 2020-2021 as OmniChannel (both online and offline shopping).
#master_id: Unique customer number
#order_channel: Which channel was used for the purchase (Android, ios, Desktop, Mobile, Offline)
#last_order_channel: The channel where the last purchase was made
#first_order_date: The date of the customer's first purchase
#last_order_date: The date of the customer's last purchase
#last_order_date_online: The date of the customer's last online purchase
#last_order_date_offline: The date of the customer's last offline purchase
#order_num_total_ever_online: The total number of purchases the customer made online
#order_num_total_ever_offline: The total number of purchases the customer made offline
#customer_value_total_ever_offline: The total amount the customer paid for offline purchases
#customer_value_total_ever_online: The total amount the customer paid for online purchases
#interested_in_categories_12: The list of categories the customer purchased from in the last 12 months


###############################################################
#TASKS
###############################################################
#TASK 1: Data Preparation

       # 1. Read the flo_data_20K.csv data. Create a copy of the dataframe.
       # 2. Define the outlier_thresholds and replace_with_thresholds functions required to suppress the outliers.
       # Note: The frequency values must be integers for CLTV calculation. Therefore, round the upper and lower limits with round().
       # 3. Suppress the outliers, if any, of the "order_num_total_ever_online", "order_num_total_ever_offline", "customer_value_total_ever_offline", "customer_value_total_ever_online" variables.
       # 4. Omnichannel customers are those who shop from both online and offline platforms. Create new variables for each customer's total number of purchases and total spending.
       # 5. Examine the variable types. Convert date-expressing variables to date type.

#TASK 2: Creating the CLTV Data Structure
       # 1. Take the analysis date as 2 days after the date of the last purchase in the data set.
       # 2. Create a new cltv dataframe containing the variables customer_id, recency_cltv_weekly, T_weekly, frequency, and monetary_cltv_avg.
       # The monetary value will be the average value per purchase, and the recency and tenure values will be expressed in weekly terms.

#TASK 3: Establishment of BG/NBD, Gamma-Gamma Models, Calculation of CLTV
       # 1. Fit the BG/NBD model.
            # a. Estimate the expected purchases from customers within 3 months and add it to the cltv dataframe as exp_sales_3_month.
            # b. Estimate the expected purchases from customers within 6 months and add it to the cltv dataframe as exp_sales_6_month.
       # 2. Fit the Gamma-Gamma model. Estimate the average value the customers will leave and add it to the cltv dataframe as exp_average_value.
       # 3. Calculate the 6-month CLTV and add it to the dataframe as cltv.
            # b. Observe the 20 people with the highest CLTV value.

#TASK 4: Creating Segments According to CLTV
       # 1. Divide all your customers into 4 groups (segments) based on 6-month CLTV and add the group names to the data set as cltv_segment.
       # 2. For 2 groups you will choose from the 4 groups, make short action recommendations to the management for the next 6 months.


##############################################################
# BG-NBD ve Gamma-Gamma ile CLTV Prediction
##############################################################



###############################################################
# İş Problemi (Business Problem)
###############################################################
# FLO satış ve pazarlama faaliyetleri için roadmap belirlemek istemektedir.
# Şirketin orta uzun vadeli plan yapabilmesi için var olan müşterilerin gelecekte şirkete sağlayacakları potansiyel değerin tahmin edilmesi gerekmektedir.


###############################################################
# Veri Seti Hikayesi
###############################################################
# Veri seti son alışverişlerini 2020 - 2021 yıllarında OmniChannel(hem online hem offline alışveriş yapan) olarak yapan müşterilerin geçmiş alışveriş davranışlarından
# elde edilen bilgilerden oluşmaktadır.

# master_id: Eşsiz müşteri numarası
# order_channel : Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile, Offline)
# last_order_channel : En son alışverişin yapıldığı kanal
# first_order_date : Müşterinin yaptığı ilk alışveriş tarihi
# last_order_date : Müşterinin yaptığı son alışveriş tarihi
# last_order_date_online : Muşterinin online platformda yaptığı son alışveriş tarihi
# last_order_date_offline : Muşterinin offline platformda yaptığı son alışveriş tarihi
# order_num_total_ever_online : Müşterinin online platformda yaptığı toplam alışveriş sayısı
# order_num_total_ever_offline : Müşterinin offline'da yaptığı toplam alışveriş sayısı
# customer_value_total_ever_offline : Müşterinin offline alışverişlerinde ödediği toplam ücret
# customer_value_total_ever_online : Müşterinin online alışverişlerinde ödediği toplam ücret
# interested_in_categories_12 : Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi


###############################################################
# GÖREVLER
###############################################################
# GÖREV 1: Veriyi Hazırlama
           # 1. flo_data_20K.csv verisini okuyunuz.Dataframe’in kopyasını oluşturunuz.
           # 2. Aykırı değerleri baskılamak için gerekli olan outlier_thresholds ve replace_with_thresholds fonksiyonlarını tanımlayınız.
           # Not: cltv hesaplanırken frequency değerleri integer olması gerekmektedir.Bu nedenle alt ve üst limitlerini round() ile yuvarlayınız.
           # 3. "order_num_total_ever_online","order_num_total_ever_offline","customer_value_total_ever_offline","customer_value_total_ever_online" değişkenlerinin
           # aykırı değerleri varsa baskılayanız.
           # 4. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Herbir müşterinin toplam
           # alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.
           # 5. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.

# GÖREV 2: CLTV Veri Yapısının Oluşturulması
           # 1.Veri setindeki en son alışverişin yapıldığı tarihten 2 gün sonrasını analiz tarihi olarak alınız.
           # 2.customer_id, recency_cltv_weekly, T_weekly, frequency ve monetary_cltv_avg değerlerinin yer aldığı yeni bir cltv dataframe'i oluşturunuz.
           # Monetary değeri satın alma başına ortalama değer olarak, recency ve tenure değerleri ise haftalık cinsten ifade edilecek.


# GÖREV 3: BG/NBD, Gamma-Gamma Modellerinin Kurulması, CLTV'nin hesaplanması
           # 1. BG/NBD modelini fit ediniz.
                # a. 3 ay içerisinde müşterilerden beklenen satın almaları tahmin ediniz ve exp_sales_3_month olarak cltv dataframe'ine ekleyiniz.
                # b. 6 ay içerisinde müşterilerden beklenen satın almaları tahmin ediniz ve exp_sales_6_month olarak cltv dataframe'ine ekleyiniz.
           # 2. Gamma-Gamma modelini fit ediniz. Müşterilerin ortalama bırakacakları değeri tahminleyip exp_average_value olarak cltv dataframe'ine ekleyiniz.
           # 3. 6 aylık CLTV hesaplayınız ve cltv ismiyle dataframe'e ekleyiniz.
                # b. Cltv değeri en yüksek 20 kişiyi gözlemleyiniz.

# GÖREV 4: CLTV'ye Göre Segmentlerin Oluşturulması
           # 1. 6 aylık tüm müşterilerinizi 4 gruba (segmente) ayırınız ve grup isimlerini veri setine ekleyiniz. cltv_segment ismi ile dataframe'e ekleyiniz.
           # 2. 4 grup içerisinden seçeceğiniz 2 grup için yönetime kısa kısa 6 aylık aksiyon önerilerinde bulununuz

# BONUS: Tüm süreci fonksiyonlaştırınız.

###############################################################
# GÖREV 1: Veriyi Hazırlama
###############################################################


# 1. flo_data_20K.csv verisini okuyunuz.Dataframe’in kopyasını oluşturunuz.
#!pip install lifetimes
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
from lifetimes.plotting import plot_period_transactions

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
from sklearn.preprocessing import MinMaxScaler
df_=pd.read_csv('FLOCLTVPrediction/flo_data_20k.csv')
df = df_.copy()
df.describe().T
df.head()
df.isnull().sum()



# 2. Aykırı değerleri baskılamak için gerekli olan outlier_thresholds ve replace_with_thresholds fonksiyonlarını tanımlayınız.
# Not: cltv hesaplanırken frequency değerleri integer olması gerekmektedir.Bu nedenle alt ve üst limitlerini round() ile yuvarlayınız.
def outlier_thresholds(dataframe, variable):
    quartile1 = dataframe[variable].quantile(0.01)
    quartile3 = dataframe[variable].quantile(0.99)
    interquantile_range = quartile3 - quartile1
    up_limit = round(quartile3 + 1.5 * interquantile_range)
    low_limit = round(quartile1 - 1.5 * interquantile_range)
    return low_limit, up_limit


def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)
    #dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit

# 3. "order_num_total_ever_online","order_num_total_ever_offline","customer_value_total_ever_offline","customer_value_total_ever_online" değişkenlerinin
#aykırı değerleri varsa baskılayanız.

replace_with_thresholds(df, "order_num_total_ever_online")
replace_with_thresholds(df, "order_num_total_ever_offline")
replace_with_thresholds(df, "customer_value_total_ever_offline")
replace_with_thresholds(df, "customer_value_total_ever_online")


# 4. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir.
# Herbir müşterinin toplam alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.
df['total_customer_value'] = df['customer_value_total_ever_offline'] + df['customer_value_total_ever_online']
df['total_order_num'] = df['order_num_total_ever_offline'] + df['order_num_total_ever_online']

# 5. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
df.info()
df['last_order_date'] = pd.to_datetime(df['last_order_date'], format='%Y-%m-%d')
df['first_order_date'] = pd.to_datetime(df['first_order_date'], format='%Y-%m-%d')
df['last_order_date_online'] = pd.to_datetime(df['last_order_date_online'], format='%Y-%m-%d')
df['last_order_date_offline'] = pd.to_datetime(df['last_order_date_offline'], format='%Y-%m-%d')

###############################################################
# GÖREV 2: CLTV Veri Yapısının Oluşturulması
###############################################################

# 1.Veri setindeki en son alışverişin yapıldığı tarihten 2 gün sonrasını analiz tarihi olarak alınız.
df['last_order_date'].max()
today_date = dt.datetime(2021, 6, 2)

# 2.customer_id, recency_cltv_weekly, T_weekly, frequency ve monetary_cltv_avg değerlerinin yer aldığı yeni bir cltv dataframe'i oluşturunuz.

#recency: Time elapsed since the last purchase. Weekly. (per user)
#T: Customer's age. Weekly. (how long ago was the first purchase made from the analysis date)
#frequency: total number of recurring purchases (frequency>1)
#monetary: average earnings per purchase

# recency: Son satın alma üzerinden geçen zaman. Haftalık. (kullanıcı özelinde)
# T: Müşterinin yaşı. Haftalık. (analiz tarihinden ne kadar süre önce ilk satın alma yapılmış)
# frequency: tekrar eden toplam satın alma sayısı (frequency>1)
# monetary: satın alma başına ortalama kazanç

cltv_df = df.groupby('master_id').agg(
    last_order_date=('last_order_date', 'max'),
    first_order_date=('first_order_date', 'min'),
    total_order_num=('total_order_num', 'sum'),
    total_customer_value=('total_customer_value', 'sum')
)

cltv_df['last_order_date'] = (today_date - cltv_df['last_order_date']).dt.days
cltv_df['first_order_date'] = (today_date - cltv_df['first_order_date']).dt.days
#cltv_df.columns = cltv_df.columns.droplevel(0)#sütun isimlerini coklu yerine basitleştirmek için kullanılır.

cltv_df.columns = ['recency', 'T', 'frequency', 'monetary']#anlamlı olması icin isimlendiriyoruz

cltv_df["monetary"] = cltv_df["monetary"] / cltv_df["frequency"]

cltv_df.describe().T

cltv_df = cltv_df[(cltv_df['frequency'] > 1)]

cltv_df["recency"] = cltv_df["recency"] / 7

cltv_df["T"] = cltv_df["T"] / 7

cltv_df['frequency']=cltv_df['frequency'].astype(int)

###############################################################
# GÖREV 3: BG/NBD, Gamma-Gamma Modellerinin Kurulması, 6 aylık CLTV'nin hesaplanması
###############################################################

# 1. BG/NBD modelini kurunuz.

bgf = BetaGeoFitter(penalizer_coef=0.001)

bgf.fit(cltv_df['frequency'],
        cltv_df['recency'],
        cltv_df['T'])

# 3 ay içerisinde müşterilerden beklenen satın almaları tahmin ediniz ve exp_sales_3_month olarak cltv dataframe'ine ekleyiniz.
bgf.predict(4 * 3,
            cltv_df['frequency'],
            cltv_df['recency'],
            cltv_df['T']).sum()

cltv_df["exp_sales_3_month"] = bgf.predict(4 * 3,
                                               cltv_df['frequency'],
                                               cltv_df['recency'],
                                               cltv_df['T'])
# 6 ay içerisinde müşterilerden beklenen satın almaları tahmin ediniz ve exp_sales_6_month olarak cltv dataframe'ine ekleyiniz.
bgf.predict(4 * 6,
            cltv_df['frequency'],
            cltv_df['recency'],
            cltv_df['T']).sum()


cltv_df["exp_sales_6_month"] = bgf.predict(4 * 6,
                                               cltv_df['frequency'],
                                               cltv_df['recency'],
                                               cltv_df['T'])

# 3. ve 6.aydaki en çok satın alım gerçekleştirecek 10 kişiyi inceleyeniz.

cltv_df["exp_sales_6_month"].sort_values(ascending=False).head(10)
cltv_df["exp_sales_3_month"].sort_values(ascending=False).head(10)

cltv_df.head(50)


plot_period_transactions(bgf)
plt.show()



# 2.  Gamma-Gamma modelini fit ediniz. Müşterilerin ortalama bırakacakları değeri tahminleyip exp_average_value olarak cltv dataframe'ine ekleyiniz.

ggf = GammaGammaFitter(penalizer_coef=0.01)

ggf.fit(cltv_df['frequency'], cltv_df['monetary'])

ggf.conditional_expected_average_profit(cltv_df['frequency'],
                                        cltv_df['monetary']).head(10)

ggf.conditional_expected_average_profit(cltv_df['frequency'],
                                        cltv_df['monetary']).sort_values(ascending=False).head(10)

cltv_df["expected_average_profit"] = ggf.conditional_expected_average_profit(cltv_df['frequency'],
                                                                             cltv_df['monetary'])
cltv_df.sort_values("expected_average_profit", ascending=False).head(10)

# 3. 6 aylık CLTV hesaplayınız ve cltv ismiyle dataframe'e ekleyiniz.

cltv = ggf.customer_lifetime_value(bgf,
                                   cltv_df['frequency'],
                                   cltv_df['recency'],
                                   cltv_df['T'],
                                   cltv_df['monetary'],
                                   time=6,  # 6 aylık
                                   freq="W",  # T'nin frekans bilgisi.
                                   discount_rate=0.01)#indirim olma ihtimaline karsi

cltv.head()

cltv = cltv.reset_index()

cltv_final = cltv_df.merge(cltv, on="master_id", how="left")
cltv_final.sort_values(by="clv", ascending=False).head(10)

# CLTV değeri en yüksek 20 kişiyi gözlemleyiniz.

cltv_final.sort_values(by="clv", ascending=False).head(20)



###############################################################
# GÖREV 4: CLTV'ye Göre Segmentlerin Oluşturulması
###############################################################

# 1. 6 aylık CLTV'ye göre tüm müşterilerinizi 4 gruba (segmente) ayırınız ve grup isimlerini veri setine ekleyiniz.
# cltv_segment ismi ile atayınız.

cltv_final

cltv_final["cltv_segment"] = pd.qcut(cltv_final["clv"], 4, labels=["D", "C", "B", "A"])

cltv_final.sort_values(by="clv", ascending=False).head(50)

#cltv_final.groupby("cltv_segment").agg({"count", "mean", "sum"})



# 2. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.

cltv_final.groupby("cltv_segment").agg({
    "recency": "mean",
    "frequency": "mean",
    "monetary": "mean"
})
