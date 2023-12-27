from dotenv import load_dotenv
load_dotenv() ## load all the environment variablbes from .env file

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro vision


def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        #read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type, #get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

##initalize our streamlit app

st.set_page_config(page_title="Screen shot reader")
st.header("Screen shot reader")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Chosse an image of screenshot...", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Tell me about the screenshot")

input_prompt="""
you are an expert in understanding screenshots. We will upload a screenshot image.
and you will have to anser any questions based on the uploded screeshot image.
"""

#if submit button is clicked 
if submit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The response is ")
    st.write(response)
