from PIL import Image

from myLLM.MyApi import geminiModel

def test():
    img = Image.open("img/1-1.png")
    model = geminiModel()
    response = model.generate_content(["제시한 사진을 3문장 이내의 한국어로 설명해줘",img])
    print(response.text)


if __name__ == "__main__":
    test()