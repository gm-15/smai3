from langchain.model_laboratory import ModelLaboratory
from MyLCH import getOpenAI
from MyLCH import getGenAI



if __name__=='__main__':
    openllm = getOpenAI()
    genllm = getGenAI()

    model_lab = ModelLaboratory.from_llms([openllm,genllm])
    model_lab.compare("천안 맛집 알려줘?")