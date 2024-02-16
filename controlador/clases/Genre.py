class Genre:

    def __init__(self, id: int, name: str):
        self.__id = id
        self.__name = name
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self.__name = name
 




