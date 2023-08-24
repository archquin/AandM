#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 13:53:16 2022

@author: archquin
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 00:40:01 2022

@author: archquin
"""


import visualisedictionary as vd
from IPython.display import Image



#ship = input()# 
ship = int(4)


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
for i in range(0,ship):
    k = len(Subs[i-1])
    elp = []
    hel = []
    for j in range(0,k,3):
        elp.append(Subs[i-1][j])        
        hel.append(Subs[i-1][j+1])
    Subone.append(elp)
    Subway.append(hel)
    Subwas.append(hel)
Subone.pop(0)
Subway.pop(0)   
Subwas.pop(0)



Subtwo = []
for i in range(len(Subone)):
    hell = []
    for j in range(len(Subone[i])):
        hell.append(clfc[i])
    Subtwo.append(hell)

for i in range(1,ship):
    mylist = set(Subway[i-1])
    Subway[i-1]=list(mylist)




            
Assembly={}
 

for i in range (1,ship):
    Subj = {}
    for j in Subway[i-1]: 
        Dic = {}
        k = len(Subwas[i-1])
        for kij in range(0,k):
            if j == Subwas[i-1][kij]:
                if Subone[i-1][kij] not in clfc:
                    Dic.update({Subone[i-1][kij]:kij})
                    Subj.update({j:Dic})
                elif Subone[i-1][kij] in clfc :
                    Dic.update({Subone[i-1][kij]:Assembly[Subone[i-1][kij]]})
                    Subj.update({j:Dic})
            Assembly.update({Subtwo[i-1][kij]:Subj})
         
            
            
            
            
G = vd.KeysGraph(Assembly)

G.draw('./test.png')
Image('./test.png')
            
            
'''
The following function was found at 

#https://stackoverflow.com/questions/69849956/python-how-to-process-complex-nested-dictionaries-efficiently 


### Dictionary shreder
def merge(a, b, path=None, update=True):
    if path is None: path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass 
            elif isinstance(a[key], list) and isinstance(b[key], list):
                for idx, val in enumerate(b[key]):
                    a[key][idx] = merge(a[key][idx], b[key][idx], path + [str(key), str(idx)], update=update)
            elif update:
                a[key] = b[key]
            else:
                raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a

#############################################################################################################################################


def find_keys(dct):
    result = []
    for k, v in dct.items():
        if isinstance(v, dict):
            result += [f"{k} --> {x}" for x in find_keys(v)]
        else:
            result.append(k)
    return result
       
kiks = find_keys(Assembly)
nky = []
ykn = []
R ={}
ny = []
for i in kiks:
    j = i.split(' --> ')
    k = i.split(' --> ')
    ykn.append(k)
    j.reverse()
    nky.append(j)
    R.update({j[0]:0})
ny= list(R.keys())

    
#https://stackoverflow.com/questions/444296/how-to-efficiently-build-a-tree-from-a-flat-structure

def build_tree(tree_list):
    if tree_list:
        return {tree_list[0]: build_tree(tree_list[1:])}
    return {0}

kyn = []
Rev = {}
for i in range(len(ykn)):
    kyn.append(build_tree(ykn[i]))

    
ll = []
for j in ny :
    cc=[]
    for i in range(len(nky)):
        if nky[i][0] == j:
            cc.append(i)
    ll.append(cc)
 


def supermerge(key,mdicts):
    Unsemble = {}
    un = {}
    for i in range(len(mdicts)):
        un = merge(un,mdicts[i])
        Unsemble.update({key:un})
    return Unsemble

Nn = []
for i in range(len(ll)):
    kk = []
    for j in range(len(ll[i])):
        kk.append(kyn[ll[i][j]])
    Nn.append(kk)
    
for i in range(len(ny)):
    Rev.update(supermerge(ny[i],Nn[i]))
    
G = vd.KeysGraph(Rev)

G.draw('./tsest.png')
Image('./tsest.png')

             
                       
            
            
    
'''
