# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 18:17:12 2023

@author: Serafin
"""


class ProductionRule:
    left_part: str # the left part of the production
    right_part: [str]
    
    def __init__(self, left, right):
        object.__setattr__(self, "left_part", left)
        object.__setattr__(self, "right_part", right)
    
    def getLeftPart(self):
        return self.left_part
    
    def getRightPart(self):
        return self.right_part
    
    def __str__(self):
        print("Left part: ")
        print(self.left_part)
        
        print("Right part: ")
        print(self.right_part)
        
        return ""
    
    