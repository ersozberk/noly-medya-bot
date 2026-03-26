🎨 Noly Market Media Generator
Bu proje, Make.com veya benzeri otomasyon araçlarından gelen verilerle otomatik olarak sosyal medya görselleri (Instagram/X) ve kısa videolar (TikTok/Reels) oluşturan bir Flask API servisidir.

🔥 Özellikler
Dinamik Görsel Oluşturma: Belirlenen kategori, soru ve tarihe göre 1080x1080 boyutunda PNG üretir.

Video (Reels/TikTok) Üretimi: MoviePy kullanarak statik görsellerden 5 saniyelik MP4 videolar oluşturur.

Otomasyon Dostu: JSON tabanlı POST isteklerini kabul eder ve doğrudan dosyayı (send_file) döndürür.

Akıllı Metin Kaydırma: Uzun soruları textwrap ile otomatik olarak alt satıra böler.

🛠 Kurulum
1. Gereksinimler
Sisteminizde Python 3.8+ yüklü olmalıdır. Ayrıca video işleme için sisteminizde ImageMagick (opsiyonel ama önerilir) ve FFmpeg kurulu olmalıdır.

2. Kütüphanelerin Yüklenmesi
Projeyi klonladıktan sonra gerekli Python paketlerini yükleyin:

'''bash
pip install flask Pillow moviepy
'''
