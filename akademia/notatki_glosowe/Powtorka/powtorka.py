from pydub import AudioSegment
from dotenv import dotenv_values
from openai import OpenAI
import hashlib
import io

# jak wczytać plik audio
audio = AudioSegment.from_mp3("plik.mp3")

# jak sprawdzić długość pliku audio
duration = audio.duration_seconds
print(f"Długość pliku audio: {duration} sekund")

# jak przekonwertować plik audio do formatu WAV
audio.export("plik.wav", format="wav")

# jak powtórzyć audio 4x
audio_repeated = audio * 4
audio_repeated.export("plik_repeated.mp3", format="mp3")

# jak nałożyć dwa pliki audio na siebie
audio1 = AudioSegment.from_mp3("plik1.mp3")
audio2 = AudioSegment.from_mp3("plik2.mp3")

audio_overlay = audio1.overlay(audio2)
audio_overlay.export("plik_overlay.mp3", format="mp3")

# jak zwiększyć głośność
audio += 10
audio.export("plik_louder.mp3", format="mp3")

# jak odtworzyć pierwsze 5 sekund pliku audio
audio_first_5 = audio[:5000]
audio_first_5.export("plik_first_5.mp3", format="mp3")

# jak połączyć dwa pliki dźwiękowe
audio1 = AudioSegment.from_mp3("plik1.mp3")
audio2 = AudioSegment.from_mp3("plik2.mp3")
audio_combined = audio1 + audio2
audio_combined.export("plik_combined.mp3", format="mp3")



# jak pracować z embeddingsami
config = dotenv_values(".env")
openai_client = OpenAI(api_key=config["OPENAI_API_KEY"])
result = openai_client.embeddings.create(
    input = [
        "This is a test sentence for generating embeddings using OpenAI's API.",
        "This is another test sentence for generating embeddings using OpenAI's API.",
        "This is a third test sentence for generating embeddings using OpenAI's API."
    ],
    model = "text-embedding-3-large"
)

# jak użyć modelu whisper-1
with open("audio.mp3", "rb") as f:
    transcript = openai_client.audio.transcriptions.create(
        file=f,
        model="whisper-1",
        response_format="verbose_json"
    )



# jak użyć MD5
md5_value = hashlib.md5(b"Hello, world!")
hash_value = md5_value.hexdigest()
print(f"MD5 hash: {hash_value}")


# jak użyć modułu io

# tworzymy obiekt BytesIO
bio = io.BytesIO()
# zapisujemy dane binarne do obiektu
bio.write(b"Hello, world!")
# przesuwamy wskaźnik na początek obiektu
bio.seek(0)
# odczytujemy dane binarne z obiektu
print(bio.read())