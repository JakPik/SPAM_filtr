from basefilter import BaseFilter
from trainingcorpus import TrainingCorpus
from corpus import Corpus

class MyFilter(BaseFilter):

    def __init__(self):
        # Initialize a filter object inherited from the base filter
        super().__init__()
        # Initialize lists to store senders and subjects of spam letters
        self.spam_senders = []
        self.spam_subjects = []


    def train(self, directory_path):
        # Train the filter based on the training corpus provided in the specified directory
        training_corpus = TrainingCorpus(directory_path)
        for name, body in Corpus(directory_path).emails():
            # Check the class label for each letter
            if training_corpus.get_class(name) == "SPAM":
                # Extract the sender and subject of a letter
                sender = self.find_sender(body)
                subject = self.find_subject(body)
                # Add unique senders and subjects of spam letters to the corresponding lists
                if sender is not None and sender not in self.spam_senders:
                    self.spam_senders.append(sender)
                if subject is not None and subject not in self.spam_subjects:
                    self.spam_subjects.append(subject)
 
                
    def compute_result(self, body):
        count = 0
        # Checking whether the sender and subject of the letters are in the list of spam senders and spam subjects
        count += self.check_for_sender(body, self.spam_senders) 
        count += self.check_for_subject(body, self.spam_subjects)
        # Return a result based on a counter
        if count != 0:
            return "SPAM"
        else:
            return "OK"

 