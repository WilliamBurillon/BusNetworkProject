# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:45:00 2019

@author: burillow
"""

###========= Definition of the data structure ================###

##=== Class Node ========##

class Node :
    
    
    def __init__(self,name,l_line,l_timetable,predecessors=[],sucessors=[]):
        self.name=name
        self.l_line=l_line
        self.l_timetable=l_timetable
        self.predecessors=predecessors
        self.sucessors=sucessors
        
    

    def __str__(self):
        return self.name
    
    
##====== class Arcs =========##
        
class Arcs : 
    
    def __init__(self,start,finish):
        self.start = start
        self.finish = finish
        #self.duration=
        
class Network :
    
    def __init__(self,l_node,l_Arcs):
        self.l_node = l_node
        self.l_Arcs = l_Arcs
        









fichier = open("1_Poisy-ParcDesGlaisins.txt", "r",encoding = "utf_8")
res=[]
#for j in range(0,len(fichier.readlines()[0])):
#        if fichier.readlines()[i+1] =='\n' and ' N ' in fichier.readlines()[i]:
#            line=fichier.readlines()[i]
#            print(line)
#    
print(type(fichier))
f=fichier.readlines()[0].split(" N ")

print(f)

f[len(f)-1]=f[len(f)-1][0:len(f[len(f)-1])-2]
print(f)

f0=f[0].split(" + ")
f[0]=f0[0]
f.append(f0[1])
print(f)

fichier.close()
        

