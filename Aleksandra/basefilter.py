#not related to simple filters
#should work, but not tested
import os
import random
from corpus import Corpus 

class BaseFilter:
    def __init__(self, directory_path=None, filter_output = None, file="!truth.txt"):
  
        self.directory_path = directory_path
        self.filter_output = filter_output
        self.file = file
    
    def test(self):
        file = os.path.join(self.directory_path, self.file)
        with open(file, "wt", encoding="utf-8") as f:
            first_iteration = True
            for email_name, _ in Corpus(self.directory_path).emails():
                if not first_iteration:
                    f.write("\n")
                first_iteration = False
                
                if self.filter_output is None:
                    self.filter_output = random.choice(["SPAM", "OK"])
                
                f.write(f'{email_name} {self.filter_output}')

                
    