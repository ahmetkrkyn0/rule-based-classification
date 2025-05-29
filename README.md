# rule-based-classification
# Müşteri Segmentasyonu Projesi

Bu proje, bir e-ticaret firmasının müşteri verilerini analiz ederek kullanıcıları segmentlere ayırmayı amaçlamaktadır. Projede kural tabanlı sınıflandırma yöntemi kullanılmış ve kullanıcıların demografik bilgileri (ülke, cinsiyet, yaş, cihaz tipi) üzerinden seviye tabanlı müşteri profilleri (persona) oluşturulmuştur.

## 🔍 Proje Amacı

- Müşteri verileri üzerinden segmentasyon gerçekleştirmek.
- Yeni gelen bir kullanıcının hangi segmente ait olduğunu tahmin etmek.
- Kullanıcının potansiyel gelirini öngörmek.

## 🛠️ Kullanılan Araçlar

- Python
- pandas
- matplotlib

## 📊 Veri Kümesi

Veri kümesi `persona.csv` dosyasından okunmaktadır. Bu dosya, kullanıcıların:
- Ülke bilgisi (`COUNTRY`)
- Cihaz türü (`SOURCE`)
- Cinsiyet (`SEX`)
- Yaş bilgisi (`AGE`)
- Satın alma bedeli (`PRICE`) gibi alanları içermektedir.

> ⚠️ **Dikkat**: `persona.csv` dosyası bu depo içerisinde yer almamaktadır. Projeyi çalıştırmak isteyenler, bu veri dosyasını ayrıca temin edip `Dataset/` klasörü altına yerleştirmelidir.

## 📈 Proje Aşamaları

1. **Veri Keşfi (Exploratory Data Analysis)**  
   Temel istatistiksel analizler yapılmış, grafiklerle desteklenmiştir.

2. **Gruplama ve Ortalama Kazanç Hesaplama**  
   Ülke, cihaz türü, cinsiyet ve yaş kırılımlarına göre ortalama gelirler hesaplanmıştır.

3. **Yaş Kategorilerine Ayırma**  
   Yaş aralıkları belirlenerek yaş bilgisi kategorik hale getirilmiştir.

4. **Persona Oluşturma**  
   Kullanıcı bilgileri birleştirilerek `customers_level_based` adında seviye tabanlı müşteri tanımları oluşturulmuştur.

5. **Segmentasyon**  
   Müşteriler `PRICE` değişkenine göre A, B, C, D olmak üzere 4 segmente ayrılmıştır.

6. **Yeni Kullanıcıların Sınıflandırılması**  
   Örnek kullanıcılar oluşturularak ait oldukları segmentler ve beklenen gelirler tahmin edilmiştir.

## 📌 Örnek Kullanıcı Sorguları

```python
new_user_1 = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user_1]
