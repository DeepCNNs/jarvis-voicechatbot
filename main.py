from src.speech_to_text import SpeechToText
from src.text_to_speech import TextToSpeech
from src.chatgpt_client import ChatGPTClient
from src.utils import record_audio, save_audio
from sounddevice import play, wait
from scipy.io.wavfile import write
import subprocess
import ffmpeg
import soundfile as sf


stt = SpeechToText()
tts = TextToSpeech()
gpt_client = ChatGPTClient()

recording = record_audio()
recording.export("out.wav", "wav")
# write('output.wav', 44100, recording)  # Save as WAV file
# text = stt.speech_to_text_audio(recording)
# text = stt.speech_to_text_file('output.wav')
# response = gpt_client.get_response(text)
# print(response)
# speech = tts.text_to_speech(response)
# save_audio("response.wav", speech)
# data, fs = sf.read("response.wav", dtype='float32')
# play(data, fs)
# status = wait()  # Wait until file is done playing
