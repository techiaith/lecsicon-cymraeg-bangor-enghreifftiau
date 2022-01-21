import os
import wget

from collections import defaultdict

WORD_FREQUENCIES_URL='https://raw.githubusercontent.com/techiaith/geiriau-mwyaf-aml/main/vocab.cy.2500.frequencies.tsv'
WORD_FREQUENCIES_FILENAME='vocab.cy.2500.frequencies.tsv'

class Frequencies(object):

    def __init__(self):
        self.word_frequencies = defaultdict(list)
        for w,f in self.read_frequencies_file():
            self.add(w,f)

    def read_frequencies_file(self):

        def download_frequencies():
            wget.download(WORD_FREQUENCIES_URL)

        def parse_entry(freq_entry):
            f = freq_entry.rstrip().split('\t')
            return f[0], int(f[1])

        if not os.path.isfile(WORD_FREQUENCIES_FILENAME):
            print ("Llwytho'r amlder geiriau i lawr..")
            download_frequencies()

        with open(WORD_FREQUENCIES_FILENAME, 'r', encoding='utf-8') as frequencies_file:
            for freq in frequencies_file:
                wordform, frequency = parse_entry(freq)
                yield (wordform, frequency)

    def add(self, wordform, frequency):
        self.word_frequencies[wordform]=frequency

    def get_frequency(self, word):
        if word in self.word_frequencies:
            return self.word_frequencies[word]
        else:
            return 0


