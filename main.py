from fastapi import FastAPI
import yt_dlp
import os

app = FastAPI()

@app.get("/")
def home():
    return {"status": "شغال"}

@app.get("/get")
def get_url(url: str):
    try:
        ydl_opts = {'format': '18/22/best', 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {"url": info['url'], "title": info.get('title')}
    except Exception as e:
        return {"error": str(e)}
