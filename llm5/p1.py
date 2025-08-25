import streamlit as st
from langchain.agents import load_tools, initialize_agent, AgentType
from MyLCH import getOpenAI, getGenAI

st.sidebar.markdown("Clicked Page1")
st.markdown("Page1")

text = st.text_area(label="질문입력", placeholder="질문을 입력하세요")

if st.button("SEND"):
    if text:
        st.info(text)
        openllm = getOpenAI()

        tools = load_tools(['wikipedia'], llm=openllm)

        agent = initialize_agent(
            tools,
            openllm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=False
        )
        st.info(agent.run(text))

    else:
        st.info("질문을 입력하세요")