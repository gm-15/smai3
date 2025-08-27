from myllm.MyApi import openAiModelArg, makeMsg


def test(prompt):
    modelName = "gpt-5"
    msg = makeMsg("너는 친절한 한국어 선생님",prompt)
    result = openAiModelArg(modelName, msg)
    print(result)

if __name__ == '__main__':
    prompt = "갤럭시 s25 알려줘?"
    test(prompt)