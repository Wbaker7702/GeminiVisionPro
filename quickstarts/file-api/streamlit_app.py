import streamlit as st
import os
from google import genai
from dotenv import load_dotenv
import tempfile

# Load environment variables
load_dotenv()

st.set_page_config(page_title="Gemini File API Demo", page_icon="✨")

st.title("✨ Gemini File API Demo")
st.markdown("""
This app demonstrates how to use the Gemini File API to upload files and generate content.
""")

# API Key handling
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    api_key = st.text_input("Enter your Google API Key", type="password")

if not api_key:
    st.warning("Please enter your Google API Key to continue.")
    st.stop()

try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"Failed to initialize client: {e}")
    st.stop()

# File upload
uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg", "pdf", "csv", "txt", "mp3", "wav"])

if uploaded_file is not None:
    st.info(f"File '{uploaded_file.name}' selected.")
    
    # Display preview based on type
    if uploaded_file.type.startswith('image'):
        st.image(uploaded_file, caption='Uploaded Image', use_container_width=True)
    elif uploaded_file.type.startswith('audio'):
        st.audio(uploaded_file)
    elif uploaded_file.type == 'text/plain':
        st.text(uploaded_file.getvalue().decode("utf-8")[:500] + "...")

    prompt = st.text_area("Prompt", "Describe this file in detail.")
    
    if st.button("Generate Content", type="primary"):
        with st.spinner("Processing..."):
            tmp_file_path = None
            try:
                # Create a temporary file to save the uploaded content
                suffix = f".{uploaded_file.name.split('.')[-1]}" if '.' in uploaded_file.name else ""
                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_file_path = tmp_file.name
                
                # Upload file to Gemini
                status_placeholder = st.empty()
                status_placeholder.text("Uploading file to Gemini...")
                
                file_response = client.files.upload(
                    file=tmp_file_path,
                    config={"display_name": uploaded_file.name}
                )
                
                status_placeholder.text(f"File uploaded: {file_response.uri}")
                
                # Generate content
                status_placeholder.text("Generating content...")
                model_name = "gemini-2.0-flash"
                
                response = client.models.generate_content(
                    model=model_name,
                    contents=[prompt, file_response]
                )
                
                status_placeholder.empty()
                st.subheader("Response")
                st.markdown(response.text)
                
                # Cleanup remote file
                try:
                    client.files.delete(name=file_response.name)
                    # st.info("Remote file cleaned up.")
                except Exception as e:
                    print(f"Failed to delete remote file: {e}")
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")
            finally:
                if tmp_file_path and os.path.exists(tmp_file_path):
                    os.unlink(tmp_file_path)
