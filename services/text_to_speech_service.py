from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play


def speak_text(text: str) -> None:
    tts = gTTS(text=text, lang='en')
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    speech = AudioSegment.from_file(fp, format="mp3")
    play(speech)

    #to jest nowy komentarz, 19:01
    #komentarz 19:36
    #komentarz sfsfs

