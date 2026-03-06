import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()

arquivo_original = open("./media/original.mp3", mode="rb")

transcricao = client.audio.transcriptions.create(
    model="whisper-1",
    language="pt",
    response_format="text",
    file=arquivo_original,
)

print(transcricao)