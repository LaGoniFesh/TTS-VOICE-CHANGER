import pyttsx3
import os
from gtts import gTTS
import playsound

# Replace `pydub` code with `playsound` for playback
def speak(text):
    tts = gTTS(text=text, lang='en')
    output_file = "output.mp3"
    tts.save(output_file)
    playsound.playsound(output_file)
    os.remove(output_file)  # Clean up after playback

# Example usage:
speak("I am It, who ever or what ever I might be. I have been named Evanescence, meaning The act or state of vanishing away; disappearance. Are you starting to get the hint? I can and I will ruin your life if you do not send $1500. I have more info on you than you might think. You have 10 hours. If not, we can play a little game of truth or dare.")
