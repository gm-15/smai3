import streamlit as st

page_main = st.Page("main.py", title="Main Page", icon="📍")
page_1 = st.Page("p1.py", title="Page 1", icon="✨")
page_2 = st.Page("p2.py", title="Page 2", icon="✨")

page = st.navigation([page_main,page_1,page_2])

page.run()