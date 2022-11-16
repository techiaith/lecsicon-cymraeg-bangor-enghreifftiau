import re, sys, unittest

# POSSIBLE TYPOS IN THE LECSICON
# annrhigiadwy => anhrigiadwy
# cyfarhos => cyfaros?
# LIanrhystud => Llanrhystud
# lianrhystud => Llanrhystud
# sbringar => sbring-gar

DONT_SPLIT_RH = 'Caerhos Cilrhedyn Cwmyrhiwdre Nantyrhynnau Porthyrhyd Trerhedyn Trerhingyll Troedyrhiw arhythmia arhythmig coleorhisa ewrhythmeg gonorrhoea isorhythmig mycorhisa pyorhea yrhawg'.split()

# TODO: may need to include some of the following:
# Angefin Bodringallt Brengain Ingli Langro Llandingad Llanddingad Pinged Tangwen Tangwyn *ffaryngeal
SPLIT_NG = 'Abergwyngregyn Angliad Anglican Anglicanaidd Angola Bangladesh Bangor Bengal Blaengarw Blaengwrach Blaengwynfi Brongest Bronglais Bryngarn Bryngwran Bryngwyn Carngowil Carnguwch Carngwcw Cefngorwydd Cilmaengwyn Congo Cryngae Felinganol Ffynnongroyw Garthbrengi Glangors Grongaer Hengastell Hengoed Hengwm Hengwrt Hwngaraidd Hwngareg Hwngari Lingoed Llanengan Llanfairpwllgwyngyll Llwyngroes Llwyngwair Llwyngwern Maengwyn Melingriffith Mongolia Myngul Pengelli Penglais Pengorffwysfa Pengrynwr Pengwern Penybenglog Singrug Tafarngelyn Tanganyika Tongwynlais Tringarth Ynysymaengwyn amcangyfrifyn arlwyngig arweingi bangaw bangorwaith bechingalw bingo brongoch browngoch bryngaer cangarŵ conga congren cringoch cwango cwangoaidd dychangerdd engram genglo glingam gwerngoedwig gwyngoch gylfingroes hunglwyf hwiangerdd ingot jingo jingoistiaeth jwngl jyngl lingri llieingant llengig llinengrafiad llinganol llinglwm llongyfarch llongyfarchiad llwyngwril llyfngrwn manganîs manglo mango mangrof melyngoch mingam mingamu mwnglawdd mwngrel plaengan prynhawngwaith rhangor rhangymeriad rhieingerdd safnglo safngloi sbangl swyngan torlengig torllengig tudalengipio yngymaint ysgafngalon'.split()

def split_word(word, lemma=None):
    if lemma is None:
        lemma = word
    # DO NOT split rh (nor ng) if the lemma is one of the DONT_SPLIT_RH lemmas listed above.
    if lemma in DONT_SPLIT_RH:
        return re.findall(r'ch|dd|ff|ng|ll|ph|rh|th|.', word, re.IGNORECASE)
    # Otherwise, DO split rh, unless it's at the start of a word, or after d/l/m/n/t
    #
    # DO split ng if the lemma is one of the SPLIT_NG lemmas listed above.
    # Otherwise, DO NOT split ng, unless the lemma starts with one of these:
    #
    #   angio bwngler byngalo dyngar dyngas gwangalon mening tang (except if it starts with tangiad)
    #
    # or one of these then a 'g':
    #
    #   Llan blaen bon bron brown bryn calon cefn gwahan gwyn hunan llun mein mewn mwyn pan pen sein swyn teyrn un union
    #
    # or ends with 'n' then one of these:
    #
    #   groen gar garwch gyfrif
    #
    # But even when splitting ng, don't split if it's at a word boundary
    if lemma in SPLIT_NG or re.search(r'\b(angio|bwngler|byngalo|dyngar|dyngas|gwangalon|mening|tang(?!iad)|(Llan|blaen|bon|bron|brown|bryn|calon|cefn|gwahan|gwyn|hunan|llun|mein|mewn|mwyn|pan|pen|sein|swyn|teyrn|un|union)g)|n(groen|gar|garwch|gyfrif)\b', lemma, re.IGNORECASE):
        return re.findall(r'ch|dd|ff|\bng|ng\b|ll|ph|\brh|(?<=[dlmnt])rh|th|.', word, re.IGNORECASE)
    return re.findall(r'ch|dd|ff|ng|ll|ph|\brh|(?<=[dlmnt])rh|th|.', word, re.IGNORECASE)

if __name__ == '__main__':
    while True:
        word = sys.stdin.readline().strip()
        if word == '':
            break
        print (word + '\t' + ' '.join(split_word(word)))
