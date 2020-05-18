import requests
import json
import pyttsx3
import speech_recognition as sr
import re
import threading
import time

API_KEY = "taqCsiGqTyOq"
PROJECT_TOKEN = "ti6sVYWTYboW"
RUN_TOKEN = "tQS9TX70Qsf8"

class Data:
    def __init__(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key": self.api_key
        }
        self.get_data()

    def get_data(self):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data',
                                params=self.params)
        data = json.loads(response.text)
        self.data = data

    def get_total_cases(self):
        data = self.data['total']
        for content in data:
            if content['name'] == "Coronavirus Cases:":
                return content['value']

    def get_total_deaths(self):
        data = self.data['total']
        for content in data:
            if content['name'] == "Deaths:":
                return content['value']
        return "0"

    def get_country_data(self, country):
        data = self.data['country']
        for content in data:
            if content['name'].lower() == country.lower():
                return content
        return "0"


data = Data(api_key=API_KEY, project_token=PROJECT_TOKEN)

def speak(text):
	engine = pyttsx3.init()
	engine.say(text)
	engine.runAndWait()

speak("hello")