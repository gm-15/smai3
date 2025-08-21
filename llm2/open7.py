import urllib

from myLLM.MyApi import openAiModel


def test(prompt):
    openModel = openAiModel()
    response = openModel.images.create_variation(
        model="dall-e-2",
        image=open(prompt, "rb"),
        n=3,
        size="1024x1024"
    )
    for n, data in enumerate(response.data):
        print(n)
        print(data.url)
        name = f"img/dogcat_clone_{n}.png"
        urllib.request.urlretrieve(data.url, name)


if __name__ == "__main__":
    prompt = "img/dogcat.png"
    test(prompt)