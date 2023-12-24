import os
from corpus import Corpus

class BaseFilter:
        
    def train(self, directory_path):
        raise NotImplementedError("Implement")
    
    def test(self, directory_path):
        self.file = "!prediction.txt"
        self.write_to_file(directory_path)
    
    def compute_result(self, body):
        raise NotImplementedError("Implement")
    
    def write_to_file(self, directory_path):
        file = os.path.join(directory_path, self.file)
        with open(file, 'w', encoding="utf-8")as f:
            for name, body in Corpus(directory_path).emails():
                body = body.lower()
                f.write(f"{name} {self.compute_result(body)}\n")
                
    def find_sender(self, body):
        array = body.split()
        count = 0
        for word in array:
            if word == "from:":
                return array[count + 1]
            count += 1
        return None
    
    def find_subject(self, body):
        array = body.split()
        count = 0

        while count < len(array):
            if array[count] == "subject:":
                count += 1
                words = []

                while count < len(array) and array[count] != '\n':
                    words.append(array[count])
                    count += 1

                subject_text = " ".join(words)
                return subject_text

            count += 1

        return None
    
    def check_for_sender(self, body, sender):
        array = body.split()
        count = 0

        while count < len(array):
            if array[count] in sender:
                return 1
            else:
                count += 1
        return 0
    
    def check_for_subject(self, body, subject):
        array = body.split()
        count = 0

        while count < len(array):
            if array[count] in subject:
                return 1
            else:
                count += 1
        return 0