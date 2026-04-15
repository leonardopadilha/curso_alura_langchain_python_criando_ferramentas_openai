import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from pydantic import Field, BaseModel
from dotenv import load_dotenv
from langchain.globals import set_debug

set_debug(False)

load_dotenv()

class Destino(BaseModel):
    cidade: str = Field("A cidade recomendada para visitar")
    motivo: str = Field("motivo pelo qual é interessante visitar essa cidade")

parseador = JsonOutputParser(pydantic_object=Destino)

modelo = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5
)

prompt_cidade = PromptTemplate(
    template="""
    Sugira uma cidade dado o meu interesse por {interesse}. {formato_de_saida}
    """,
    input_variables=["interesse"],
    partial_variables={"formato_de_saida": parseador.get_format_instructions()}
)

cadeia = prompt_cidade | modelo | parseador

"""
prompt = modelo_de_prompt.format(
    dias=numero_de_dias,
    numero_criancas=numero_criancas,
    atividade=atividade
)
"""

resposta = cadeia.invoke({ "interesse": "praia" })
print(resposta)

