from basefilter import BaseFilter
from trainingcorpus import TrainingCorpus
from corpus import Corpus

class MyFilter(BaseFilter):

    def __init__(self):
        super().__init__()
        self.spam_senders = []
        self.spam_subjects = []


    def train(self, directory_path):
        training_corpus = TrainingCorpus(directory_path)
        #self.subject = []
        for name, body in Corpus(directory_path).emails():
            if training_corpus.get_class(name) == "SPAM":
                sender = self.find_sender(body)
                subject = self.find_subject(body)
                if sender is not None and sender not in self.spam_senders:
                    self.spam_senders.append(sender)
                if subject is not None and subject not in self.spam_subjects:
                    self.spam_subjects.append(subject)
 
                
    def compute_result(self, body):
        count = 0
        count += self.check_for_sender(body, self.spam_senders) 
        count += self.check_for_subject(body, self.spam_subjects)
        if count != 0:
            return "SPAM"
        else:
            return "OK"

 