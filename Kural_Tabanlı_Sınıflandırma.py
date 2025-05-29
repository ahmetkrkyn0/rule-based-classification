###########
# GÖREV-1
###########

import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv(r"Dataset/persona.csv")
df.head()
df.info()
df.describe()

df.nunique()

df["PRICE"].nunique()

df["PRICE"].value_counts()

df["COUNTRY"].value_counts()
df["AGE"].value_counts()

df.groupby("COUNTRY")["PRICE"].sum()
df.groupby("COUNTRY")["PRICE"].sum().plot(kind="bar")
plt.xlabel("Ülkeler")
plt.ylabel("Toplam Gelir")
plt.title("Ülkelere Göre Toplam Satış Geliri")
plt.show()

df.groupby("SOURCE")["PRICE"].sum()

df.groupby("COUNTRY")["PRICE"].mean()

df.groupby("SOURCE")["PRICE"].mean()

df.groupby(["COUNTRY", "SOURCE"])["PRICE"].mean()
df.groupby(["COUNTRY", "SOURCE"])["PRICE"].mean().plot(kind="bar")
plt.show()


##########################################################################
# GÖREV-2 COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
##########################################################################

df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"])["PRICE"].mean()
df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"])["PRICE"].mean().plot(kind="bar")
plt.show()


##########################################################################
# Görev 3:  Çıktıyı PRICE’a göre sıralayınız.
# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE’a göre uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.
##########################################################################

# agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"])["PRICE"].mean().sort_values(ascending=False)
agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)


###################################################################################################################################
# Görev 4:  Indekste yer alan isimleri değişken ismine çeviriniz.
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir. Bu isimleri değişken isimlerine çeviriniz.
###################################################################################################################################

agg_df = agg_df.reset_index()


###################################################################################################################################
# Görev 5:  Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
# Age sayısal değişkenini kategorik değişkene çeviriniz.
# Aralıkları ikna edici şekilde oluşturunuz.
# Örneğin: ‘0_18', ‘19_23', '24_30', '31_40', '41_70'
###################################################################################################################################

df["AGE_CAT"] = pd.cut(df["AGE"], [0, 18, 23, 30, 40, 70], labels=["0_18", "19_23", "24_30", "31_40", "41_70"])
df.head()
agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE", "AGE_CAT"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False).reset_index()


###################################################################################################################################
# Görev 6:  Yeni seviye tabanlı müşterileri (persona) tanımlayınız
# Yeni seviye tabanlı müşterileri (persona) tanımlayınız ve veri setine değişken olarak ekleyiniz.
# Yeni eklenecek değişkenin adı: customers_level_based
# Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek customers_level_based değişkenini oluşturmanız gerekmektedir.
###################################################################################################################################

df["customers_level_based"] = (df["COUNTRY"].str.upper() + "_" + df["SOURCE"].str.upper() + "_" + df["SEX"].str.upper() + "_" + df["AGE_CAT"].astype(str))

agg_df = df.groupby("customers_level_based").agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)



###################################################################################################################################
# Görev 7:  Yeni müşterileri (personaları) segmentlere ayırınız.
# Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız.
# Segmentleri SEGMENTisimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
# Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).
###################################################################################################################################

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.head()
agg_df.groupby("SEGMENT").agg({"PRICE": ["mean", "max", "sum"]})


###################################################################################################################################
# Görev 8:  Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini  tahmin ediniz.
###################################################################################################################################

# Soru-1: 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir? #
new_user_1 = "TUR_ANDROID_FEMALE_31_40"
agg_df = agg_df.reset_index()
agg_df[agg_df["customers_level_based"] == new_user_1]

# Soru-2: 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir? #
new_user_2 = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == "FRA_IOS_FEMALE_31_40"]












