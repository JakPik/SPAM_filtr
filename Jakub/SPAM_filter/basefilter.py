import os
import random
from corpus import Corpus

class BaseFilter:
    def __init__(self, folder_path, input = None, file = "!truth.txt"):
        self.result = input
        self.input = input
        self.folder_path = folder_path
        self.file = file

    def write_to_file(self):
        first = False
        file = os.path.join(self.folder_path, self.file)
        with open(file, "w", encoding="utf-8")as f:
            for _ in Corpus(self.folder_path).emails():
                if(first == True):
                    f.write("\n")
                if(self.input == None):
                    if(random.randint(0, 1) == 0):
                        self.result = "SPAM"
                    else:
                        self.result = "OK"
                first = True
                f.write(self.result)