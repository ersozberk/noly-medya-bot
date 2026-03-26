
# Noly Market Medya Oluşturucu

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/ersozberk/noly-medya-bot/edit/main/README.md)
[![pt-br](https://img.shields.io/badge/lang-tr-green.svg)](https://github.com/ersozberk/noly-medya-bot/edit/main/README-tr.md)

Bu proje, Make.com veya benzeri otomasyon araçlarından gelen verilerle otomatik olarak sosyal medya görselleri (Instagram/X) ve kısa videolar (TikTok/Reels) oluşturan bir Flask API servisidir.

## Özellikler
Dinamik Görsel Oluşturma: Belirlenen kategori, soru ve tarihe göre 1080x1080 boyutunda PNG üretir.

Video (Reels/TikTok) Üretimi: MoviePy kullanarak statik görsellerden 5 saniyelik MP4 videolar oluşturur.

Otomasyon Dostu: JSON tabanlı POST isteklerini kabul eder ve doğrudan dosyayı (send_file) döndürür.

Akıllı Metin Kaydırma: Uzun soruları textwrap ile otomatik olarak alt satıra böler.

## Kurulum
1. Gereksinimler
Sisteminizde Python 3.8+ yüklü olmalıdır. Ayrıca video işleme için sisteminizde ImageMagick (opsiyonel ama önerilir) ve FFmpeg kurulu olmalıdır.

2. Kütüphanelerin Yüklenmesi
Projeyi klonladıktan sonra gerekli Python paketlerini yükleyin:

```Bash
pip install flask Pillow moviepy
```

3. Uygulamayı Çalıştırma
```Bash
python app.py
```
Servis varsayılan olarak http://0.0.0.0:5000 adresinde çalışmaya başlayacaktır.

## API KullanımıMedya Oluşturma


| Paramatre | Tip | Açıklama |
|--------------|---------------|--------------|
| question | String | Görselde görünecek ana soru metni |
| Category | String  | Tahmin kategorisi (Örn: Spor, Kripto) |
| endPoint | String | Bitiş tarihi bilgisi |
| type| String | image (varsayılan) veya video | 

Örnek JSON:
```Json
{
    "question": "Bitcoin bu ay 100k dolar barajını aşar mı?",
    "category": "KRİPTO",
    "endDate": "31 Aralik 2025",
    "type": "video"
}
```


## Mimari
Make.com (HTTP Module): Belirlenen tetikleyiciye göre API'ye POST isteği atar.

Flask API: Gelen veriyi doğrular ve ilgili fonksiyona (image veya video) yönlendirir.

Pillow: Arka planı oluşturur, metinleri yerleştirir ve renk paletini uygular.

MoviePy (Opsiyonel): Eğer video istenmişse, oluşturulan görseli MP4 formatına dönüştürür.

Response: Üretilen dosya binary olarak doğrudan HTTP yanıtı ile geri gönderilir.

## Notlar
Fontlar: Kod şu anda ImageFont.load_default() kullanmaktadır. Daha profesyonel bir görünüm için projenize bir .ttf dosyası ekleyip ImageFont.truetype("font-adi.ttf", size) şeklinde güncellemeniz önerilir.

Dosya Yönetimi: Üretilen dosyalar sunucu dizininde birikir. Periyodik olarak temizleyen bir cleanup fonksiyonu eklenmesi tavsiye edilir.

Performans: Video üretimi CPU yoğunluklu bir işlemdir; yüksek trafikli kullanımlarda kuyruk yapısı (Celery/Redis) kullanılması önerilir.
