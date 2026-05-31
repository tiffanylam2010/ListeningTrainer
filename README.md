# ListeningTrainer

ListeningTrainer is a web-based language listening practice tool designed to help learners improve listening comprehension through transcript-assisted learning.

## Features

* Play videos with synchronized transcripts
* Jump to any sentence directly from the transcript
* Sentence-by-sentence listening with auto-pause
* Edit transcript text and adjust subtitle timing
* Delete and merge transcript segments
* A-B loop support for focused listening practice
* Automatic transcript saving
* Support for loading videos by video ID

## Why I Built This

When practicing listening skills, I often needed to:

* Repeat difficult sentences multiple times
* Correct transcript timing errors
* Edit transcript content
* Focus on a small section of a video

Existing video players did not provide the workflow I wanted, so I built this tool to support intensive listening practice.

## Technology Stack

* Python
* Flask
* HTML
* CSS
* JavaScript
* YouTube IFrame Player API

## Project Structure

```text
ListeningTrainer/
├── app.py
├── templates/
│   └── index.html
├── subtitle/
├── README.md
├── LICENSE
└── requirements.txt
```

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python app.py
```

Open:

```text
http://localhost:8000
```

## Roadmap

Planned features:

* Progress tracking
* Automatic subtitle download
* Transcript search
* Vocabulary bookmarking
* Support for additional video and audio sources

## License

MIT License
