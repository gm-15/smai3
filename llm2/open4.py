from myllm.MyApi import openAiModelArg, makeMsg, openAiModel


def test(prompt):
    promptMp3 = "prompt.mp3"
    model = openAiModel()
    response = model.audio.speech.create(
        model="tts-1",
        input=prompt,
        voice="alloy",
        response_format="mp3",
        speed=1.1,
    )
    response.stream_to_file(promptMp3)


    modelName = "gpt-4o"
    msg = makeMsg("너는 친절한 한국어 선생님",prompt)
    result = openAiModelArg(modelName, msg)
    print(result)

    # 결과를 음성으로 변환 하시오
    resultMp3 = "result.mp3"
    response = model.audio.speech.create(
        model="tts-1",
        input=result,
        voice="alloy",
        response_format="mp3",
        speed=1.1,
    )
    response.stream_to_file(resultMp3)


if __name__ == '__main__':
    prompt = "우간다의 수도가 어디야"
    test(prompt)