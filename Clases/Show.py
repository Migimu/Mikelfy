from Gestores.Artists import Artists


class Show:
    
    __id: str
    __name: str
    __contry: str
    __price: int
    __urlToBuyTicket: str
    __date: int
    #__artists: Artists
    
    def __init__(self, id: int, name: str, contry: str, price: int, urlToBuyTicket: str, date: int):
        self.__id = id
        self.__name = name
        self.__contry = contry
        self.__price = price
        self.__urlToBuyTicket = urlToBuyTicket
        self.__date = date

    
    def GET_ID(self):
        return self.__id
    
    def GET_NAME(self):
        return self.__name
    
    def SET_NAME(self, name: str):
        self.__name = name
        
    def GET_COUNTRY(self):
        return self.__contry
    
    def SET_COUNTRY(self, contry: str):
        self.__contry = contry
        
    def GET_PRICE(self):
        return self.__price
    
    def SET_PRICE(self, price: int):
        self.__price = price
        
    def GET_URL_TO_BUY_TICKET(self):
        return self.__urlToBuyTicket
    
    def SET_URL_TO_BUY_TICKET(self, urlToBuyTicket: str):
        self.__urlToBuyTicket = urlToBuyTicket
        
    def GET_DATE(self):
        return self.__date
    
    def SET_DATE(self, date: int):
        self.__date = date
    



