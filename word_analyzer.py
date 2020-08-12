a = r'C:\Users\xxxxx\Desktop\Visual Studio Code Projects\paypal.txt'


def second(lst):
    return lst[1]


def word_analyzer(filename, company):
    
    firm = company.lower()

    file = open(filename, 'r', encoding='utf_8')

    lines = file.read()
    lines= lines.strip()
    
    words = lines.split(' ')
    
    lst= []
    d= {}
    
    exclude= ['from', 'with', 'that', "it's", 'will', 'them', 'they', 'these', 'while', 'about', 'your', 
              'please', 'through', 'enable', 'enables', 'ways', 'have', 'ability', 'multiple', 'skills', 'some', 'many',
              'name', 'more', 'than', 'move', 'work', 'thrive', 'please', 'using', 'first', 'last', 'million', 'billion',
              'world', 'name', 'please', 'around', 'us', 'strong', firm]
    
    for w in words:
        if len(w.strip())>3: #and w not in exclude:
            if w[-1] in '!@#$%^&*()-_=+[]{}:;,.<>?/|\•1234567890" ':
                lst.append(w[ :-1].lower())
            
            elif w[-3: ] == 'ing':
                lst.append(w[ : -3].lower())
            
            elif w[-2:] == "'s" or w[-2:] == "’s":
                lst.append(w[ :-2].lower())
            
            elif w[-2:] == "es" or w[-2:] == 'ts' or  w[-2:] == 'rs':
                lst.append(w[:-1].lower())
            
            elif w[1] == '•':
                lst.append(w[2:].strip().lower())
            
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
    
    #return s
    
    for a in s:
        print(a[0],':', a[1])

word_analyzer(a, 'paypal')


