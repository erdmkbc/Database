# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 03:11:47 2021

@author: erdmk
"""

import sqlite3

connection = sqlite3.connect("chinook.db")
   
print("Your information")
for row in cursor:
    print(row[0])

class database:
    
    def displayOptions():
        connection.row_factory = sqlite3.Row
        cursor = connection.execute('SELECT * FROM customers')
        
        row = cursor.fetchone()
        names = row.keys()
        
        print("Your Options!")
        for i in range(len(names)):
            print(str(i + 1 ) + "- ) " + names[i])
            
    def getAllOptions(option):
        
        cursor = connection.execute("SELECT %s FROM customers" %(option))
        print("Your information")
        for row in cursor:
            print(row[0])
            
    def chooseFilter(option , filt , target):
        
        cursor = connection.execute("SELECT {} FROM customers WHERE {} = '{}'"  .format(option , filt , target))     
        print("Your information")
        for row in cursor:
            print(row[0])
            
    def ordering(option , filt , target ):
        
        cursor = connection.execute("SELECT {} FROM customers WHERE {} = '{}' order by {}" .format(option , filt , target , option) )
        print("Your list ordered!")
        for row in cursor:
            print(row[0])
            
    def whereLike(option , filt , target):
        
        cursor = connection.execute("SELECT {} FROM customers WHERE {} LIKE '%{}%'".format(option, filt, target))
        print("Your like")
        for row in cursor:
            print(row[0])
            
    def insertInformation(target1 , target2 , target3 , information1 , information2 , information3):
        
        cursor = connection.execute("""INSERT INTO customers ({},{},{}) 
                                    VALUES ('{}' , '{}' , '{}' ) """ 
                                    .format(target1 , target2 , target3 ,information1 , information2 , information3)) 
                                                                                                      
        connection.commit()
        
    def deleteInformation(target , information):
        
        cursor = connection.execute("DELETE from customers where {} = '{}' " .format(target , information))
        
        connection.commit()
        
    

while True:
    
    print("***Welcome to chinook from customers database***")
    print("***Welcome to chinook from customers database***")
    print("\n")

    print("***Database Options***")
    database.displayOptions()

    usersOption = input("Which information do you want to view : ")
    database.getAllOptions(usersOption)

    print("\n")

    filterDecision = str(input("Do you want to use filter : "))

    if(filterDecision == "Y"):
       filterTarget = input("You want to filter the target: ")
       filterOption = input("You want to filter the feature: ")
       filterInformation = input("You want to filter the information: ")
   
       database.chooseFilter(filterTarget, filterOption, filterInformation)

       orderDecision = str(input("Do you want to use ordering : "))

    if(orderDecision == "Y"):
       database.ordering(filterTarget, filterOption, filterInformation)
   
    LikeDecision = str(input("Do you search a letter in database : "))

    if(LikeDecision == "Y"):
       likeTarget = input("You want to filter the target: ")
       likeOption = input("You want to filter the feature: ")
       likeInformation = input("You want to filter the letter: ")   
   
       database.whereLike(likeTarget,likeOption,likeInformation)
    
       insertDecision = str(input ("Do you want to add information : "))

    if(insertDecision == "Y"):
       feature1 = input ("First Feature you want to add: ")
       feature2 = input ("Second Feature you want to add: ")
       feature3 = input ("Third Feature you want to add: ")
    
       infoinsert1 = input ("First Enter information that you want to : ")
       infoinsert2 = input ("Second Enter information that you want to : ")
       infoinsert3 = input ("Third Enter information that you want to : ")
    
       database.insertInformation(feature1,feature2,feature3,infoinsert1,infoinsert2,infoinsert3)
    
    deleteDecision = str(input ("Do you want to delete any information : "))

    if(deleteDecision == "Y"):
      featureDelete = input("Enter feature that you want to delete : ")
      informationDelete = input ("Enter information that you want to delete : ")
    
      database.deleteInformation(featureDelete , informationDelete)
      
    D = str(input ("Do you want to continue(Y/N) : "))
    
    if(D == "N"):
        break

        
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    
   
    




        
