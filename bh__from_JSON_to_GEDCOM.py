#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 10:59:10 2019

@author: irinasm
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:29:04 2019

@author: irinasm
"""

import json

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
        
    def setID(self):
        self.id = data["ID"]

    def setFName(self):
        self.firstName = data["firstName"]
        
    def setLName(self):
        self.lastName = data["lastName"] 
        
    def setBdate(self):
        self.birthDate = data["birthDate"]
        
    def setBplace(self):
        self.birthPlace = data["birthPlace"]
        
    def setGender(self):
        self.gender = data["gender"]
        
    def setMomID(self):
        self.motherID = data["motherID"]  
        
    def setDadID(self):
        self.fatherID = data["fatherID"]   
    
    def setDeath(self):
        self.death = data["death"]
        
    def setDeathPlace(self):
        self.deathPlace = data["deathPlace"]  
        
    def setDeathDate(self):
        self.deathDate = data["deathDate"]
        
    def setSibling(self):
        for each in data["sibling"]:
            self.sibling.append(each["siblingID"])
            
    def set_data(self):
        self.setID()
        self.setFName()
        self.setLName()
        self.setBdate()
        self.setBplace()
        self.setGender()
        self.setMomID()
        self.setDadID()
        self.setDeath()
        self.setDeathPlace()
        self.setDeathDate()
        self.setSibling()
        return 1   ### chto vozvraschat'?        
    
    def __print__(self):   ### will be deleted
        print ("The Person is %s %s %s %s" % (self.id, self.firstName, self.lastName, self.gender))
        print ("The Person's bday at %s in %s" % (self.birthDate, self.birthPlace))
        print ("The Person's MomID is %s and DadID is %s" % (self.motherID, self.fatherID))
        print ("The Person's death is %s on %s in %s" % (self.death, self.deathDate, self.deathPlace))
        print ("The sibling's ID are %s" % (self.sibling))  #list of siblings (type: list of int)
        print ("The sibling's ID are %s" % (", ".join(self.sibling)))  #string of siblings        
        

       
### from JSON file to Person object
name_json_file = "user.json"     
with open(name_json_file) as json_file:  
    data = json.load(json_file)

my_person = Person(0)   #create default object of Person class
my_person.__print__()    ### will be deleted
print ("-------------")  ### will be deleted

my_person.set_data()    #set User's data to our Person object
my_person.__print__()   ### will be deleted


##############            ### will be deleted
###   JSON file   ###
#{
#    "ID": "1",
#    "firstName": "John",
#    "lastName": "Smith",
#    "birthDate": "10/22/1955",
#    "birthPlace": "New York",
#    "gender": "male",
#    "motherID": "10",
#    "fatherID": "100",
#    "sibling": [
#        {
#            "siblingID": "1000"
#        },
#        {
#            "siblingID": "2000"
#        },
#       {
#            "siblingID": "3000"
#        }
#    ],
#    "death": "true",
#    "deathPlace": "Boston",
#    "deathDate": "01/17/2015" 
#}        


print ("------------------------------------")   ### will be deleted
print ("------------------------------------")   ### will be deleted


####  from Person object to GEDCOM file   ###
# Path to my ".ged" file
name_gedcom_file = "user.ged"
with open(name_gedcom_file, "w") as writing_gedcom_file: 
    writing_gedcom_file.write("User gedcom file:\n")  ### will be deleted
    
    lines_header = ["HEADER will be here\n"]   ### will be deleted
    
    #create the person data
    lines_person= ["0 @I" + my_person.id +"@ INDI\n",
             "1 NAME " + my_person.firstName + " /" + my_person.lastName + "/\n",
             "1 SEX " + my_person.gender + "\n",
             "1 BIRT\n" + "2 DATE " + my_person.birthDate + "\n",
             "2 PLAC " + my_person.birthPlace + "\n",
             "1 DEAT\n" + "2 DATE " + my_person.deathDate + "\n",
             "2 PLAC " + my_person.deathPlace + "\n",
             #"1 FAMC @F" + my_person.parentFamilyID +"@\n",  #### add parent's family ID
             "1 FAMC @F" + "111" + "@\n"  #vremenno dlya illyustracii
             ]
    
    #create the family of parents
    lines_parent = [
            #"0 FAMC @F" + my_person.parentFamilyID +"@ FAM\n",   #### add parent's family ID
              "0 FAMC @F" + "111" +"@\n",  #vremenno dlya illyustracii
              "1 HUSB @I" + my_person.fatherID +"@\n",
              "1 WIFE @I" + my_person.motherID +"@\n",
              "1 CHIL @I" + my_person.id +"@\n"
              ]
 
    #create a list of siblings (type: list of string)
    lines_sibling = []
    for each in my_person.sibling:
        lines_sibling.append("1 CHIL @I" + each +"@\n")
    
    writing_gedcom_file.writelines(lines_header + lines_person + lines_parent + lines_sibling)
 
### will be deleted
# Print GEDCOM file    
with open(name_gedcom_file, "r") as reading_gedcom_file:     
        for line in reading_gedcom_file.readlines():
            print (line)
