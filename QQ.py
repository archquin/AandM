
    


import visualisedictionary as vd
from IPython.display import Image



ship = int(3)

    
ship = ship + 1
clfc = []

Subs =[]


for i in range(1,ship):
    txt = 'Instr'+str(i)
    with open(txt) as f:
        lines = f.readlines()
        x = 0
        

        subb = []
        for line in lines:
            x += 1
            if x == 1:
                clfc.append(line.strip())
            if x > 2 :
                if line != '':
                    subb.append(line.strip())
                    f.close()
        Subs.append(subb)

               
            
            



Subone = []
Subway =[]
Subwas =[]

Subwhat = []
Subwhy = []


for i in range(0,ship):
    k = len(Subs[i-1])
    elp = []
    hel = []
    phe = []
    for j in range(0,k,4):
        elp.append(Subs[i-1][j])        
        hel.append(Subs[i-1][j+1])
        phe.append(Subs[i-1][j+2])
    Subone.append(elp)
    Subway.append(hel)
    Subwas.append(hel)
    Subwhat.append(phe)
    Subwhy.append(phe)

    
Subone.pop(0)
Subway.pop(0)   
Subwas.pop(0)
Subwhat.pop(0)
Subwhy.pop(0)




Subtwo = []
for i in range(len(Subone)):
    hell = []
    for j in range(len(Subone[i])):
        hell.append(clfc[i])
    Subtwo.append(hell)

for i in range(1,ship):
    mylist = set(Subway[i-1])
    Subway[i-1]=list(mylist)

for i in range(1,ship):
    mylist = set(Subwhat[i-1])
    Subwhat[i-1]=list(mylist)



'''
Subthree = []
for i in range(len(Subone)):
    hell = []
    for j in range(len(Subone[i])):
        hell.append(clfc[i])
    Subthree.append(hell)
'''




            
Assembly={}

for i in range (1,ship):
    Subj = {}
    for v in Subwhat[i-1]:
        Suju = {}
        for j in Subway[i-1]: 
            Dic = {}
            k = len(Subwas[i-1])
            kk = len(Subwhy[i-1])
            for kij in range(0,k):
                for key in range(0,kk):
                    if j == Subwas[i-1][kij] and v == Subwhy[i-1][key] and key == kij:
                        if Subone[i-1][kij] not in clfc:
                            Dic.update({Subone[i-1][kij]:kij})
                            Suju.update({j:Dic})
                            Subj.update({v:Suju})
                        elif Subone[i-1][kij] in clfc :
                            Dic.update({Subone[i-1][kij]:Assembly[Subone[i-1][kij]]})
                            Suju.update({j:Dic})
                            Subj.update({v:Suju})

                    Assembly.update({Subtwo[i-1][kij]:Subj})
             
                
            
            
            
G = vd.KeysGraph(Assembly)

G.draw('./test.png')
Image('./test.png')
