## Inspiration
Since I always prefer videos with captions over pure audio, I wanted an easy and fast way to caption videos that often lack them.

## What it does
EasyCaption captions videos in English using a speech to text model. This works for videos in any language. For example, a video in Spanish will have English subtitles. The resulting video can be watched directly in the web app or downloaded for later.

## How we built it
I used a Vite + React + TypeScript template to get started with the project. I used FastAPI for the backend, and FFmpeg command line executed with Python subprocess to handle the video creation process. Whisper was used for its speech to text transcription and timing.

## Challenges we ran into
I had an issue with loading the videos from the backend and displaying them on the frontend. I tackled this issue by assigning a unique key to each video, so that the page would re-render on every new video.

## Accomplishments that we're proud of
I am very proud to have gone from nothing to a working product in <7 hours. 

## What we learned
I learned how to serve files from the frontend to the backend, and vice versa.

## What's next for EasyCaption
I want to expand on this project to make it cloud hosted and readily available for anyone to use.