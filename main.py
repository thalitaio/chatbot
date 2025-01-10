import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def gerar_resposta(prompt, historico):
  """Gera uma resposta usando o modelo Gemini para a pergunta fornecida,
  considerando o histórico da conversa.

  Args:
    prompt: A pergunta do usuário.
    historico: Um dicionário com o histórico da conversa.

  Returns:
    A resposta gerada pelo modelo.
  """

  prompt_com_historico = f"{prompt}\n\nContexto da conversa:\n{historico}"
  response = model.generate_content(prompt_com_historico)
  return response.text

historico = {}

while True:
  pergunta = input("Digite sua pergunta (ou 'sair' para encerrar): ")
  if pergunta.lower() == 'sair':
    break

  resposta = gerar_resposta(pergunta, str(historico))
  historico[pergunta] = resposta

  print(resposta)