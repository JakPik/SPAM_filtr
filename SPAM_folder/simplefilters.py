import random
from basefilter import BaseFilter

class NaiveFilter(BaseFilter):
    def train(self, folder_path):
        pass
    
    def compute_result(self, body):
        return "OK"
    
class RandomFilter(BaseFilter):
    def train(self, folder_path):
        pass
    
    def compute_result(self, body):
        choice = random.randint(0, 1)
        if choice == 0:
            result = "SPAM"
        else:
            result = "OK"
        return result
    
class ParanoidFilter(BaseFilter):
    def train(self, folder_path):
        pass
    
    def compute_result(self, body):
        return "SPAM"
    
if __name__ == "__main__":
    NaiveFilter().test("./Python/SPAM_filter/test", "!prediction_ok")
    ParanoidFilter().test("./Python/SPAM_filter/test", "!prediction_spam")
    RandomFilter().test("./Python/SPAM_filter/test", "!prediction_rand")
