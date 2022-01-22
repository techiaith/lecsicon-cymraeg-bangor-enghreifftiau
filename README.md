# Enghreifftiau defnyddio Lecsicon Cymraeg Bangor 

Mae'r gronfa cod yma yn arddangos beth ellir ei ddatblygu gyda [Lescicon Cymraeg Prifysgol Bangor](https://github.com/techiaith/lecsicon-cymraeg-bangor).

Mae hefyd o ddiddordeb i unrhyw un sydd eisio dysgu codio (Python) ac/neu ddysgu Cymraeg neu i ddatblygu unrhyw beth newydd ar gyfer y Gymraeg. 

Mae pedwar prif sgript sgript enghreifftiol:

 - gwirydd sillafu
 - morffoleg
 - lemateiddiwr
 - gêm Wordle Cymraeg



### Gwirydd Sillafu

```
lecsicon-cymraeg-bangor-enghreifftiau> python3 .\spellchecker.py
Llwytho'r lecsicon i lawr..
100% [..........................................................................] 4415891 / 4415891

Llwytho'r geirfa...
Rhowch eiriau i wirio sillafu
> llwyddo
True
['ll', 'w', 'y', 'dd', 'o']
> llywddo
False
>
```

### Morffoleg (Gwirio Gair)

```
lecsicon-cymraeg-bangor-enghreifftiau> python3 .\morphology.py
Llwytho'r geirfa...
Rhowch eiriau lemma i fewn i weld ei bob ffurf a rhediad..
> coch
coch    ADJ     coch    Info:{'Degree': 'Pos'}
coch    ADJ     cochach Info:{'Degree': 'Cmp'}
coch    ADJ     cochaf  Info:{'Degree': 'Sup'}
coch    ADJ     coched  Info:{'Degree': 'Equ'}
coch    ADJ     choch   Info:{'Degree': 'Pos', 'Mutation': 'AM'}
coch    ADJ     chochach        Info:{'Degree': 'Cmp', 'Mutation': 'AM'}
coch    ADJ     chochaf Info:{'Degree': 'Sup', 'Mutation': 'AM'}
coch    ADJ     choched Info:{'Degree': 'Equ', 'Mutation': 'AM'}
coch    ADJ     goch    Info:{'Degree': 'Pos', 'Mutation': 'SM'}
coch    ADJ     gochach Info:{'Degree': 'Cmp', 'Mutation': 'SM'}
coch    ADJ     gochaf  Info:{'Degree': 'Sup', 'Mutation': 'SM'}
coch    ADJ     goched  Info:{'Degree': 'Equ', 'Mutation': 'SM'}
coch    ADJ     nghoch  Info:{'Degree': 'Pos', 'Mutation': 'NM'}
coch    ADJ     nghochach       Info:{'Degree': 'Cmp', 'Mutation': 'NM'}
```


### Lemmateiddiwr

```
lecsicon-cymraeg-bangor-enghreifftiau> python3 .\lemmatizer.py
Llwytho'r geirfa...
Rhowch eiriau i'w lemmateiddio
> clo
('clo', 'NOUN', {'Gender': 'Masc', 'Number': 'Sing'})
('cloi', 'VERB', {'Mood': 'Imp', 'Number': 'Sing', 'Person': '2'})
('cloi', 'VERB', {'Mood': 'Ind', 'Number': 'Sing', 'Person': '3', 'Tense': 'Fut'})
('cloi', 'VERB', {'Mood': 'Ind', 'Number': 'Sing', 'Person': '3', 'Tense': 'Pres'})
```

### Gêm Wordle Cymraeg

Bydd angen gosod `termcolor` yn gyntaf cyn rhedeg y sgript gêm Wordle. 

Mae'r gêm yn defnyddio rhestr o'r geiriau mwyaf aml y Gymraeg er mwyn cynnig eiriau 5 lythyren haws. Er gellir addasu'r sgript i'w wneud yn anoddach neu'n haws, yn ogystal a newid y nifer o lythrennau. Defnyddir deugraffau yr wyddor Cymraeg (h.y. 'ch', 'll') 
 
![delwedd](https://user-images.githubusercontent.com/8668769/150603899-17e3e038-aaf3-440d-bba6-9a15b5236da4.png)

