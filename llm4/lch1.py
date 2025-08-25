from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from numpy.ma.core import product

from MyLCH import getOpenAI
from MyLCH import getGenAI

# def test(txt):
#     template = "{prompt}를 홍보하기위한 문구를 만들어줘"
#     prompt = PromptTemplate(
#         input_variables=["product"],
#         template=template
#     )
#     print(prompt.format(product=txt))

if __name__=='__main__':
    txt ="카메라"
    template = "{product}를 홍보하기위한 문구를 만들어줘"
    prompt = PromptTemplate(
        input_variables=["product"],
        template=template
    )
    print(prompt.format(product=txt))

    openllm = getOpenAI()
    genllm = getGenAI()

    openchain = LLMChain(llm = openllm, prompt= prompt)
    genchain = LLMChain(llm = genllm, prompt=prompt)

    print(openchain.run("카메라"))
    print(genchain.run("카메라"))