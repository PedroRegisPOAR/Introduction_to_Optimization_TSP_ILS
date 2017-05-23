import random
import time

def ler(name):
    import string
    file = open(name + '.txt', 'r')
    n = int(file.readline())
    d = []
    for line in file:
        d.append(list(map(float,line.split())))
    return d

d10 = ler('10c')        
d20 = ler('20c')
d40 = ler('40c')
d80 = ler('80c')
d100 = ler('100c')   

    
def randomRoute(n):
    route = [i for i in range(n)]
    random.shuffle(route)
    return route

def pertubateRoute(r, n, p):
    for k in range(p):
        i = random.randint(1,n-1)
        j = random.randint(1,n-1)
        r[i], r[j] = r[j], r[i]
    return r

def custo(r, d, n):
    return sum([d[r[i]][r[i+1]] for i in range(n-1)]) + d[r[n-1]][r[0]]

def movimento2opt(r, i, k):
    return r[:i] + r[i:k+1][::-1] + r[k+1:]

def busca2opt(d, r, n):
    melhora = 1
    cb = custo(r, d, n)
    rb = r
    
    while melhora == 1:
        melhora = 0
        i = 1
        while i < n-1 and melhora == 0:
            k = i + 1
            while k < n and melhora == 0:
                r = movimento2opt(rb, i, k)
                caux = custo(r, d, n)
                if cb > caux:
                    melhora = 1
                    rb = r
                    cb = caux
                k += 1
            i += 1
    return rb, cb

def g(d, n, p):
    r, cont, contmax = randomRoute(n), 0, 0
    rb, cb = busca2opt(d, r, n)
    
    t1 = time.clock()
    while cont < 5*n and contmax < n*n//10:        
        r = pertubateRoute(list(rb), n, p)        
        raux, caux = busca2opt(d, r, n)                
        if cb > caux:
            rb, cb, cont = raux, caux, 0
        else:
            cont += 1
        contmax += 1
    t2 = time.clock()
    return cb, rb, t2 - t1, contmax



n = 20
p = int(0.1*n)
r = randomRoute(n)
d = d20


for i in range(10):
    o = g(d, n, p)
    print('Custo: ', round(o[0],2), '\t Tempo: ', round(o[2], 5), '\t Iterações: ', o[3])
    


"""
n = 10
p = int(n/100)
r = randomRoute(n)
d = d10

n = 20
p = int(n/100)
r = randomRoute(n)
d = d20

n = 40
p = int(n/100)
r = randomRoute(n)
d = d40

n = 80
p = int(n/100)
r = randomRoute(n)
d = d80

n = 100
p = int(n/100)
r = randomRoute(n)
d = d100

# r = [chr(65 + i ) for i in range(8)]
#r = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#n = 8
#busca2opt(r, n)        
"""
