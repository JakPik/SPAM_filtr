import os
from corpus import Corpus

class TrainingCorpus:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def get_class(self, email_filename):
        file_path = os.path.join(self.directory_path, "!truth.txt")
        with open(file_path, "rt", encoding="utf-8") as f:
            for line in f:
                filename, classification = line.strip().split()
                if filename == email_filename:
                    return classification
        return None
    
    def is_ham(self, email_filename):
        email_class = self.get_class(email_filename)
        return email_class == "OK"
    
    def is_spam(self, email_filename):
        email_class = self.get_class(email_filename)
        return email_class == "SPAM"
        
    def spams(self):
        for filename, content in Corpus(self.directory_path).emails():
            if self.is_spam(filename):
                yield filename, content
    
    def hams(self):
        for filename, content in Corpus(self.directory_path).emails():
            if self.is_ham(filename):
                yield filename, content