# Gemini File API Sample Client Code

## Background
The Gemini File API provides a simple way for developers to upload files and use them with the Gemini API in multimodal scenarios. This repository shows how to use the File API to upload an image and include it in a `GenerateContent` call to the Gemini API.


> [!IMPORTANT]
> The File API is currently in beta and is [only available in certain regions](https://ai.google.dev/available_regions).

## Quickstarts
Ready to get started? Learn the essentials of uploading files and using them in GenerateContent requests to the Gemini API:

[File API Colab](https://github.com/google-gemini/cookbook/blob/main/quickstarts/File_API.ipynb)

[Audio Colab](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Audio.ipynb)

[Video Colab](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Video.ipynb)


## Streamlit App (UI Demo)
A graphical interface is available to upload files and interact with Gemini.

```bash
# Install dependencies
pip3 install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```

## Python Sample
```
# Prepare a virtual environment for Python.
python3 -m venv venv
source venv/bin/activate

# Add API key to .env file
touch .env
echo "GOOGLE_API_KEY='YOUR_API_KEY'" >> .env

# Install dependencies.
pip3 install -U -r requirements.txt

# Run the sample code.
python3 sample.py
```

## Node.js Sample
```
# Make sure npm is installed first. 

# Add API key to .env file
touch .env
echo "GOOGLE_API_KEY='YOUR_API_KEY'" >> .env

# Install dependencies.
npm install

# Run the sample code.
npm start
```

## cURL Bash Script Sample
The following script will upload a file given the file path.
```
bash ./sample.sh -a "<YOUR_KEY>" -i "sample_data/gemini_logo.png" -d "Gemini logo"
```
