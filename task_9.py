import random


class StrandsDNA():
    def __init__(self):
        self.__all_strands = []

    def add_strands(self, strands):
        for i in strands.split():
            self.__all_strands.append(i)
        
    def get_max_strands(self):        
        self.__max_length = max(len(strand) for strand in self.__all_strands)
        self.max_strands = [strand for strand in self.__all_strands if len(strand) == self.__max_length]
        self.max_strands.sort()
        return self.max_strands


    def __str__(self):
        return self.__all_strands

    def __repr__(self):
        return self.__str__()


def generate_random_dna_sequence(length):
    dna_bases = 'ATGC'
    return ''.join(random.choice(dna_bases) for _ in range(length))


dna_sequence = ''
for _ in range(10):
    dna_sequence += generate_random_dna_sequence(random.randint(5, 10)) + ' '
print(dna_sequence.strip())

dna = StrandsDNA() 
dna.add_strands(dna_sequence)
print(dna.get_max_strands())
