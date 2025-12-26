from google import genai
import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import time
from gtts import gTTS
from mutagen.mp3 import MP3
import vlc

# запись запитання
Frequency = 44100
seconds = 5
print("start talking")
records = sd.rec(int(Frequency * seconds), samplerate=Frequency, channels=1)
sd.wait()
write('voice.wav', Frequency, records)


# recognition
voice_recognition = whisper.load_model("tiny")
vtt = voice_recognition.transcribe("voice.wav")
# AI-Module
client = genai.Client(api_key = "AIzaSyCbkix5GWP0Pz0mZcu9fF3C1pUh1512uc4")
response_ai = client.models.generate_content(
    model="gemini-2.5-flash", contents=f"{vtt["text"]}")


# генерація відповіді
tts = gTTS(text=response_ai.text, lang='en')
tts.save("response")
instance = vlc.Instance('--no-video')
player = instance.media_player_new()
media = instance.media_new('response')
player.set_media(media)
time_to_play = MP3("response").info.length
player.play()
time.sleep(time_to_play)


