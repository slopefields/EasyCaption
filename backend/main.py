from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from captions import transcribe, create_caption_file, burn_captions
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/temp", StaticFiles(directory="temp"), name="temp")

@app.get('/')
async def test():
    return {"hello"}

@app.post('/burn-captions')
async def test(video: UploadFile = File(...), translate: str = Form(...)):
    do_translate = translate == "true" # boolean
    print(f"burn captions, translate: {do_translate}")

    video_path = os.path.join("assets", video.filename)
    with open(video_path, "wb") as f:
        f.write(await video.read())

    if (do_translate):
        captions = transcribe(video_path, "translate")
    else:
        captions = transcribe(video_path, "transcribe")
    
    create_caption_file(captions)

    burn_captions(video_path)