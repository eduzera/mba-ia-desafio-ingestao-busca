import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from langchain.prompts import PromptTemplate

load_dotenv()

PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.
- Caso a resposta esteja no CONTEXTO, responda de forma clara e objetiva.
- Caso a resposta conter dados monetários, apresente os valores em Reais (R$) e por extenso.

EXEMPLOS DE PERGUNTAS NO CONTEXTO:
Pergunta: Qual o faturamento da Empresa SuperTechIABrazil?
Resposta: O faturamento foi de 10 milhões de reais.

Pergunta: Qual o ano de fundação da Empresa SuperTechIABrazil?
Resposta: A empresa foi fundada em 2010.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

def search_prompt(question=None):
    embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_MODEL","text-embedding-3-small"))

    store = PGVector(
      embeddings=embeddings,
      collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
      connection=os.getenv("DATABASE_URL"),
      use_jsonb=True,
    )
    
    results = store.similarity_search_with_score(question, k=10)
    context = "\n\n".join([doc.page_content for doc, score in results])
    
    prompt_template = PromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt_text = prompt_template.format(contexto=context, pergunta=question)

    model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)
    return model.invoke(prompt_text)