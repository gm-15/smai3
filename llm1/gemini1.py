from myLLM.MyApi import geminiModel
import google.generativeai as genai
from dotenv import load_dotenv
import os

def test(user_message):
    model = geminiModel()
    load_dotenv()
    chat = model.start_chat(history=[])
    response = chat.send_message(user_message)
    print("Gemini:", response.text)


if __name__ == "__main__":
    # while True:
    #     txt = input("질문을 입력하세요(q)")
    #     if txt =="q":
    #         break
    #     result = test(txt)
    #     print(result)
    print("\n--- Gemini 챗봇 시작 ---")

    while True:
        user_message = input("나: ")
        if user_message.lower() == '종료':
            break
        test(user_message)
    print("--- 챗봇 종료 ---")



