import time

import lexicon


if __name__ == "__main__":
    l=lexicon.Lexicon()
 
    print ("Rhowch eiriau i wirio eu sillafu")
    try:
        while True:
            candidate = input('> ')
            s = l.contains(candidate)
            print (s)
            if s:
                print (l.generate_spelling(candidate))
        
    except KeyboardInterrupt:
        pass 

