import os
import random
from corpus import Corpus

class NaiveFilter:
    def train(self, directory_path):
        pass
    
    def test(self, directory_path):
        file = os.path.join(directory_path, '!prediction.txt')
        with open(file, "w", encoding="utf-8")as f:
            for email_name, _ in Corpus(directory_path).emails():                
                 f.write(f'{email_name} OK\n')
                
class ParanoidFilter:
    def train(self, directory_path):
        pass
    
    def test(self, directory_path):
        file = os.path.join(directory_path, '!prediction.txt')
        with open(file, "w", encoding="utf-8")as f:
            for email_name, _ in Corpus(directory_path).emails():                
                 f.write(f'{email_name} SPAM\n')

class RandomFilter:
                
    def train(self, directory_path):
        pass
    
    def test(self, directory_path):
        file = os.path.join(directory_path, '!prediction.txt')
        with open(file, "w", encoding="utf-8")as f:
            for email_name, _ in Corpus(directory_path).emails():                
                 f.write(f'{email_name} {random.choice(["OK","SPAM"])}\n')

