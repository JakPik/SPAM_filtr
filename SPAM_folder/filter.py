from basefilter import BaseFilter
from trainingcorpus import TrainingCorpus
from corpus import Corpus

class MyFilter(BaseFilter):

    def train(self, directory_path):
        self.sender = []
        self.subject = []
        for name, body in Corpus(directory_path).emails():
            if TrainingCorpus(directory_path).get_class(name) == "SPAM":
                body = body.lower()
                self.sender.append(self.find_sender(body))
                self.subject.append(self.find_subject(body)) 
                
    def compute_result(self, body):
        count = 0
        # main errors in functions check_for_sender and check_for_subject
        count += self.check_for_sender(body, self.sender) 
        count += self.check_for_subject(body, self.subject)
        if count != 0:
            return "SPAM"
        else:
            return "OK"

    
if __name__ == "__main__":
    tests = MyFilter()
    tests.train("./Python/SPAM_filter/test")
    tests.test("./Python/SPAM_filter/test")
