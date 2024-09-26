import streamlit as st
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.llms import Ollama

# Initialize the language model
llm = Ollama(model="llama3.2", temperature=0)


def process_youtube_url(url, question):
    try:
        # Load YouTube transcript
        loader = YoutubeLoader.from_youtube_url(url)
        docs = loader.load()

        transcript = docs[0].page_content

        # Create the prompt
        prompt = f"""Answer the user question based on the provided transcript from a YouTube video. \
        Transcript: ```{transcript}```
        User question: {question}"""

        # Generate response
        response = llm.invoke(prompt)

        return response
    except Exception as e:
        return f"An error occurred: {str(e)}"


# Streamlit UI
st.title("YouTube Video Q&A")

# Input for YouTube URL
youtube_url = st.text_input("Enter YouTube URL:")

# Input for user question
user_question = st.text_input("Enter your question about the video:")

if st.button("Get Answer"):
    if youtube_url and user_question:
        with st.spinner("Processing..."):
            answer = process_youtube_url(youtube_url, user_question)
            st.write("Answer:")
            st.write(answer)
    else:
        st.warning("Please enter both a YouTube URL and a question.")

# Display some usage instructions
st.markdown(
    """
### How to use:
1. Enter a valid YouTube URL in the first text box.
2. Type your question about the video in the second text box.
3. Click the "Get Answer" button to receive an answer based on the video content.
"""
)
