from flask import Flask
from flask_cors import CORS
from threading import Thread
import services.isrunning_service as isrunning_service
import assistant.assistant as assistant

api = Flask(__name__)
CORS(api)
assistThread = Thread(target=assistant.assist)


@api.route('/toggle', methods=['POST'])
def toggle_assistant():
    try:
        if isrunning_service.is_running():
            isrunning_service.mark_as_not_running()
            return "Assistent thread marked to be closed", 200
        else:
            isrunning_service.mark_as_running()
            if not assistThread.is_alive():
                globals()["assistThread"] = Thread(target=assistant.assist)
                assistThread.start()
                return "Assistent thread starting", 200
            return "Previous assistent thread still running", 200
    except:
        return "Something went wrong", 418


if __name__ == '__main__':
    isrunning_service.mark_as_not_running()
    api.run()
