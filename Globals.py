def calculadora():
    n1=3
    n2=5
    def sumar(n1,n2):
       suma=n1+n2
       return suma
    def leer_numeros():
      nonlocal n1,n2
      n1=int(input("inserta un numero por favor:"))
      n2=int(input("inserta un numero por favor:"))
      return sumar(n1,n2)
    def leer_numeros2():
      n1=int(input("inserta un numero por favor:"))
      n2=int(input("inserta un numero por favor:"))
      return sumar(n1,n2)
     
    
    print(sumar(n1,n2))
    print(leer_numeros())
    print(leer_numeros2())
    
calculadora()



