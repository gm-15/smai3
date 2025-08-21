from operator import iconcat

import streamlit as st

from myLLM import geminiTxt

#Sidebar
st.sidebar.markdown("Clicked Page 1")

#Page
st.title("Page 1")
text = st.text_area(label="질문입력", placeholder="질문을 입력하세요")

if st.button("SEND"):
    if text:
        result = geminiTxt(text)
        st.info(result)
    else:
        st.info("질문을 입력하세요")