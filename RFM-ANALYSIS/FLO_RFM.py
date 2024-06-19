###############################################################
#Customer Segmentation with RFM
###############################################################

###############################################################
#Business Problem
###############################################################

#FLO wants to segment its customers and determine marketing strategies based on these segments.
#For this purpose, customer behavior will be defined and groups will be formed according to these behavioral clusters.
###############################################################
#Data Set Story
###############################################################

#The data set consists of information obtained from the past shopping behavior of customers who made their last purchases in 2020 - 2021 as OmniChannel (both online and offline shopping).
#master_id: Unique customer number
#order_channel: Which channel the purchase was made on (Android, iOS, Desktop, Mobile, Offline)
#last_order_channel: The channel where the last purchase was made
#first_order_date: The date of the customer's first purchase
#last_order_date: The date of the customer's last purchase
#last_order_date_online: The date of the customer's last online purchase
#last_order_date_offline: The date of the customer's last offline purchase
#order_num_total_ever_online: Total number of purchases the customer made online
#order_num_total_ever_offline: Total number of purchases the customer made offline
#customer_value_total_ever_offline: Total amount the customer paid for offline purchases
#customer_value_total_ever_online: Total amount the customer paid for online purchases
#interested_in_categories_12: List of categories the customer shopped in the last 12 months

###############################################################
#TASKS
###############################################################

#TASK 1: Understanding (Data Understanding) and Preparing the Data
       # 1. Read the flo_data_20K.csv data.
       # 2. In the data set, examine:
                 # a. The first 10 observations,
                 # b. Variable names,
                 # c. Descriptive statistics,
                 # d. Missing values,
                 # e. Variable types.
       # 3. Omnichannel customers refer to customers who shop both online and offline. Create new variables to calculate the total number of purchases and total spending for each customer.
       # 4. Examine the variable types. Convert date-expressing variables to the date type.
       # 5. Examine the distribution of the number of customers, average number of products purchased, and average expenditure in the sales channels.
       # 6. List the top 10 customers who generate the most revenue.
       # 7. List the top 10 customers who place the most orders.
       # 8. Functionalize the data preparation process.
#TASK 2: Calculating RFM Metrics
#TASK 3: Calculating RF and RFM Scores
#TASK 4: Defining RF Scores as Segments
#TASK 5: Time for action!
       # 1. Examine the recency, frequency, and monetary averages of the segments.
       # 2. Using RFM analysis, find the relevant profiles for 2 cases and save the customer IDs to a CSV file.
               # a. FLO is adding a new women's shoe brand to its portfolio. The product prices of the new brand are above the general customer preferences. Therefore, it is desired to communicate specially with the profile of customers who are loyal customers, spend an average of over 250 TL and shop from the women's category. Save the ID numbers of these customers to a CSV file named new_brand_target_customer_ids.csv.
               # b. A discount of almost 40% is planned for men's and children's products. With this discount, it is desired to specially target the customers who have been good customers in the past but have not shopped for a long time, the dormant ones, and the new customers who are interested in the relevant categories. Save the IDs of the appropriate profile customers to a CSV file named discount_target_customer_ids.csv.
#TASK 6: Functionalize the entire process.

###############################################################
# RFM ile Müşteri Segmentasyonu (Customer Segmentation with RFM)
###############################################################

###############################################################
# İş Problemi (Business Problem)
###############################################################
# FLO müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama stratejileri belirlemek istiyor.
# Buna yönelik olarak müşterilerin davranışları tanımlanacak ve bu davranış öbeklenmelerine göre gruplar oluşturulacak..

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

# GÖREV 1: Veriyi Anlama (Data Understanding) ve Hazırlama
           # 1. flo_data_20K.csv verisini okuyunuz.
           # 2. Veri setinde
                     # a. İlk 10 gözlem,
                     # b. Değişken isimleri,
                     # c. Betimsel istatistik,
                     # d. Boş değer,
                     # e. Değişken tipleri, incelemesi yapınız.
           # 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Herbir müşterinin toplam
           # alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.
           # 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
           # 5. Alışveriş kanallarındaki müşteri sayısının, ortalama alınan ürün sayısının ve ortalama harcamaların dağılımına bakınız.
           # 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.
           # 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.
           # 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.

# GÖREV 2: RFM Metriklerinin Hesaplanması

# GÖREV 3: RF ve RFM Skorlarının Hesaplanması

# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması

# GÖREV 5: Aksiyon zamanı!
           # 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.
           # 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulun ve müşteri id'lerini csv ye kaydediniz.
                   # a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
                   # tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Sadık müşterilerinden(champions,loyal_customers),
                   # ortalama 250 TL üzeri ve kadın kategorisinden alışveriş yapan kişiler özel olarak iletişim kuralacak müşteriler. Bu müşterilerin id numaralarını csv dosyasına
                   # yeni_marka_hedef_müşteri_id.cvs olarak kaydediniz.
                   # b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşteri olan ama uzun süredir
                   # alışveriş yapmayan kaybedilmemesi gereken müşteriler, uykuda olanlar ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
                   # olarak kaydediniz.


# GÖREV 6: Tüm süreci fonksiyonlaştırınız.

###############################################################
# GÖREV 1: Veriyi  Hazırlama ve Anlama (Data Understanding)
###############################################################
import datetime as dt
import pandas as pd
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

df_ = pd.read_csv(r"C:\Users\rana_\Downloads\Data Science\crmAnalytics\FLOMusteriSegmentasyonu\flo_data_20k.csv")
df = df_.copy()

# 2. Veri setinde
        # a. İlk 10 gözlem,
        # b. Değişken isimleri,
        # c. Boyut,
        # d. Betimsel istatistik,
        # e. Boş değer,
        # f. Değişken tipleri, incelemesi yapınız.
df.head(10)
df.columns
df.shape
df.describe().T
df.isnull().sum()
df.info()



# 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir.
# Herbir müşterinin toplam alışveriş sayısı ve harcaması için yeni değişkenler oluşturunuz.
df["master_id"].value_counts()#anlıyoruz ki satırlar benzersiz müsterilerin toplam alıisverisini gösteriyor
df["TotalPrice"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]
df["TotalOrder"] = df["order_num_total_ever_offline"] + df["order_num_total_ever_online"]

# 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.

df["first_order_date"] = df["first_order_date"].apply(pd.to_datetime)
df["last_order_date"] = df["last_order_date"].apply(pd.to_datetime)
df["last_order_date_online"] = df["last_order_date_online"].apply(pd.to_datetime)
df["last_order_date_offline"] = df["last_order_date_offline"].apply(pd.to_datetime)

df.info()


# 5. Alışveriş kanallarındaki müşteri sayısının, toplam alınan ürün sayısı ve toplam harcamaların dağılımına bakınız. 

df.groupby("master_id").agg({"TotalOrder": "sum"}).sort_values("TotalOrder", ascending=False).head()
df.groupby("master_id").agg({"TotalPrice": "sum"}).sort_values("TotalPrice", ascending=False).head()
df.groupby("master_id").agg({"TotalPrice": "sum", "TotalOrder": "sum"}).sort_values("TotalPrice", ascending=False).head()

# 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.

df.groupby("master_id")["TotalPrice"].sum().sort_values(ascending=False).head(10)


# 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.

df.groupby("master_id")["TotalOrder"].sum().sort_values(ascending=False).head(10)

# 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.
def preprocess_data(df):
    """
    Preprocesses the data by:
    1. Creating new columns 'TotalPrice' and 'TotalOrder'
    2. Converting date columns to datetime format

    Args:
        df (pandas.DataFrame): The input dataframe

    Returns:
        pandas.DataFrame: The preprocessed dataframe
    """
    # Create new columns
    df["TotalPrice"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]
    df["TotalOrder"] = df["order_num_total_ever_offline"] + df["order_num_total_ever_online"]

    # Convert date columns to datetime
    date_columns = ['first_order_date', 'last_order_date', 'last_order_date_online', 'last_order_date_offline']
    for col in date_columns:
        df[col] = pd.to_datetime(df[col])

    return df
preprocess_data(df)
###############################################################
# GÖREV 2: RFM Metriklerinin Hesaplanması
###############################################################

# Veri setindeki en son alışverişin yapıldığı tarihten 2 gün sonrasını analiz tarihi

df["last_order_date"].max()
today_date = dt.datetime(2021, 6, 2)
type(today_date)

# customer_id, recency, frequnecy ve monetary değerlerinin yer aldığı yeni bir rfm dataframe

rfm = df.groupby('master_id').agg({'last_order_date': lambda OrderDate: (today_date - OrderDate.max()).days,  #ilgili müsterinin son satın alma tarihini çıkar yani recency
                                   'TotalOrder': lambda TotalPrice: TotalPrice.sum(),  # musterilere gore kaçar sipariş oldugu yani frequency
                                   'TotalPrice': lambda TotalPrice: TotalPrice.sum()})#musterilere gore toplam odedıklerı ucret yani monetary
rfm.head()

rfm.columns = ['recency', 'frequency', 'monetary']

rfm.describe().T
#monetary 0 olmaması gerekir
rfm.shape

###############################################################
# GÖREV 3: RF ve RFM Skorlarının Hesaplanması (Calculating RF and RFM Scores)
###############################################################

#  Recency, Frequency ve Monetary metriklerini qcut yardımı ile 1-5 arasında skorlara çevrilmesi ve
# Bu skorları recency_score, frequency_score ve monetary_score olarak kaydedilmesi
rfm["recency_score"] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])

rfm["frequency_score"] = pd.qcut(rfm['frequency'].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])

rfm["monetary_score"] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])

rfm.describe().T

# recency_score ve frequency_score’u tek bir değişken olarak ifade edilmesi ve RF_SCORE olarak kaydedilmesi

rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str) +
                    rfm['frequency_score'].astype(str))


###############################################################
# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması
###############################################################

# Oluşturulan RFM skorların daha açıklanabilir olması için segment tanımlama ve  tanımlanan seg_map yardımı ile RF_SCORE'u segmentlere çevirme

seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}

rfm['segment'] = rfm['RFM_SCORE'].replace(seg_map, regex=True)#regex tablosu ile degisiklik yap



###############################################################
# GÖREV 5: Aksiyon zamanı!
###############################################################

# 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.
rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(["mean", "count"])#segmente göre rfm degerlerini groubya alarak toplam ve ortalama durumlarını inceliyoruz


# 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulunuz ve müşteri id'lerini csv ye kaydediniz.

# a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
# tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Bu müşterilerin sadık  ve
# kadın kategorisinden alışveriş yapan kişiler olması planlandı. Müşterilerin id numaralarını csv dosyasına yeni_marka_hedef_müşteri_id.cvs
# olarak kaydediniz.
df.head()
# Kategorileri ayrı sütunlara ayırma
all_categories = set()
for row in df['interested_in_categories_12']:
    all_categories.update(category.strip('[]') for category in row.split(', '))

for category in all_categories:
    df[category] = df['interested_in_categories_12'].str.contains(category).astype(int)

df.head()


# Kadın sütununda 1 olanların master_id'lerini al
women_master_ids = df.loc[df['KADIN'] == 1, 'master_id']

# Sonuçları yazdırın
print(women_master_ids)
rfm.head()
loyal_women = rfm.loc[rfm.index.isin(women_master_ids) & (rfm['segment'] == 'loyal_customers')]

# Sonuçları yazdırın
print(loyal_women)


loyal_women.index.to_series().to_csv('yeni_marka_hedef_müşteri_id.csv', header=False)

# b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşterilerden olan ama uzun süredir
# alışveriş yapmayan ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
# olarak kaydediniz.

# Erkek ve çocuk sütunlarında 1 olan kişilerin master_id'lerini alın
at_risk_master_ids = df.loc[(df['ERKEK'] == 1) | (df['COCUK'] == 1), 'master_id']

# "at_risk" segmentindeki erkek ve çocukları seçin
at_risk_customers = rfm.loc[rfm.index.isin(at_risk_master_ids) & (rfm['segment'] == 'at_risk')]

# at_risk_customers dataframe'indeki index numaralarını yeni bir CSV dosyasına kaydet
at_risk_customers.index.to_series().to_csv('indirim_hedef_müşteri_ids.csv', header=False)
