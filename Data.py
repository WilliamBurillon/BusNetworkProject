# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 11:27:35 2019

@author: burillow
"""

class Data:
    
    def __init__(self, file):
        
        self.file = open(file,"r",encoding = "utf_8")
    
    
    
    def getBusStation(self):
        
        f=self.file.readlines()[0].split(" N ")
        f[len(f)-1]=f[len(f)-1][0:len(f[len(f)-1])-2]
        f0=f[0].split(" + ")
        f[0]=f0[0]
        f.append(f0[1])
        return f
    
    def closing(self):
        self.file.close()
        
d=Data("1_Poisy-ParcDesGlaisins.txt")

print(d.getBusStation())
d.closing()

        
        

