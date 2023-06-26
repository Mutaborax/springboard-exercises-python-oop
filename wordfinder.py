
import random

file_path = "/Users/nsip/Downloads/Springboard Boot Camp/python-oo-practice/words.txt"


class WordFinder:

    def __init__(self, file_path):

        self.words = []
        with open(file_path) as file:
            for line in file:
                self.words.append(line.strip())
        print(f"{len(self.words)} words read")

    def random(self):
        '''Returns a random word from the list'''
        return random.choice(self.words)
