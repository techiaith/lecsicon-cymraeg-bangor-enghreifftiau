import time

import lexicon


if __name__ == "__main__":
    l=lexicon.Lexicon()
 
    print ("Rhowch eiriau i wirio eu sillafu")
    try:
        while True:
            candidate = input('> ')
            lemma_records = l.get_lemmas(candidate)

            if len(lemma_records) == 0:
                s = False
            else:
                s = True
            print (s)
            if s:
                first_record = lemma_records[0]
                lemma = first_record[0]
                print (l.generate_spelling(candidate, lemma))
        
    except KeyboardInterrupt:
        pass 

