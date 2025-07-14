# YouTube Subtitles Extractor

A simple FastAPI web application to extract subtitles from YouTube videos. Users can input a YouTube URL and choose to extract subtitles with or without timestamps.

## Features

- Extracts subtitles from YouTube videos using [`YouTubeTranscriptApi`](https://github.com/jdepoix/youtube-transcript-api).
- Option to display subtitles with or without timestamps.
- Simple web interface built with FastAPI and Jinja2 templates.

## Requirements

- Python 3.8+
- FastAPI
- Jinja2
- youtube-transcript-api
- Uvicorn (for running the server)

## Installation

```sh
pip install fastapi jinja2 youtube-transcript-api uvicorn
```

## Usage

1. Start the server:

    ```sh
    uvicorn main:app --reload
    ```

2. Open your browser and go to [http://localhost:8000](http://localhost:8000).

3. Enter a YouTube video URL and select the subtitle format.

## Project Structure

- [`main.py`](main.py): FastAPI application logic.
- [`templates/subtitles.html`](templates/subtitles.html): Jinja2 template for the web interface.

