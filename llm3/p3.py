import time

import streamlit as st
from myLLM import geminiTxt

# Sidebar
st.sidebar.markdown("Clicked Page 3")

# Page
st.title("Page 3 프로그램 작성기")

text = st.text_area(label="질문입력:",
                    placeholder="질문을 입력 하세요")
selected_option = st.radio("언어를 선택하세요", ("java", "python", "c++"))
if st.button("SEND"):
    if text and selected_option:
        st.write(f"선택된 옵션: {selected_option}")
        # Progress Bar Start -----------------------------------------
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        # Progress Bar End -----------------------------------------

        result = geminiTxt(f"{selected_option}를 이용하여  {text}")
        my_bar.empty()
        st.code(result, language=selected_option)
    else:
        st.info("질문을 입력 하세요")