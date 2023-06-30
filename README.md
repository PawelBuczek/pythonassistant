# pythonassistant

Playing around with ChatGPT API and stuff, not meant to be a fully functional application.  
(but worked as of June 2023)  

**Instalation:**  
1. Download this repo onto your local machine  

2. Make sure you have `python (3)` and `pip` installed.  

3. Make sure your `pip` and `pip setuptools` are upgraded   

3. If required on your machine, open command line and run below commands to install all necessary packages:  
`pip3 install flask flask_cors SpeechRecognition openai gtts pydub` 
`pip install git+https://github.com/openai/whisper.git` 

4. Go to \services\chat_gpt_service.py file and replace `yourChatGPTKey` placeholder with your actual ChatGPT key  
*(you can create it at https://platform.openai.com/account/api-keys if you have an account on OpenAI)*

5. run app.py  

6. open frontend_starting_button.html with any browser you like and click the button  