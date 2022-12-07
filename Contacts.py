class Contacts:
    def __init__(self, name = None,mobileNo = None, city= None, profession = None):
        self.__name = name 
        self.__mobile_no = mobileNo
        self.__city  = city
        self.__profession = profession
    @property
    def name(self):
        return self.__name
    @property
    def mobile_no(self):
        return self.__mobile_no
    @property
    def city(self):
        return self.__city
    @property
    def profession(self):
        return self.__profession
    def print_contact(self):
        print('name:',self.name)
        print('mobile number:',self.mobile_no)
        print('city',self.city)
        print('profession', self.profession)
    
        