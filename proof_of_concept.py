#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:29:04 2019

@author: irinasm
"""

import json

#from gedcom.element.individual import IndividualElement
#from gedcom.parser import Parser


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
    
    def __print__(self):
        print ("The Person is %s %s %s %s" % (self.id, self.firstName, self.lastName, self.gender))
        print ("The Person's bday at %s in %s" % (self.birthDate, self.birthPlace))
        print ("The Person's MomID is %s and DadID is %s" % (self.motherID, self.fatherID))
        print ("The Person's death is %s on %s in %s" % (self.death, self.deathDate, self.deathPlace))
        #print ("The sibling's ID are %s" % (', '.join(self.sibling)))
        print ("The sibling's ID are %s" % (self.sibling))
       # print ("The sibling's ID are {}".format(self.sibling))
        
      

    def create_person(self, id):  # nuzhna li eta funkciya voobsche? ili prosto sozdavat' ob'ekt klassa Person?
        return Person(id)
        
        
### from JSON file
user_json_file =  "user.json"       
with open(user_json_file) as json_file:  
    data = json.load(json_file)
    
#    myid = data["ID"]
#    print ("ID:" + myid)
#    print ("Name:" + data["firstName"])
#    print ("Last name:" + data["lastName"])
#    print ("Bdate:" + data["birthDate"])
#    print ("BPlace:" + data["birthPlace"])
#    print ("Gender:" + data["gender"])

        
my_person = Person(0)
my_person.__print__()
print ("--???????????--")

my_person2 = my_person.create_person(555)
my_person2.__print__()
print ("-------------")

# Sdelat' odnu obschuyu funkciyu, kotoraya zapolnyaet vse polya ob'ekta
#my_person.setID()
#my_person.setFName()
#my_person.setLName()
#my_person.setBdate()
#my_person.setBplace()
#my_person.setGender()
#my_person.setMomID()
#my_person.setDadID()
#my_person.setDeath()
#my_person.setDeathPlace()
#my_person.setDeathDate()
#my_person.setSibling()

my_person.set_data()
my_person.__print__()


##############
###   JSon file   ###
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


###   GEDCOM (family) file example   ###

#1 FAMC @F1@
#1 CHAN 
#2 DATE 11 FEB 2006
#0 @F1@ FAM
#1 HUSB @I1@
#1 WIFE @I2@
#1 MARR 
#1 CHIL @I3@

print ("------------------------------------")
print ("------------------------------------")


#### from Person object to GEDCOM file   ###

# Path to my ".ged" file
file_path = "user.ged"

#lines_sibling = "aaa"
#b = "bb"
#print (my_person.sibling)
#for each in my_person.sibling:
#lines_sibling.join(b)
#print ("lines_sibling :", lines_sibling)  


   
    
with open("user.ged", "w") as writing_gedcom_file: 
    writing_gedcom_file.write("user_ged file:\n")
    lines_person= ["0 @I" + my_person.id +"@\n",
             "1 NAME " + my_person.firstName + " /" + my_person.lastName + "/\n",
             "1 SEX " + my_person.gender + "\n",
             "1 BIRT\n" + "2 DATE " + my_person.birthDate + "\n",
             "2 PLAC " + my_person.birthPlace + "\n",
             "1 DEAT\n" + "2 DATE " + my_person.deathDate + "\n",
             "2 PLAC " + my_person.deathPlace + "\n",
             #"1 FAMC @F" + my_person.parentFamilyID +"@\n",  #### add parent's family ID
             "1 FAMC @F" + "111" + "@\n"  #vremenno dlya illyustracii
             ]

    lines_parent = [
            #"0 FAMC @F" + my_person.parentFamilyID +"@ FAM\n",   #### add parent's family ID
              "0 FAMC @F" + "111" +"@ FAM\n",  #vremenno dlya illyustracii
              "1 HUSB @I" + my_person.fatherID +"@\n",
              "1 WIFE @I" + my_person.motherID +"@\n",
              "1 CHIL @I" + my_person.id +"@\n",
              ]
    
    #create a list of siblings (type: list of string)
    lines_sibling = []
    for i in my_person.sibling:
        temp = "1 CHIL @I" + i +"@\n" 
        lines_sibling.append(temp)
    
    writing_gedcom_file.writelines(lines_person + lines_parent + lines_sibling)
        
    
with open("user.ged", "r") as reading_gedcom_file:
        for line in reading_gedcom_file.readlines():
            print (line)
    
# Initialize the parser
#gedcom_parser = Parser()

# Parse my file
#gedcom_parser.parse_file(file_path)