import time

import google.cloud.texttospeech as tts
from google.oauth2 import service_account


class TextToSpeech:
    def __init__(self):
        credentials = service_account.Credentials.from_service_account_file(
            "/home/adity/PycharmProjects/jarvis/config/key.json")
        voice_name = "en-GB-Wavenet-B"
        self.client = tts.TextToSpeechClient(credentials=credentials)
        language_code = "en-GB"
        self.voice_params = tts.VoiceSelectionParams(
            language_code=language_code, name=voice_name
        )
        self.audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    def text_to_speech(self, text: str):
        text_input = tts.SynthesisInput(text=text)

        t = time.time()
        response = self.client.synthesize_speech(
            input=text_input, voice=self.voice_params, audio_config=self.audio_config
        )
        print("time taken: ", time.time() - t)

        return response.audio_content
