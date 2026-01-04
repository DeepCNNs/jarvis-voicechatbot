import time

from google.cloud import speech
from google.oauth2 import service_account
import io


class SpeechToText:
    def __init__(self):
        # Creates google client
        credentials = service_account.Credentials.from_service_account_file(
            "/home/adity/PycharmProjects/jarvis/config/key.json")

        self.client = speech.SpeechClient(credentials=credentials)
        self.config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            audio_channel_count=1,
            language_code="en-IN",
            sample_rate_hertz=44100,
        )

    def speech_to_text_file(self, file_name):
        # Loads the audio file into memory
        with io.open(file_name, "rb") as audio_file:
            content = audio_file.read()
            print(content)
            audio = speech.RecognitionAudio(content=content)

        # Sends the request to google to transcribe the audio
        t = time.time()
        response = self.client.recognize(request={"config": self.config, "audio": audio})
        print("time taken: ", time.time() - t)

        # Reads the response
        for result in response.results:
            print("Transcript: {}".format(result.alternatives[0].transcript))

        return result.alternatives[0].transcript

    def speech_to_text_audio(self, audio):
        audio = speech.RecognitionAudio(content=audio)
        # Sends the request to google to transcribe the audio
        t = time.time()
        response = self.client.recognize(request={"config": self.config, "audio": audio})
        print("time taken: ", time.time() - t)

        # Reads the response
        for result in response.results:
            print("Transcript: {}".format(result.alternatives[0].transcript))

        return result.alternatives[0].transcript
