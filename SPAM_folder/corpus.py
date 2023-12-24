import os

class Corpus:
    def __init__(self, directory_path):
        self.mail_folder_path = directory_path

    def emails(self):
        for filename in os.listdir(self.mail_folder_path):
            if filename.startswith('!'):
                continue
            file_path = os.path.join(self.mail_folder_path, filename)
            with open(file_path, 'r', encoding="utf-8") as f:
                body = f.read()

            yield filename, body