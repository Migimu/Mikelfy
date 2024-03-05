class User:
    def __init__(self, id: int, username: str, name: str, email: str, password: str, country: int, birthDate: str):
        self.__id = id
        self.__username = username
        self.__name = name
        self.__email = email
        self.__password = password
        self.__country = country
        self.__birthDate = birthDate
        
    def __str__(self):
        return self.__id ,'.- ', self.__username  
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, username: str):
        self.__username = username
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password: int):
        self.__password = password         
        
    @property
    def country(self):
        return self.__country
    
    @country.setter
    def country(self, country: str):
        self.__country = country
        
    @property
    def birthDate(self):
        return self.__birthDate
    
    @birthDate.setter
    def birthDate(self, birthDate: str):
        self.__birthDate = birthDate


