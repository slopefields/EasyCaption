from collections import namedtuple
from utils import format_time
import subprocess
import whisper
import os

CAPTION_PATH = "./temp/captions.ass"
OUTPUT_PATH = "./temp/output.mp4"
FONT_FOLDER_PATH = "./assets/fonts"
VIDEO_RES_X = 640
VIDEO_RES_Y = 360

WHISPER_MODEL = whisper.load_model("tiny")

Phrase = namedtuple("Phrase", ["text", "start", "end"])

def transcribe(video_path, task):
    result = WHISPER_MODEL.transcribe(video_path, task=task)
    captions = []
    for segment in result["segments"]:
        text = segment["text"]
        start = segment["start"]
        end = segment["end"]
        captions.append(Phrase(text, start, end))
    print(captions)
    return captions

def create_caption_file(captions):
    os.makedirs(os.path.dirname(CAPTION_PATH), exist_ok=True)
    with open(CAPTION_PATH, 'w') as f:
        # [Script Info]
        f.write("[Script Info]\n")
        f.write("ScriptType: v4.00+\n")
        f.write("ScaledBorderAndShadow: yes\n")
        f.write(f"PlayResX: {VIDEO_RES_X}\n")
        f.write(f"PlayResY: {VIDEO_RES_Y}\n\n")
        
        # [V4+ Styles]
        f.write("[V4+ Styles]\n")
        f.write("Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, " \
        "Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, " \
        "MarginL, MarginR, MarginV, Encoding\n")
       
        # COMMON ALIGNMENTS:
        # 1	Bottom-left
        # 2	Bottom-center
        # 3	Bottom-right
        # 4	Middle-left
        # 5	Middle-center
        # 6	Middle-right
        # 7	Top-left
        # 8	Top-center
        # 9	Top-right

        f.write("Style: Default, THE BOLD FONT (FREE VERSION), 20, &H00FFFFFF, &H000000FF, &H00000000, &H80000000, " \
                "-1, 0, 0, 0, 100, 100, 0, 0, 1, 3, 0, 2, "
                "10, 10, 10, 1\n\n")
        

        # [Events]
        f.write("[Events]\n")
        f.write("Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")
        for phrase in captions:
            formatted_start = format_time(phrase.start)
            formatted_end = format_time(phrase.end)
            f.write(f"Dialogue: 0,{formatted_start},{formatted_end},Default,,0,0,0,,{{\\fscx92\\fscy92\\t(0,75,\\fscx100\\fscy100)}}{phrase.text}\n")

def burn_captions(video_path):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    filter_complex = f"[0:v]subtitles={CAPTION_PATH}:fontsdir={FONT_FOLDER_PATH}[vout]"

    cmd = [
            "ffmpeg",
            "-y",
            "-i", video_path,
            "-filter_complex", filter_complex,
            "-map", "[vout]",
            "-map", "0:a",
            "-crf", "18",
            "-preset", "ultrafast",
            "-r", "24",
            "-c:v", "libx264",
            "-c:a", "copy", 
            "-threads", "16",
            OUTPUT_PATH
        ]
    print(f"RUNNING COMMAND: {cmd}")
    subprocess.run(cmd)