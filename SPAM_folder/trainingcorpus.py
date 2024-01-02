import os
from corpus import Corpus

class TrainingCorpus:
    def __init__(self, directory_path):
        # Initialize the corpus object for training, indicating the path to the directory
        self.directory_path = directory_path

    def get_class(self, email_filename):
        # Get the classification (SPAM or OK) for the specified filename from the file "!truth.txt"
        file_path = os.path.join(self.directory_path, "!truth.txt")
        with open(file_path, "rt", encoding="utf-8") as f:
            for line in f:
                filename, classification = line.strip().split()
                if filename == email_filename:
                    return classification
        return None
    
    def is_ham(self, email_filename):
        # Checking if an email with file name is "ham" (OK)
        email_class = self.get_class(email_filename)
        return email_class == "OK"
    
    def is_spam(self, email_filename):
        # Checking if an email with file name is "spam"
        email_class = self.get_class(email_filename)
        return email_class == "SPAM"
        
    def spams(self):
        # Generator method returning pairs (filename, email body) for each spam email in the training corpus
        for filename, content in Corpus(self.directory_path).emails():
            if self.is_spam(filename):
                yield filename, content
    
    def hams(self):
        for filename, content in Corpus(self.directory_path).emails():
                    # Метод-генератор, возвращающий пары (имя файла, тело письма) для каждого ham-письма в корпусе обучения
            if self.is_ham(filename):
                yield filename, content