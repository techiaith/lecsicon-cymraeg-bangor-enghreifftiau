import os
import lexicon

if __name__ == "__main__":
    l=lexicon.Lexicon()
    
    print ("Rhowch eiriau i'w lemmateiddio")
    try:
        while True:
            query = input('> ')
            lemmas = l.get_lemmas(query)
            for lemma in lemmas:
                print(lemma)
            print()

    except KeyboardInterrupt:
        pass

