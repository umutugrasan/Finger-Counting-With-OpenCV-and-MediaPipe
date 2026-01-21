##### **# OpenCV ve MediaPipe ile 10 Parmak Sayma**



Bu proje, bilgisayar kamerası aracılığıyla el hareketlerini algılayan ve ekranda toplam parmak sayısını (0-10) gerçek zamanlı olarak gösteren bir Python uygulamasıdır.



###### **Özellikler**



* **Çoklu El Desteği:** Hem sağ hem sol eli aynı anda algılayarak toplam parmak sayısını hesaplar.
* **Akıllı Algoritma:** Ayna görüntüsü farkını ortadan kaldıran, koordinat bazlı el ayrımı mantığı kullanılmıştır.
* **Yüksek Performans:** MediaPipe kütüphanesi sayesinde düşük gecikme ile çalışır.
* **Açıklayıcı Kod:** Kod içerisinde detaylı açıklama satırları bulunmaktadır.
* **Sürüm Uyumsuzluğu Çözümü:** Python'ın en güncel sürümleri ile MediaPipe kütüphanesi arasındaki sürüm uyumsuzluklarını aşmak adına; bu proje sanal bir ortam (venv) üzerinde, stabilite testi yapılmış eski sürümler kullanılarak yapılandırılmıştır. Gerekli kütüphaneler requirements.txt dosyasında listelenmiştir.



###### **Öğrenilenler**



Bu süreçte şu konularda pratik deneyim kazanılmıştır:



* Görüntü işleme (Computer Vision) temelleri.
* El landmark (eklem) noktalarının analizi ve birbirlerine göre bağıl konumlarının hesaplanması.
* Aynalanmış görüntü üzerinde sağ-sol el ayrımı mantığı geliştirme.
* Sanal ortam (virtual environment) yönetimi.

###### **MediaPipe El Landmark Noktaları**

Projede kullanılan el eklem noktalarının (landmark) referans şeması aşağıdadır:

![MediaPipe Hand Landmarks](hand_landmarks.png)
