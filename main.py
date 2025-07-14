from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled

import re

app = FastAPI()
templates = Jinja2Templates(directory="templates")


def extract_video_id(url: str) -> str:
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    return match.group(1) if match else url


def fetch_subtitles(video_id: str, with_timestamps: bool = True) -> str:
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except TranscriptsDisabled:
        return "Subtitles are disabled for this video."
    except Exception as e:
        return f"Error fetching subtitles: {e}"

    if with_timestamps:
        return "\n".join([f"{entry['start']:.2f}s - {entry['text']}" for entry in transcript])
    else:
        return "\n".join([entry['text'] for entry in transcript])


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("subtitles.html", {"request": request, "subtitles": "", "url": "", "format": "with"})


@app.get("/get_subtitles", response_class=HTMLResponse)
def get_subtitles(request: Request, url: str = Query(...), format: str = Query("with")):
    video_id = extract_video_id(url)
    with_timestamps = format == "with"
    subtitles = fetch_subtitles(video_id, with_timestamps)
    return templates.TemplateResponse("subtitles.html", {
        "request": request,
        "subtitles": subtitles,
        "url": url,
        "format": format
    })
