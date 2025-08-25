from gtts import gTTS
import io
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI  # ✅ New import
from langchain_core.runnables import RunnableSequence
# Step 1: Create prompt template
translation_template = PromptTemplate(
    input_variables=["text", "target_language"],
    template="Translate the following text into {target_language}:\n\n{text}"
)
# Step 2: Load LLM (gpt-3.5-turbo)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.8)
# Step 3: Combine with RunnableSequence (replacement for LLMChain)
trans_chain = translation_template | llm

def translator(output_language,text):
    result = trans_chain.invoke({
    "text": text,
    "target_language": output_language
})
    return result.content



def audio_converter(text):
    tts = gTTS(text)
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)  # Important: reset to beginning of stream
    return mp3_fp
