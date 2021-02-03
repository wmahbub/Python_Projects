from PyDictionary import PyDictionary

from english_words import english_words_set

from itertools import permutations


def word_match(a,b):
 
    if a[0: ]=='':
        return 0
    
    if b[0: ] == '':
        return 0
    
    else:
        if a[0] == b[0]:
            return 1 + word_match(a[1:], b[1:])
        
        else:
            return 0 + word_match(a[1:], b[1:])

def letter_match(a,b):
    
    counter= 0
    
    for i in range(len(a)):
        if a[i] in b:
            counter +=1
    
    return counter


def anagram(word):
    
    letters=[]
    new_words=[]
    
    for i in range(len(word)):
        letters.append(word[i])
    
    for i in range(len(letters)):
       a= list(permutations(letters,i))
       
       for j in range(len(a)):
           new_words.append(''.join(a))
      
    
    return new_words

print(anagram('word'))



    
    
    
            
