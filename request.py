import requests

url = 'https://github.com'
headers = {'user-agent': 'custom-agent'} #kendimiz hakkında bilgi veriyoruz

r = requests.get(url, headers=headers, timeout=2) #timeout sitenin requeste yanıtı için süre kısıtlaması yapar. (2 saniye)

print(r.status_code) #client ile server arasındaki iletişim sürecini ifade eden 3 haneli sayılar, status code'dur. siteye gönderdiğimiz istekten sonra bir status code da istiyoruz.
# print(r.text) # sitede var olan tüm icerigini alıyor. (bu kısmı yorum satırından çıkararak dene) (javascript gibi aktif değişkenleri burada göremeyebilirsin, sade ve temel kodu alıyoruz.

print(r.headers.get('Date'))  # sayfaya ait headers değerleri içinden Date'i filtreler. (almak istediğin bilgiye göre date kısmını değiştirebilirsin.)

# 200 yani BASARI kodu geldi. 
# olumlu dönüş olması, user-agent propertysi için github'ın filtreleme yapmadığını gösteriyor.
# bazı web siteleri user-agent’sız ya da bilinmeyen user-agent’la gelen isteği reddeder.
# buraya kadarki kodu headers olmadan da çalıştırabilirsin, bu da siteye kendimizi tanıtmadan istek göndermemiz anlamına gelir.

url2 = 'http://github.com' #https yerine http yazarak sistemin nasıl tepki vereceğini deniyoruz.

r = requests.get(url2, allow_redirects=False) #

print(r.status_code)

#301 kodu geliyor, yani bizi http'den https adresine alıp taşımış.
