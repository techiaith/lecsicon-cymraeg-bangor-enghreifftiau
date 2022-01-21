import os
import wget

from os import listdir
from zipfile import ZipFile
from collections import defaultdict

import trie

LEXICON_URL='https://raw.githubusercontent.com/techiaith/lecsicon-cymraeg-bangor/main/lecsicon_cc0.zip'
LEXICON_FILENAME='lecsicon_cc0.txt'


class Lexicon(object):

    def __init__(self):
        self.lex_trie = trie.Trie()

        self.wordform_lookup = defaultdict(list)
        self.lemma_lookup = defaultdict(list)

        for w,l,p,f in self.read_lexicon_file():
            self.add(w,l,p,f)

        self.spellings = defaultdict(list)
        self.initialise_spellings_cache()
        #self.add('mae hen wlad fy nhadau', 'mae hen gwlad fy tadau', 'PHRASE', '')


    def read_lexicon_file(self):

        def download_lexicon():
            wget.download(LEXICON_URL)

            if os.path.isfile('lecsicon_cc0.zip'):
                z=ZipFile('lecsicon_cc0.zip','r')
                z.extractall()
                z.close()

            for fn in os.listdir():
                if fn.endswith('.zip') or fn.endswith('.tmp'):
                    os.remove(fn)

            print ("\n")

        def parse_entry(lex_entry):
            def parse_ud_fields(ud_string):
                p=dict()
                ud = ud_string.split('|')
                for m in ud:
                    f = m.split('=')
                    p[f[0]]=f[1]
                return p

            f = lex_entry.rstrip().split('\t')
            return f[0], f[1], f[2], parse_ud_fields(f[3]) if len(f)>3 else ''

        if not os.path.isfile(LEXICON_FILENAME):
            print ("Llwytho'r lecsicon i lawr..")
            download_lexicon()

        print ("Llwytho'r geirfa...") 
        with open(LEXICON_FILENAME, 'r', encoding='utf-8') as lexicon_file:
            for lex in lexicon_file:
                wordform, lemma, pos, ud = parse_entry(lex)
                yield (wordform, lemma, pos, ud)


    def contains(self, word):
        return self.lex_trie.search(word)

    def get_lemmas_with_info(self, wordform):
        return '\n'.join('{}\tLemma:{}\tPos:{}\tInfo:{}'.format(query, *l) for l in self.get_lemmas(query))

    def get_lemmas(self, wordform):
        return self.wordform_lookup[wordform]

    def get_wordforms(self, lemma):
        return self.lemma_lookup[lemma]

    def get_size(self):
        return len(self.wordform_lookup), len(self.lemma_lookup)

    def add(self, wordform, lemma, pos, features):
        self.lex_trie.insert(wordform)
        self.wordform_lookup[wordform].append((lemma, pos, features))
        self.lemma_lookup[lemma].append((wordform,pos,features))

    def generate_spelling(self, wordform):
        result=[]
        digraphs = ['ch','dd','ff','ng','ll','ph','rh','th']

        l = len(wordform)
        skip=False

        for c in range(l):

            if skip:
                skip=False
                continue

            ch = wordform[int(c)]
            nch=''
            if c<l-1:
                nch = wordform[c+1]

            for dg in digraphs:
                if ch==dg[0] and nch==dg[1]:
                    result.append(dg)
                    skip=True
                    break

            if skip==False:
                result.append(wordform[c])

        return result

    def initialise_spellings_cache(self):

        for k,v in self.lemma_lookup.items():
            spelling = self.generate_spelling(k)
            self.spellings[len(spelling)].append(".".join(spelling))


    def is_word_length(self, word, length):
        spelling = self.generate_spelling(word)
        if len(spelling)==length:
            return True
        else:
            return False


    def get_spellings(self, length):
        return self.spellings[int(length)]


if __name__ == "__main__":
    l=Lexicon() 
    print (l.get_size())
    print ("Lecsicon wedi'i llwytho")
