import sys
import speech_recognition as sr
import whisper
import services.text_to_speech_service as text_to_speech_service
import services.chat_gpt_service as chat_gpt_service
import services.isrunning_service as isrunning_service
import os

__audio_prompt_file_location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__), "audio_prompt.wav"))


def assist():
    recognizer = sr.Recognizer()
    text_to_speech_service.speak_text("What can I help you with?")
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, 10.0)
            if not isrunning_service.is_running():
                sys.exit()
            try:
                with open(__audio_prompt_file_location__, "wb") as f:
                    f.write(audio.get_wav_data())
                model = whisper.load_model("base")
                result = model.transcribe(
                    __audio_prompt_file_location__, fp16=False, language='English')
                user_input = result["text"]
                print(f"User said: {user_input}")
            except Exception as e:
                print("Error transcribing audio: {0}".format(e))
            response = chat_gpt_service.get_response(user_input)
        text_to_speech_service.speak_text(response)
