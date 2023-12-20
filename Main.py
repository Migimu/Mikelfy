from Clases.User import User
from Gestores.Users import Users


class MAIN:
    def __init__(self):
        self.users = Users()
        
    def MENU(self):
        opcion = 1 
        while (opcion > 0 and opcion <= 4):
            opcion = self.PEDIR_OPCION()
            match opcion:
                case 1:
                    self.RESGISTRAR_USUARIO()
                case 2:
                    self.INICIAR_SESION()
                case 3:
                    self.ELIMINAR_USUARIO()
                case 4:
                    self.MOSTRAR_USUARIOS()      
        print("Adios")
    
    def PEDIR_OPCION(self):
        isValid = False
        resp = 0
        while not isValid:
            try:
                print("Selecciona una opcion: \n 1. Registrarse \n 2. Iniciar sesion \n 3. Eliminar usuarios \n 4. Mostrar usuarios \n 0. Salir")
                resp = int(input())    
                isValid = True               
            except:
                print("Introduce un numero valido")
                
        return resp
                
    def RESGISTRAR_USUARIO(self):
        user = self.PEDIR_TEXTO("Introduce un nombre para tu usuario:")
        name = self.PEDIR_TEXTO("Introduce tu nombre:")
        email = self.PEDIR_TEXTO("Introduce tu correo electronico:")
        password = self.PEDIR_TEXTO("Introduce una contrasenia:")
        self.users.ADD_USER(user, name, email, password)
        
    def INICIAR_SESION(self):
        if (self.users.GET_LENGHT() > 0):                  
            self.PEDIR_USUARIO()
        else:
            print("No hay ningun usuario registrado")
            self.VOLVER_REGISTRAR()     
    
    def PEDIR_USUARIO(self):
        inputUser = self.PEDIR_TEXTO("Introduce tu nombre de usuario:")
        user = self.users.FIND_USER(inputUser)
        if user != "":
            self.PEDIR_PASSWORD(user)
        else:
            print("El usuario introducido no existe")
            self.VOLVER_REGISTRAR()     
            
    def VOLVER_REGISTRAR(self):
        resp = self.PEDIR_TEXTO("Quieres registrarse? Si/No")
        if resp.upper() == "SI":
            self.RESGISTRAR_USUARIO()
            
    def ELIMINAR_USUARIO(self):
        username = self.PEDIR_TEXTO("Introduce el nombre del usuario a eliminar:")
        user = self.users.FIND_USER(username)
        if user != None:
            self.users.DELETE_USER(user)
            print("El usuario ", user.GET_USER() ," se ha eliminado")
        else:
            print("El usuario introducido no existe")

    def PEDIR_PASSWORD(self, user: User):
        inputPassword = self.PEDIR_TEXTO("Introduce tu contrasenia:")
        while user.GET_PASSWORD() != inputPassword:
            inputPassword = self.PEDIR_TEXTO("Contrasenia incorrecta, vuelve a escribirla:")
        else: 
            print("Bienvenido ", user.GET_NAME())          
    
    def PEDIR_TEXTO(self, text: str):
        print(text)
        resp = input()   
        return resp
    
    def MOSTRAR_USUARIOS(self):
        user: User
        for user in self.users.GET_USERS():
            print("Username: ",user.GET_USER(),"\nName: ",user.GET_NAME(),"\nName: ",user.GET_EMAIL(),"\nBirthdate: ",user.GET_BIRTHDATE(),"\n#####################")
        




