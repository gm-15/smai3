import time

import streamlit as st
from myLLM import geminiTxt, progressBar

# Sidebar
st.sidebar.markdown("Clicked Page 4")

# Page
st.title("Page 4 번역기")

text = st.text_area(label="질문입력:",
                    placeholder="질문을 입력 하세요")

language = st.selectbox("언어를 선택하세요", ("English", "Japanese", "Chinese"))
if st.button("SEND"):
    if text and language:
        st.info(f"선택하신 언어는 : {language}")
        st.info(text)
        my_bar = progressBar("Operation in progress. Please wait")
        result = geminiTxt(f"{language}를 이용하여 다음 문장을 번역해줘 {text}")
        my_bar.empty()
        st.info(result)

    else:
        st.info("질문을 입력 하세요")