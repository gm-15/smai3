import os
import time
import streamlit as st
from PIL import Image

from myLLM import makeAudio, makeMsg, progressBar, openAiModelArg

# Sidebar
st.sidebar.markdown("Clicked Page 8")

# Page
st.title("Page 8")
system = st.text_input("SYSTEM", placeholder="system을 입력")
text = st.text_input("질문 입력", placeholder="질문을 입력하세요")
if st.button("SEND"):
    if text and system:
        #음성으로 플레이하고
        #OpenAi 물어보고 결과를 받는다
        makeAudio(text, "temp.mp3")
        st.audio("audio/temp.mp3", autoplay=True)

        st.info(f"{system}에게 다음과 같이 문의합니다. {text}")
        msg = makeMsg(system, text)
        my_bar = progressBar("Operation in progress. Please wait.")
        result = openAiModelArg("gpt-4o", msg)
        my_bar.empty()

        #결과를 음성으로 플레이하고
        #결과 내용을 화면에 출력한다.
        makeAudio(result, "result.mp3")
        st.audio("audio/result.mp3", autoplay=True)
        st.info(result)
    else:
        st.audio("audio/retry.mp3",autoplay=True)
        st.info("입력하세요")