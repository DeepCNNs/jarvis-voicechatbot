from copy import deepcopy
import numpy
import sounddevice as sd
import pyaudio
import wave
from pydub import AudioSegment
from pydub.silence import split_on_silence
from scipy.io.wavfile import write


def record_audio():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording
    audio = AudioSegment.empty()
    found = False

    while True:
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()  # Wait until recording is finished
        write('output.wav', 44100, recording)  # Save as WAV file
        chunks = get_split_on_silence('output.wav')
        print(len(chunks))

        if len(chunks) == 0 and found:
            break

        if len(chunks) > 0:
            for chunk in chunks:
                audio += chunk
            found = True

    return audio


def save_audio(filename, audio):
    with open(filename, "wb") as out:
        out.write(audio)
        print(f'speech saved to "{filename}"')


def record_audio_1():
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 3
    filename = "output.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()


def get_split_on_silence(file):
    seg = AudioSegment.from_file(file)
    # Split track where the silence is 2 seconds or more and get chunks using
    # the imported function.
    chunks = split_on_silence(
        # Use the loaded audio.
        seg,
        # Specify that a silent chunk must be at least 2 seconds or 2000 ms long.
        min_silence_len=1000,
        # Consider a chunk silent if it's quieter than -16 dBFS.
        # (You may want to adjust this parameter.)
        silence_thresh=-16
    )

    return chunks
