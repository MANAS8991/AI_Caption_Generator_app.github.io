import requests
import streamlit as st

API_URL_Semantics = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
API_URL_Caption = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"

headers = {"Authorization": ""}

def generate_semantics(file):
    response = requests.post(API_URL_Semantics, headers=headers, data=file)
    return response.json()[0]["generated_text"]

def generated_caption(payload):
    response = requests.post(API_URL_Caption, headers=headers, json=payload)
    return response.json()[0]["generated_text"]

# st.title("Image Captioning")
st.image('a1.png', use_column_width=True)

file= st.file_uploader("Upload an Image", type=["jpg","jpeg","png"])

if file:
    col1,col2= st.columns(2)
    with col1:
        st.image(file, use_column_width=True)
    with col2:
        with st.spinner("Generating Semantics..."):
            semantics= generate_semantics(file)

        with st.spinner("Generating Caption..."):
            prompt_dic={"inputs": f"Question: Convert the following semantics"
                        f" '{semantics}' to an instagram caption for my post."
                        f"Make sure to add hash tags and emojis."
                        f" Answer: "}
            caption_raw= generated_caption(prompt_dic)
            st.subheader("Caption")

            caption= caption_raw.split("Answer: ")[1]

            style= """
                   <style>
                    .fancy-text {
                        padding: 20px;
                        border-radius: 15px;
                        border: 2px solid #ccc;
                        box-shadow: 5px 5px 15px #aaa;
                    }
                   </style>
                       """
            fancy_text= f"<div class='fancy-text'>{caption}</div>"

            st.markdown(style, unsafe_allow_html=True)
            st.markdown(fancy_text, unsafe_allow_html=True)
