# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 03:52:39 2021

@author: erdmk
"""
import json 

with open ("users.json") as users:
    
    data = json.load(users)
    

class information:
    
    def __init__ (self, names , nameValue , option , addressValue):
       
        self.names = names
        self.nameValue = nameValue
        self.option = option
        self.addressValue = addressValue
        
    def display(names):
        
        print("*Your options!*")
        for i in range(len(names)):
            print(str(i) + " - ) " + names[i])
            
   
    def chooseNames(nameValue):
        
        nameValue = int(nameValue) + 1
        print(data[nameValue])
        
    def chooseSection(nameValue , option):
        
        nameValue = int(nameValue)
        print(data[nameValue][option])
        
    def chooseAdress(nameValue , option , adressValue):
        
        nameValue = int(nameValue)
        print(data[nameValue][option][adressValue])
        
    def chooseCompany(nameValue , option , cSection):
        
        nameValue = int(nameValue)
        print(data[nameValue][option][cSection])


while True:
    names = ["Leanne Graham" , "Ervin Howell" , "Clementine Bauch" , "Patricia Lebsack"
         
         "Chelsey Dietrich" , "Mrs. Dennis Schulist" , "Kurtis Weissnat" , 
         
         "Nicholas Runolfsdottir V" , "Glenna Reichert" , "Clementina DuBuque" ] 

    print(information.display(names))

    nameValue = input ("Enter the your name : " )

    information.chooseNames(nameValue)

    option = input ("Enter your information section : " ) 

    information.chooseSection(nameValue, option)

    if option == "address":
    
        adress = ["street" , "suite" , "city" ,  "zipcode"]

        print(information.display(adress))

        adressValue = input ("Enter your choice : " )

        information.chooseAdress(nameValue, option, adressValue)
        
    if option == "company":
        
        company = ["name" , "catchPhrase" , "bs"]
        
        print(information.display(company))
        
        cSection = input ("Enter your company section : ") 
        
        information.chooseCompany(nameValue , option , cSection)
        
        
    c = input ("Do you want to continue  Y / N : ")
    
    if c == "N":
        break
    
    



    
    