# Noly Market Media Generator

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/ersozberk/noly-medya-bot/edit/main/README.md)
[![pt-br](https://img.shields.io/badge/lang-tr-green.svg)](https://github.com/ersozberk/noly-medya-bot/edit/main/README-tr.md)

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

