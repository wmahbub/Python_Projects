import random

def grid_rand(a):
    
    list=[]
    
    for i in range(1,a):
        list.append(i)

    for j in range(a+1,10):
        list.append(j)
    
    return list


def grid(row, col):
    
    seq = []
    
    for i in range(row):
        for j in range(col):
            
            a= random.randint(0,1)
            b= random.randint(1,9)
            
            if a==0:
                seq.append(0)
            
            else:
                if b not in seq:
                    seq.append(b)
                
                else:
                    c= grid_rand(b)
                    use= []
                    
                    for m in c:
                        if m not in seq:
                            use.append(m)
                    
                    seq.append( random.choice(use) )
    
    return seq                        
            

def boxes(a):
    for i in range(a):
        print(grid(3,3))


def triangle(a):
    b= list(range(a-1, -1, -1))
    
    for i in range(a):
        for j in range(i+1):
            print('*', end='  ')
        print('\r')

triangle(4)

#print(list(range(4,0,-1)))
