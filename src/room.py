# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description): #constructor
        self.name = name
        self.description = description
        
    def __str__(self): #string : prints out the rooms name "Just a string", unique
        return f"{self.name}"   
    
   
