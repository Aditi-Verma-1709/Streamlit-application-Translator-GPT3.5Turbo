#  Multilingual Translation Streamlit App

This is a **Streamlit** application that leverages **LangChain** and **OpenAI's GPT-3.5 Turbo** to provide translation and audio playback for various text inputs.

---

##  Features

- Uses **LangChain** for working with Large Language Models.
- **Model used**: `GPT-3.5 Turbo`
- Accepts both **text input** and **file uploads**.
- Supports file types: `.pdf`, `.txt`, `.json`, `.csv`
- Translates content into the selected target language.
- Provides **text** and **audio output** of the translated text.

---

##  Installation

Before running the application, ensure all required packages are installed:

```bash
pip install -r requirements.txt

> ** Note:**  
> Replace the placeholder API key (`Sample_API_Key`) with your actual **OpenAI API key**.  
> You can set it using environment variables or a `.env` file depending on how your project is configured.


##  To launch the application, use the following command in your terminal:

```bash
streamlit run Project_app.py
