from youtube_transcript_api import YouTubeTranscriptApi

import re


# -------------------------------

# Função para extrair o ID do vídeo da URL

# -------------------------------

def extrair_video_id(url):

"""

Extrai o ID do vídeo do YouTube

Ex: https://www.youtube.com/watch?v=ABCD1234 → ABCD1234

"""

match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)

return match.group(1) if match else None


# -------------------------------

# Função para obter a legenda do vídeo

# -------------------------------

def obter_transcricao(video_id):

"""

Usa a API do YouTube Transcript para pegar a legenda.

Retorna o texto concatenado.

"""

try:

transcricao = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt', 'en'])

texto_completo = " ".join([item['text'] for item in transcricao])

return texto_completo

except Exception as e:

print("Erro ao obter transcrição:", e)

return None


# -------------------------------

# Função para simular o resumo (IA falsa)

# -------------------------------

def resumir_simulado(texto):

"""

Simula um resumo ao selecionar os 5 primeiros parágrafos ou frases longas.

"""

frases = re.split(r'(?<=[.!?]) +', texto)

resumo = " ".join(frases[:5])

return resumo if resumo else "Resumo não disponível."


# -------------------------------

# Programa principal

# -------------------------------

def main():

print("Resumo de Vídeo do YouTube (IA Simulada)")

url = input("Digite a URL do vídeo do YouTube: ")


# Extrair ID

video_id = extrair_video_id(url)

if not video_id:

print("URL inválida.")

return


# Obter legenda

print(" Extraindo legendas...")

texto = obter_transcricao(video_id)

if not texto:

print("Não foi possível obter a legenda.")

return


# Gerar resumo simulado

print("Gerando resumo (simulação)...")

resumo = resumir_simulado(texto)


print("\nResumo gerado:\n")

print(resumo)


# Executa o programa

if _name_ == "_main_":

main()