import sqlite3

##########################################################
#                       My Object
##########################################################

class DataBase():

    def __init__(self,nameDatabase : str ):
        
        """
            This is the creator of my object
            This method is called during the creation of my object
            The goal of this method is to create a connection from my code to my database  
        """
        
        self.db = sqlite3.connect(nameDatabase)
        self.cur = self.db.cursor()



    def createTable(self, nameTable : str, column : str ):

        """
            The goal of this method is to add new table on my database
            This method need 2 parameters :
                - the name of the table => string
                    exemple : "user"
                - some informations about my column
                    exemple : "id CHAR (32) PRIMARY KEY , name VARCHAR(20)"
        """

        self.cur.execute('CREATE TABLE IF NOT EXISTS' + name + ' ( ' + column + ' )' )
        self.db.commit()



    def addData(self,table : str ,listColumn : str ,data):

        """
            The goal of this method is to add data on one table
            This method need 3 parameters :
                - the name of the table => string
                    exemple : "user"
                - the name of the colmun => string
                    exemple : "id,name"
                - the data => tuple
                    exemple : (3,'thomas')
        """

        ### I calcule the number of ? with the column number of my table
        nbOfColumn = ""
        for i in range(0,len(listColumn.split(',')) - 1 ,1) :
            nbOfColumn = nbOfColumn + ("?,")
        nbOfColumn = nbOfColumn + ("?")
            
        ### I creat my request
        request = 'INSERT INTO ' + table + ' ( ' + listColumn + ' ) VALUES ( ' + nbOfColumn + ')'

        ### I execute my request
        self.cur.execute( request , data)
        self.db.commit()



    def printTableData(self, column : str , table : str):

        """
            The goal of this method is to print one table of my database.
            This method need 2 parameters :
                - the name of the table => string
                    exemple : "user"
                - the name of the columns => string
                    warning : if you want to print all column, you can use "*"
        """

        ### I capture all data of my table 
        self.cur.execute("Select " + column + " FROM " + table )

        ### I print all lign of my "list"
        for ligne in self.cur :
            print("id : {0}  | name : {1} ".format(ligne[0],ligne[1]))



    def updateData(self, table : str , newData : str , condition : str):

        """
            The goal of this method is to update data in one table.
            This method need 2 parameters :
                - the name of the table => string
                    exemple : "user"
                - the condition => string
                    exemple : name = "Paul"
                - the new data => string
                    exemple : name = "Martin",id = 8
        """
                
        self.cur.execute("UPDATE " + table + " SET " + newData + " WHERE " + condition)
        self.db.commit()


        
    def deleteData(self, table : str , condition : str):
        
        """
            The goal of this method is to delete data in one table.
            This method need 2 parameters :
                - the name of the table => string
                    exemple : "user"
                - the condition => string
                    exemple : name = "Martin",id = 8
        """
        
        self.cur.execute("DELETE FROM " + table + " WHERE " + condition)
        self.db.commit()


          
    def __del__(self):

        """
            The goal of this method is to close my dataBase after the end of the programm
            exemple :
                del objectName
        """
        
        self.db.close()
        print("\n End of the program")








##########################################################
#                       My code
##########################################################

myDB = DataBase("week9Task.db") ### I create my object

help(myDB.addData) ### I print some informations about my method on the terminal

print("\n Add Data : ")
myDB.addData("user","id,name",(3,"Pierre") )### I add some data
myDB.printTableData("*","user") ### I print the table called "user" on the terminal

print("\n Update Data : ")
myDB.updateData("user","id = 8,name = 'Martin'","name = 'Pierre'")### i update some data
myDB.printTableData("*","user") ### I print the table called "user" on the terminal

print("\n Delete Data : ")
myDB.deleteData("user","name = 'Martin'") ### I delete some data
myDB.printTableData("*","user")### I print the table called "user" on the terminal

del myDB ### I destroy my object
