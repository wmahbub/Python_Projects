#from PyDictionary import PyDictionary

def second(lst): 
    return lst[1]


def word_analyzer(filename, *company):
    
    firm = str(*company).lower()

    file = open(filename, 'r', encoding='utf_8')

    lines = file.read()
    lines= lines.strip()
    
    words = lines.split(' ')
    
    lst= []
    d= {}
    
    exclude= ['from', 'with', 'that', "it's", 'will', 'there','them', 'they', 'these', 'while', 'about', 'your', 
              'please', 'through', 'enable', 'enables', 'ways', 'have', 'this','ability', 'multiple', 'skills', 'some', 'many',
              'name', 'more', 'than', 'move', 'work', 'thrive', 'please', 'using', 'first', 'last', 'million', 'billion',
              'world', 'name', 'please', 'around', 'us', 'it', 'their', 'what','because','strong', 'just','ensure', 'where', 
              'when', 'want', 'join', 'boston', '201',"they're", "he's", "we're" , "should've", 'should', 'could', "could've", 
              'would', "would've", 'into', 'most', "they've", "it's", firm]
    
    for w in words:
        if len(w.strip())>3:
            if w[-1] in '!@#$%^&*()-_=+[]{}:;,.<>?/|\•1234567890" ':
                lst.append(w[ :-1].lower())
            
            elif w[-3: ] == 'ing':
                lst.append(w[ : -3].lower())
            
            elif w[-2: ] == "'s" or w[-2: ] == "’s":
                lst.append(w[ :-2].lower())
            
            elif w[-2: ] == "es" or w[-2: ] == 'ts' or  w[-2: ] == 'rs':
                lst.append(w[ :-1].lower())
                
            #elif w[-2: ] == 'ed':
                #lst.append(w[ :-1].lower())
            
            elif w[1] == '•':
                lst.append(w[2: ].strip().lower())
            
            else:
                lst.append(w.lower())
        
    for w in lst:
        if w not in exclude:
            if w not in d:
                d[w]= 1
            
            else:
                d[w]+=1
    
    s = [ [ k , d[k] ] for k in d if d[k]>1]
    
    s.sort(key=second, reverse= True)
    
    for i in range(20): # this number changes with job descriptions 
        print(s[i][0],':', s[i][1])


def resume_analyzer(filename, *company):
    
    print('-'*25)
    print('Resume Top 15 Words')
    print('-'*25)

    word_analyzer(filename, *company)
    
    print('-'*25)


def cover_letter_analyzer(filename, *company):
    
    print('-'*25)
    print('Cover Letter Top 15 Words')
    print('-'*25)

    word_analyzer(filename, *company)
    
    print('-'*25)
    

def job_desc_analyzer(filename, *company):

    print('-'*30)
    print('Job Description Top 15 Words')
    print('-'*30)

    word_analyzer(filename, *company)

    print('-'*30)




text =job_desc_analyzer(r'C:\Users\wajda\Desktop\Visual Studio Code Projects\Zynga_RPM.txt', 'zynga')

#cover_letter_analyzer(r'C:\Users\xxxxx\Documents\GitHub\Python_Projects\Python_Projects\Text\cover_letter_springboard.txt', 'springboard')

#resume_analyzer(r'C:\Users\xxxxx\Documents\GitHub\Python_Projects\Python_Projects\Text\resume_BU.txt')

#f= open('paypal_vscode.txt', 'w')
#f.writelines(str(text))
#   f.close

