from gtts import gTTS
import base64


def textToSpeech(data):
    my_text = data

    if not my_text:
        raise ValueError("Empty text. Please provide some text.")

    tts = gTTS(text=my_text, lang='en', slow=False)
    tts.save('textToSpeechFile.mp3')

    with open("textToSpeechFile.mp3", "rb") as file:
        my_speech = base64.b64encode(file.read())

    return my_speech


    
