import requests
import json

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

    def get_data(self):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data',
                                params=self.params)
        data = json.loads(response.text)
        return data

data = Data(api_key=API_KEY, project_token=PROJECT_TOKEN)
print(data.get_data())