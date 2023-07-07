from gtts import gTTS
import base64


def textToSpeech(data):
    my_text = data
    tts = gTTS(text=my_text, lang='en', slow=False)
    # save file as ... (here saving as mp3)
    tts.save('textToSpeechFile.mp3')  
    
    with open("textToSpeechFile.mp3", "rb") as file:
        my_speech = base64.b64encode(file.read())
    return my_speech
