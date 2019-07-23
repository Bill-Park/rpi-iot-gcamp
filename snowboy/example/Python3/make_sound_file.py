import pyaudio
import wave
import audioop
import math
import os

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.mp3"

def main(file_name = "output.mp3") :
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    print("* recording")

    frames = []
    volume_count = 0

    while volume_count < 35 :
        data = stream.read(CHUNK)
        frames.append(data)
        rms = audioop.rms(data, 2)
        volume = 20 * math.log10(rms)
        print(volume)
        if volume < 61 :
            volume_count += 1
        else :
            volume_count = 0

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return file_name

if __name__ == "__main__" :
    file_name = main()
    os.system("aplay {}".format(file_name))
