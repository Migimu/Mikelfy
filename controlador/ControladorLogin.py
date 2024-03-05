from controlador.clases.User import User
from controlador.gestores.Countries import Countries
from controlador.gestores.Users import Users
from modelo.Conn import CONEXION


class ControladorLogin:
    
    def __init__(self):
        self.users = Users()
        self.countries = Countries()
        
    def GET_COUNTRIES(self):
        return self.countries.GET_COUNTRIES()
      
    def VALIDAR(self, username, password):       
        user: User = self.users.GET_USER_BY_USERNAME(username)
        if user != None:
            if user.password == password:
                return 1, user
            else:
                return 0, user
        else:          
            return -1, username
        
    def VALIDATE_USERNAME(self, username):       
        user: User = self.users.GET_USER_BY_USERNAME(username)
        if user == None:
            return True
        else:          
            return False
        
    def RESGISTRATE(self, username, name, email, country, birthDate, password):       
        self.users.ADD_USER(User(0, username, name, email, password, country, birthDate))
        
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
        
    def LOGOUT(self):
        conn = CONEXION()
        conn.CREATE_USERS()   
        conn.UPDATE_USERS()   
        conn.CREATE_PLAYLISTS()   
        conn.UPDATE_PLAYLISTS()   
        conn.DELETE_PLAYLISTS()   
 
        

        




