import pymysql
from Contacts import Contacts
class DB:
    def  __init__(self):
        self.__db  = None
        self.__cursor = None
        self.connect()
    def connect(self):
        if(self.__db!= None):
            return 
        self.__db= pymysql.connect(host = 'localhost',user  = 'root',password  =  'abc',database  =  'Contacts')
        self.__cursor = self.__db.cursor()
    def insert_contact(self,contact):
        if(self.__db==None):
            self.connect()
        query = 'INSERT INTO Contacts (username ,mobile_no , city  , profession) VALUES(%s , %s, %s, %s)'
        args= (contact.name,contact.mobile_no, contact.city , contact.profession)
        self.__cursor.execute(query,args)
        self.__db.commit()
    def is_username_exist(self,name):
        if(self.__db==None):
            self.connect()
        query = 'Select *  from contacts where username = %s'
        args = (name)
        self.__cursor.execute(query,args)
        data= self.__cursor.fetchall()
        if(len(data)==0):
            return None
        else:
            return data[0]
    def get_list_of_courses(self):
        if(self.__db==None):
            self.connect()
        query = 'SELECT * from contacts'
        self.__cursor.execute(query)
        data= self.__cursor.fetchall()
        list = []
        for item in data:
            contact = Contacts(item[1],item[2],item[3],item[4])
            list.append(contact)
        return list
    def __del(self):
        if(self.__cursor!= None):
            self.__cursor.close()
        if(self.__db!= None):
            self.__db.close()
