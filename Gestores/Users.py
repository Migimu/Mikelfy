from Clases.User import User

class Users():

    def __init__(self, users = []):
        self.__users: [User] = users
    
    def ADD_USER(self, user: User):
        self.__users.append(user)
        
    def ADD_USER(self, user: str, name: str, surname: str, password: str):
        user = User(self.GET_LAST_ID(), user, name, surname, password, "ESP", "14/10/2023")
        self.__users.append(user)

    def DELETE_USER(self, user: User):
        self.__users.remove(user)

    def FIND_USER(self, username: str):
        encontrado = False
        cont = 0
        user = None
        while cont < len(self.__users) and not encontrado:
            if username == self.__users[cont].GET_USER():
                user = self.__users[cont]
                encontrado = True
            cont+=1
        return user
    
    def GET_USERS(self):
        return self.__users
            
    def GET_LAST_ID(self):
        id = 0
        lenght = len(self.__users)
        if lenght == 0:
            id = 1
        else:
            id = int(self.__users[lenght - 1].GET_ID()) + 1         
        return id

    def GET_LENGHT(self):        
        return len(self.__users)




