# YouTube Q&A Streamlit Application

This Streamlit application allows users to ask questions about YouTube videos by providing a URL. The app uses the video's transcript to generate answers based on the content.

## Features

- Input a YouTube URL
- Ask questions about the video content
- Get AI-generated answers based on the video transcript

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher


## Installation

1. Clone this repository or download the source code.

2. Navigate to the project directory:

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Open the `app.py` file in a text editor.

2. Set up the LLM ([see here for installing Ollama](https://ollama.com))

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Your default web browser should open automatically and display the application. If it doesn't, you can manually open the URL shown in the terminal (usually `http://localhost:8501`).

3. Enter a YouTube URL in the first text input field.

4. Type your question about the video in the second text input field.

5. Click the "Get Answer" button to process your request.

6. The app will display the AI-generated answer based on the video's content.

## Troubleshooting

- Ensure that the YouTube URL is valid and the video is publicly accessible.
- Some videos may not have transcripts available, which can cause the app to fail for those specific videos.


