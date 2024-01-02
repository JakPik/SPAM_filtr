import os
from corpus import Corpus
from trainingcorpus import TrainingCorpus

class BaseFilter:
    
    def __init__(self):
        # File name to save the default predictions
        self.file = "!prediction.txt" 
        
    def train(self, directory_path):
        # Filter training method to be overridden in subclasses
        raise NotImplementedError("Implement")
    
    def test(self, directory_path):
        # Method for testing the filter and writing the results to a file
        self.write_to_file(directory_path)
    
    def compute_result(self, body):
        # Method to calculate the classification result, which should be overridden in subclasses
        raise NotImplementedError("Implement")
    
    def write_to_file(self, directory_path):
        # Method for writing predictions to a file
        file = os.path.join(directory_path, self.file)
        with open(file, "wt", encoding="utf-8")as f:
            # Iterate through the emails in the corpus and write the results to a file
            for email_name, body in Corpus(directory_path).emails():
                f.write(f"{email_name} {self.compute_result(body)}\n")
                
    def find_sender(self, body):
        # Method for searching for the sender in the text of a letter
        array = body.split()
        count = 0
        lowercased_array = [word.lower() for word in array]
        for word in lowercased_array:
            if word == "from:":
                return array[count + 1]
            count += 1
        return None
    
    def find_subject(self, body):
        # Method for searching for a subject in the text of a letter
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
    
    def check_for_sender(self, body, spam_senders):
        # Method for checking whether a sender is in the spam sender list
        sender = self.find_sender(body)
        return 1 if sender and sender in spam_senders else 0
    
    def check_for_subject(self, body, spam_subjects):
        # Method for checking if a topic is in the list of spam topics
        subject = self.find_subject(body)
        return 1 if subject and subject in spam_subjects else 0
        