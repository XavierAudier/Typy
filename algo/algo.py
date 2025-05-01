# Defining the algorithm responsible for building the list of example to type
import numpy as np
import re

class TrainingAlgorithm():

    def __init__(self, example_length=3):
        self.example_length = example_length
        self.example_dict = {}

    def build_from_textfile(self, text_file_path):
        """
        Trains the algorithm based of the provided file
        """
        with open(text_file_path, 'r') as f_:
            file_str = "".join(f_.readlines())

        re.sub(r'\s+','', file_str)
        for idx in range(len(file_str)):
            token = file_str[idx:idx+self.example_length]
            if token in self.example_dict.keys():
                self.example_dict[token] += 1
            else:
                self.example_dict[token] = 1
        
        self.ranked_list = sorted([(value, key) for (key, value) in self.example_dict.items()], reverse=True)
        self.sorted_keys = [tup[1] for tup in self.ranked_list]
        self.sorted_vals = [tup[0] for tup in self.ranked_list]
        self.cum_sum_vals = np.cumsum(self.sorted_vals)
        
    def get_next_example(self):
        next_val = np.random.randint(0, self.cum_sum_vals[-1])
        next_key = self.sorted_keys[np.searchsorted(self.cum_sum_vals, next_val)]

        return next_key
