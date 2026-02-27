from flask import Flask, request, send_file, jsonify
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
from moviepy import ImageClip

app = Flask(__name__)

# Senin yazdığın resim üretim fonksiyonu
def create_social_image(question, category, end_date):
    width, height = 1080, 1080
    image = Image.new('RGB', (width, height), color='#0B0E14')
    draw = ImageDraw.Draw(image)

    # Sunucuda (Linux) çalışacağı için varsayılan fontu kullanıyoruz
    title_font = ImageFont.load_default()
    category_font = ImageFont.load_default()
    brand_font = ImageFont.load_default()

    draw.text((100, 150), f"🔥 KATEGORI: {category.upper()}", font=category_font, fill="#00FF9D")
    
    wrapped_text = textwrap.fill(question, width=25)
    draw.multiline_text((100, 250), wrapped_text, font=title_font, fill="#FFFFFF", spacing=30)

    draw.text((100, 850), f"⏳ Bitis: {end_date}", font=category_font, fill="#FF3366")
    draw.text((100, 930), "NOLY MARKET'TE TAHMIN ET, TP KAZAN!", font=brand_font, fill="#8A2BE2")

    output_filename = f"post_{category.lower()}_{os.urandom(4).hex()}.png"
    image.save(output_filename)
    return output_filename

# Senin yazdığın video üretim fonksiyonu
def create_tiktok_video(question, category, end_date):
    width, height = 1080, 1920
    image = Image.new('RGB', (width, height), color='#0a001a')
    draw = ImageDraw.Draw(image)

    title_font = ImageFont.load_default()
    category_font = ImageFont.load_default()
    brand_font = ImageFont.load_default()

    draw.text((100, 300), f"⚡ KATEGORI: {category.upper()}", font=category_font, fill="#00FF9D")
    
    wrapped_text = textwrap.fill(question, width=22)
    draw.multiline_text((100, 450), wrapped_text, font=title_font, fill="#FFFFFF", spacing=40)

    draw.text((100, 1500), f"⏳ Son Karar: {end_date}", font=category_font, fill="#FF3366")
    draw.text((100, 1600), "Tarafini Sec, TP Kazan!", font=brand_font, fill="#8A2BE2")
    draw.text((100, 1700), "📍 nolymarket.com", font=category_font, fill="#A0A0A0")

    temp_image_path = f"temp_{os.urandom(4).hex()}.png"
    image.save(temp_image_path)

    clip = ImageClip(temp_image_path).with_duration(5)
    output_filename = f"reel_{category.lower()}_{os.urandom(4).hex()}.mp4"
    clip.write_videofile(output_filename, fps=24, codec="libx264", audio=False, logger=None)
    
    if os.path.exists(temp_image_path):
        os.remove(temp_image_path)
        
    return output_filename

# Make.com buraya istek atacak
@app.route('/generate-media', methods=['POST'])
def generate_media():
    data = request.json
    question = data.get('question')
    category = data.get('category')
    end_date = data.get('endDate')
    media_type = data.get('type', 'image') # image veya video

    if not question or not category:
        return jsonify({"error": "Eksik veri"}), 400

    try:
        if media_type == 'video':
            filename = create_tiktok_video(question, category, end_date)
            mime_type = 'video/mp4'
        else:
            filename = create_social_image(question, category, end_date)
            mime_type = 'image/png'
            
        # DİKKAT: Üretilen dosyayı Make.com'a gönderiyoruz!
        return send_file(filename, mimetype=mime_type)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
