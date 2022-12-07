from Model import DB
class Controller:
    def validateUsername(self,name):
        db= DB()
        status = db.is_username_exist(name)
        if(name==''):
            return (False, 'Please Enter a name ')
        if(status!= None):
            return (False, 'Username already exist please choose a different one')
        return (True,'')
    def validate_mobile_no(self,mobile_no):
        if(mobile_no[0]!= '+'):
            return (False, 'Please Enter a valid number')
        status = mobile_no.removeprefix('+')
        try:
            status = int(mobile_no)
            return (True,'')
        except Exception as e:
            return (False, 'Please Enter a valid number')
    def insert_contact(self,contact):
        db= DB()
        db.insert_contact(contact)
    def get_Courses(self):
        db = DB()
        list = db.get_list_of_courses()
        return list
    def show_Search_BY_Name_Results(self,name):
        db= DB()
        status  = db.is_username_exist(name)
        return status