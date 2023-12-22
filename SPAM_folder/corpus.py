
import os
class Corpus:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def emails(self):
       
        for filename in os.listdir(self.directory_path):
     
            if filename.startswith('!'):
                continue

            file_path = os.path.join(self.directory_path, filename)
            with open(file_path, 'rt', encoding='utf-8') as f:
                
                yield filename, f.read()
                
