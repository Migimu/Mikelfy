from assets.util.Utils import FIND, GET_LAST_ID
from controlador.clases.User import User
from modelo.LocalStorage import localStorage

class Users:
    def __init__(self, users = []):
        if len(users) == 0:
            self.__users = localStorage.users
        else:            
            self.__users = users
        
    def GET_USERS(self):
        return self.__users
    
    def GET_USERS_BY_ID(self, id: int):
        userEncontrado = FIND(self.__users ,id=id)
        return userEncontrado
    
    def GET_USER_BY_USERNAME(self, username: str):
        encontrado = False
        userEncontrado = None
        cont = 0
        while not encontrado and cont < len(self.__users):
            user: User = self.__users[cont]
            if user.username == username:
                encontrado = True
                userEncontrado = user
            cont += 1
        return userEncontrado
    
    def ADD_USER(self, user: User):
        user.id = GET_LAST_ID(self.__users)
        self.__users.append(user)
        localStorage.createdUsers = user

    def CHANGE_USER_PASSWORD(self, userId, newPassword):
        encontrado = False
        cont = 0
        while not encontrado and cont < len(self.__users):
            user: User = self.__users[cont]
            if user.id == userId:
                encontrado = True
                self.__users[cont].password = newPassword
                localStorage.updatedUsers = self.__users[cont]
            cont += 1
                     
            
    

        


