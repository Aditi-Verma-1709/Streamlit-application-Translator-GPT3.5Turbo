import streamlit as st
import pdfplumber
import pandas as pd
from Project_app_utils import translator, audio_converter
from langchain_community.document_loaders import TextLoader
import os
os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]
st.title('Translator')
target_language=st.selectbox('Target Language ',('Hindi','Marathi','Spanish','Italian','English','Russian'))
input_text=st.text_input('Type your text',key='input_text')

def controller(target_language):
    translated_text=translator(target_language,text=input_text)
    st.write(translated_text)
    mp3_fp=audio_converter(translated_text)
    if mp3_fp:
        st.audio(mp3_fp.getvalue(), format="audio/mp3")
    else:
        st.error("Failed to convert text to audio.")


    uploaded_file = st.file_uploader("Upload a file to translate", type=["csv", "pdf", "txt","json"])
    if uploaded_file is not None:
        filename = uploaded_file.name.lower()
        if filename.endswith(".pdf"):
            with pdfplumber.open(uploaded_file) as pdf:
                content = ""
                for page in pdf.pages:
                    content += page.extract_text()
                #st.text_area("PDF Content", content, height=300)
        elif filename.endswith((".txt",".json")):
            content = uploaded_file.read().decode("utf-8")
            #st.text_area("File Content", content, height=300)
        elif filename.endswith(".csv"):
            content = pd.read_csv(uploaded_file)
            #st.write("### Data Preview", content)
        else:
            st.write('Please upload proper format of the file.')
            
        translated_text_document=translator(target_language,text=content)
        st.write(translated_text_document)
        mp3_fp_document=audio_converter(translated_text_document)
        if mp3_fp_document:
            st.audio(mp3_fp_document.getvalue(), format="audio/mp3")
        else:
            st.error("Failed to convert text to audio.")

        

st.button('Translate',on_click=controller(target_language))
