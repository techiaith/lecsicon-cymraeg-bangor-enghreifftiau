import time
import secrets
import lexicon
import frequencies

from termcolor import colored, cprint

def evaluate_guess(lexicon, guess, word):
    result=[]
    
    guess_spelling = lexicon.generate_spelling(guess)
    word_spelling = lexicon.generate_spelling(word)

    success=True
    for ix in range(len(guess_spelling)):

        ch_guess=guess_spelling[int(ix)]
        ch_word=word_spelling[int(ix)]

        if ch_guess==ch_word:
            result.append((ch_guess, "white", "on_green"))
        elif ch_guess.upper()==ch_word:
            result.append((ch_guess, "white", "on_green"))
        elif ch_guess in word:
            result.append((ch_guess, "white", "on_yellow"))
            success=False
        else:
            result.append((ch_guess, "", ""))
            success=False

    return success, result
        
   
def print_result(attempt, result):
    print (str(attempt) + "/6 ", end='')

    for letter, textcolor, backgroundcolor in result:
        if textcolor=='' and backgroundcolor=='':
            print(" " + letter + " ", end='')
        else:
            cprint(" " + letter + " ", textcolor, backgroundcolor, end='')

        # gap rhwng lythrenau..
        print(" ", end='')

    print()

def choose_random_word(lexicon, frequencies):
    candidates = l.get_spellings(5)
    while True:
        word = secrets.choice(candidates).replace(".","")
        if "-" in word:
            continue

        freq = frequencies.get_frequency(word)
        if freq>500:
            return word



if __name__ == "__main__":
    l=lexicon.Lexicon()
    f=frequencies.Frequencies()
 
    print ("Byddwch barod i chwarae Wordle Cymraeg....")
    try:
        word = choose_random_word(l,f)
        print (word)

        success=False
        for attempt in range(1,7):
            if success:
                print ("Llongyfarchiadau mawr!! %s/%s : %s" % (attempt -1, 6, word))
                break

            while True:
                guess = input('%s > ' % attempt)
                if l.is_word_length(guess, 5):
                    success, result = evaluate_guess(l, guess, word)
                    print_result (attempt, result)
                    break
                else:
                    print("Rhaid i'r gair bodoli yn y lecsicon neu bod yn 5 lythyren")

        
    except KeyboardInterrupt:
        pass 

