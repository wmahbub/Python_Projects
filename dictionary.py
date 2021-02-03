from PyDictionary import PyDictionary

from english_words import english_words_set


def word_match(a, b):

    if a[0:] == '':
        return 0

    if b[0:] == '':
        return 0

    else:
        if a[0] == b[0]:
            return 1 + word_match(a[1:], b[1:])

        else:
            return 0 + word_match(a[1:], b[1:])


def letter_match(a, b):

    counter = 0

    for i in range(len(a)):
        if a[i] in b:
            counter += 1

    return counter


word1= "fixed"
word2= "flying"

lower= len(word1)-3
upper= len(word1)

d=[]

for w in english_words_set:
    if len(w)>= lower and len(w)<= upper:
        d.append([word_match(word1,w) + letter_match(word1,w),w])
    
d.sort(reverse=True)
print(d[0:11])
    
    

