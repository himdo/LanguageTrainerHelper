import pyaudio
import sys
from scipy.io.wavfile import read
import numpy as np

class PlayAudio:
    def play(self, filePath):
        try:
            samplerate, wf_data = read(filePath)

            p = pyaudio.PyAudio()
            format = None
            dtype = wf_data.dtype
            if dtype == np.dtype('float32'):
                format = pyaudio.paFloat32
            elif dtype == np.dtype('int16'):
                format = pyaudio.paInt16

            stream = p.open(format=format,
                            channels=1,
                            rate=samplerate,
                            output=True)

            stream.write(wf_data.tobytes())


            stream.stop_stream()
            stream.close()

            p.terminate()
            return True
        except:
            return False