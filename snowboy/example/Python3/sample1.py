import snowboydecoder
import sys
import signal
import make_sound_file
import os
from naver_api import stt, tts
import weather_api
import serial

interrupted = False

ser = serial.Serial("/dev/ttyACM0", 9600)
led_on_str = "[led on\r\n"
led_off_str = "[led off\r\n"

def test() :
    print("hi")
    snowboydecoder.play_audio_file()
    detector.terminate()

    file_name = make_sound_file.main()
    return_text = stt.main(file_name)
    print(return_text)

    if return_text.find("안녕") != -1 :
        file_name = tts.main("안녕하세요")
        os.system("mpg123 {}".format(file_name))

    elif return_text.find("날씨") >= 0 :
        temp, humi = weather_api.main()
        weather_text = "온도는 {}도, 습도는 {}% 입니다.".format(temp, humi)
        file_name = tts.main(weather_text)
        os.system("mpg123 {}".format(file_name))

    elif return_text.find("조명") != -1 :
        if return_text.find("밝게") != -1 :
            ser.write(led_on_str.encode())
        elif return_text.find("어둡게") != -1 :
            ser.write(led_off_str.encode())

    detector.start(detected_callback=test,
        interrupt_check=interrupt_callback,
        sleep_time=0.03)

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)

model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.7)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=test,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
