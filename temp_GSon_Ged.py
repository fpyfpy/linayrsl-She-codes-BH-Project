#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:20:42 2019

@author: irinasm
"""

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
###########   
my_user_data = [data["ID"], data["firstName"], data["lastName"], data["birthDate"], data["birthPlace"], data["gender"],
                data["motherID"], data["fatherID"], data["death"],  data["deathPlace"], data["deathDate"],
                data["sibling"]]
print (my_user_data)  
#############
my_person2 = Person(33)
my_person2.__print__()
#obj = Person(22)
#obj.__print__()

def fields(person):
    obj_fields = [person.id, person.firstName, person.lastName, person.birthDate, person.birthPlace, person.gender,
                  person.motherID, person.fatherID, person.death, person.deathPlace, person.deathDate,
                  person.sibling]
    return obj_fields

my_person2_fields = fields(my_person2)
print (my_person2_fields)

my_person2_fields = my_user_data
print (my_person2_fields)


#def sett_all_data(person, user_data):
 #  person_fields = fields(person)
  #  for f, d in (person_fields, user_data):
   #      f = d
    #return 0     
        
#sett_all_data(my_person2, my_user_data)
       
#print (my_person2)
print (fields(my_person2))        

#def sett_data(obj, field, data):
 #   obj.field = data

#def sett_all_data(obj, obj_fields, user_data):
#    for field, data in (obj_fields, user_data):
#        obj.sett_data(field, data)
#print (obj_fields)

print ()
#sett_data(obj, field, data)
    


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


