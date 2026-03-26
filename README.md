# Noly Market Media Generator
This project is a Flask API service that automatically creates social media images (Instagram/X) and short videos (TikTok/Reels) from data from Make.com or similar automation tools.

## Features
Dynamic Image Generation: Generates 1080x1080 PNGs based on specified category, question, and date.

Video (Reels/TikTok) Generation: Creates 5-second MP4 videos from static images using MoviePy.

Automation Friendly: Accepts JSON-based POST requests and returns the file directly (send_file).

Smart Text Wrapping: Automatically divides long questions into new lines using textwrap.

## Installation
1. Requirements
Your system must have Python 3.8+ installed. Additionally, you must have ImageMagick (optional but recommended) and FFmpeg installed for video processing.

2. Installing Libraries
After cloning the project, install the necessary Python packages:

```Bash
pip install flask Pillow moviepy
```
3. Running the Application
```Bash
python app.py
```
The service will start by default at http://0.0.0.0:5000.

## API Usage Media Creation

| Parameter | Type | Description |
|--------------|---------------|--------------|
| question | String | Main question text to appear in the image |
| Category | String | Prediction category (e.g., Sports, Crypto) |
| endPoint | String | End date information |
| type| String | image (default) or video |

Example JSON:
```Json
{
"question": "Will Bitcoin surpass the $100k mark this month?",
"category": "CRYPTO",
"endDate": "December 31, 2025",
"type": "video"
}
```

## Architecture
Make.com (HTTP Module): Sends a POST request to the API according to the specified trigger.

Flask API: Validates the incoming data and directs it to the relevant function (image or video).

Pillow: Creates the background, places the text, and applies the color palette.

MoviePy (Optional): If a video is requested, converts the generated image to MP4 format.

Response: The generated file is sent back directly as a binary HTTP response.

## Notes
Fonts: The code currently uses ImageFont.load_default(). For a more professional look, it's recommended to add a .ttf file to your project and update it to ImageFont.truetype("font-name.ttf", size).

File Management: Generated files accumulate in the server directory. Adding a cleanup function that periodically cleans them is recommended.

Performance: Video generation is a CPU-intensive process; using a queuing structure (Celery/Redis) is recommended for high-traffic applications.



# Noly Market Medya Oluşturucu
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


