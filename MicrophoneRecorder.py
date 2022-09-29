import pyaudio
import wave
class Microphone:
    def __init__(self):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100

        self.p = pyaudio.PyAudio()

    def recordAudio(self, recordingTime, path="voice.wav"):
        stream = self.p.open(format=self.FORMAT,
                            channels=self.CHANNELS,
                            rate=self.RATE,
                            input=True,
                            frames_per_buffer=self.CHUNK)

        print("* recording")

        frames = []
        # Todo in the future instead of hard stopping at the time wait until a break then stop
        for i in range(0, int(self.RATE / self.CHUNK * recordingTime)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        self.p.terminate()

        wf = wave.open(path, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

# mic = Microphone()
# mic.recordAudio(5)