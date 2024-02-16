
from controlador.clases.User import User
from modelo.mockUsers import usuarios

class Users(object):
    def __init__(self, users = []):
        if len(users) == 0:
            self.__users = usuarios
        else:            
            self.__users = users
        
    def GET_USERS(self):
        return self.__users
    
    def GET_USERS_BY_ID(self, id: int):
        encontrado = False
        userEncontrado = None
        cont = 0
        while encontrado and cont < len(self.__users):
            user: User = self.__users[cont]
            if user.id == id:
                encontrado = True
                userEncontrado = user
            cont += 1
        return userEncontrado
    
    def GET_USER_BY_USERNAME(self, username: str):
        encontrado = False
        userEncontrado = None
        cont = 0       
        print(len(self.__users))
        while not encontrado and cont < len(self.__users):
            user: User = self.__users[cont]
            if user.username == username:
                encontrado = True
                userEncontrado = user
            cont += 1
        return userEncontrado
    
    def ADD_USER(self, user: User):
        self.__users.append(user)
        usuarios = self.__users

    def CHANGE_USER_PASSWORD(self, userId, newPassword):
        encontrado = False
        cont = 0
        while not encontrado and cont < len(self.__users):
            user: User = self.__users[cont]
            if user.id == userId:
                encontrado = True
                self.__users[cont].password = newPassword
            cont += 1
        usuarios = self.__users             

    def DELETE_USER(self, user: User):
        self.__users.remove(user)
            
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

        


