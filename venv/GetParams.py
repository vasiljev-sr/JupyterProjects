import json


class GetParams:
    def __init__(self, file_name):
        self.file_name = file_name
        if self.file_name.endswith('.json'):
            with open(self.file_name, "r") as reader:
                self.data = json.load(reader)

    def get_shot_rate(self):
        return self.data['shot rate']

    def get_path(self):
        return self.data['path']

    def get_sleep_time(self):
        return self.data['sleep time']
