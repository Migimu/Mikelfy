from controlador.clases.User import User
from controlador.gestores.Users import Users


class ControladorLogin:
    
    def __init__(self):
        self.users = Users()
      
    def VALIDAR(self, username, password):       
        user: User = self.users.GET_USER_BY_USERNAME(username)
        if user != None:
            if user.password == password:
                return 1, user
            else:
                return 0, user
        else:          
            return -1, username
        
    def RESGISTRAR(self, username, name, email, country, birthDate, password):       
        user: User = self.users.GET_USER_BY_USERNAME(username)
        if user == None:
            self.users.ADD_USER(User(0, username, name, email, password, country, birthDate))
            return True
        else:          
            return False
        
    def VALIDATE_PASSWORD(self, user, password, newPassword):
        if password == newPassword:
            if user.password == newPassword:
                return 0
            else:               
                return 1
        else:          
            return -1
        
    def CHANGE_PASSWORD(self, userId, newPassword):  
        self.users.CHANGE_USER_PASSWORD(userId, newPassword)
        

        




