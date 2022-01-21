import os
import lexicon

if __name__ == "__main__":

    try:
        l = lexicon.Lexicon()

        print ("Rhowch eiriau lemma i fewn i weld ei bob ffurf a rhediad..")
        while True:
            query = input('> ')
            print('\n'.join('{}\t{}\t{}\tInfo:{}'.format(query, p,w,u) for w,p,u in l.get_wordforms(query))) 

    except KeyboardInterrupt:
        pass

