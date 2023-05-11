import pyttsx3
import time
import io
import base64

engine = pyttsx3.init()


def voice(text):
    voices = engine.getProperty('voices')
    # engine.setProperty('voice', 'te-in')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 180)

    voice_output = io.BytesIO()
    engine.save_to_file(text, voice_output)
    engine.runAndWait()

    # Reset the output stream position to the beginning
    voice_output.seek(0)
    return base64.b64encode(voice_output.getvalue()).decode()


# voice('Welcome ! My intelligent system can provide you with information on any single word , noun or sentence. Simply enter the word you want to know more about.')

