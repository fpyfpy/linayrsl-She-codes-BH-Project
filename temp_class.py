#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:25:07 2019

@author: irinasm
"""

class Person(object):
    def __init__(self, id, firstName = "unknown",
                           lastName = "unknown",
                           birthDate = 0000,
                           birthPlace = "unknown",
                           gender = "unknown",
                           motherID = "unknown",
                           fatherID = "unknown",
                           death = "unknown",
                           deathPlace = "unknown",
                           deathDate = "unknown",
                           sibling = []):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        self.birthPlace = birthPlace
        self.gender = gender
        
        self.motherID = motherID
        self.fatherID = fatherID
    
        self.death = death
        self.deathPlace = deathPlace
        self.deathDate = deathDate
        
        self.sibling = sibling

vasya = Person(3)