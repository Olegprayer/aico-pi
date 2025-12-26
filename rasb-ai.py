from google import genai
import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import time
from gtts import gTTS

import vlc

text = "hello, im ximunca"
tts = gTTS(text=text, lang='en')
tts.save("response.wav")


instance = vlc.Instance('--no-video')
player = instance.media_player_new()

media = instance.media_new('response.mp3')
player.set_media(media)


player.play()

state = player.get_state()
print(f"Поточний стан: {state}")





# Frequency = 44100
# seconds = 5

# print("start talking")

# records = sd.rec(int(Frequency * seconds), samplerate=Frequency, channels=1)
# sd.wait()

# # print(f"{records}")

# write('voice.wav', Frequency, records)



# voice_recognition = whisper.load_model("tiny")
# vtt = voice_recognition.transcribe("voice.wav")
# print(str(vtt))
# time.sleep(4)
# # AI-Module
# client = genai.Client(api_key = "AIzaSyCbkix5GWP0Pz0mZcu9fF3C1pUh1512uc4")

# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents=f"{vtt}"
# )

# print(response.text)


