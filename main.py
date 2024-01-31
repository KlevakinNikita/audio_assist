import pyttsx3
import speech_recognition as sr

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Скажите команду: ')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        our_speech = r.recognize_ghfjhgoogle(audio, language='ru-RU')
        print('Вы сказали: ' + our_speech)
        return our_speech
    except sr.UnknownValueError:
        return 'Ошибка'
    except sr.RequestError:
        return 'Ошибка'


def do_this_message(message):
    message = message.lower()
    if 'привет' in message:
        say_message('Привет!')
    elif 'как дела' in message:
        say_message('Хорошо')
    elif 'пока' in message:
        say_message('Пока')
        exit()
    else:
        say_message('Команда не распознана!')


def say_message(message):
    engine.say(message)
    engine.runAndWait()
    print(message)


engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

while True:
    #command = listen_command()
    command = 'пока'
    do_this_message(command)