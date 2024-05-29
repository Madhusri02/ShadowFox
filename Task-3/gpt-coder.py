import streamlit as st
from clarifai.client.model import Model
from linkgen import search_youtube_videos 
from dotenv import load_dotenv
import os

PATH_ID = os.getenv("PATH_ID")
OAUTH_ID = os.getenv("OAUTH_ID") 

st.set_page_config(
    page_title="GPT-CODER :)",
    page_icon="🚀",
    layout="wide",
)

# ui for streamlit application
sidebar = st.sidebar
sidebar.title("Pages")
sidebar.write("- Chatbot")
sidebar.write("- About us")
bg_img  = """
<style>
[data-testid="stAppViewContainer"]{
    background-color : #1B1A55;
}
</style>
 """
st.title("⭐GPT-CODER⭐")
st.markdown(bg_img , unsafe_allow_html=True)

# prompt = st.text_input("Enter your queries below:")
def app():
    # getting user prompt from the user
    prompt = st.text_input("Enter your queries below:")
    while(prompt):
        x = st.button('Submit', key="x")
        try : 
            if x:
                #  getting response for the user input from the gpt-4-turbo
                model_url="https://clarifai.com/openai/chat-completion/models/gpt-4-turbo"
                model_prediction = Model(url=model_url,pat=PATH_ID).predict_by_bytes(prompt.title().encode(), input_type="text")  
                st.write(model_prediction.outputs[0].data.text.raw)
                st.write("Video references for your usage")
                video_link = search_youtube_videos(prompt , 5)
                print(video_link)
                for i in video_link:
                    st.write(i)
        except:
            if x:
                model_url="https://clarifai.com/openai/chat-completion/models/gpt-4-turbo"
                model_prediction = Model(url=model_url,pat=PATH_ID).predict_by_bytes(prompt.title().encode(), input_type="text")  
                st.write(model_prediction.outputs[0].data.text.raw)
                # st.write("Vide references for your usage")
                # video_link = search_youtube_videos(prompt , 5)
                # for i in video_link:
                #     st.write(i)
            

if __name__ == "__main__":
    app()
    
# st.write("Enter your queries below:")


