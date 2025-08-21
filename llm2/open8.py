import urllib.request

from myLLM.MyApi import openAiModel


def test(prompt):
    openModel = openAiModel()
    response = openModel.images.edit(
        model="dall-e-2",
        prompt=prompt,
        size="1024x1024",

        n=1,
        image=open("img/sample.png","rb"),
        mask=open("img/sample-mask.png","rb")
    )
    image_url = response.data[0].url
    print(image_url)
    urllib.request.urlretrieve(image_url, "sample2.png")

if __name__ == "__main__":
    prompt = "크리스마스 트리를 넣어줘"
    test(prompt)