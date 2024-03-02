from pathlib import Path

def absPath(file, direcoryAts = "assets" , direcoryImg = "imagenes"):
    path = str(Path(__file__).parent.parent.parent.absolute() / direcoryAts / direcoryImg / file)
    return path

def FILTER(item, name: str, startYear: int, endYear: int, genre: int):    
    name = name.replace(" ", "").lower()
    itemName = item.name.replace(" ", "").lower()
    if ((name == "" or itemName == name) and 
        (startYear == None or item.releaseYear >= startYear) and 
        (endYear == None or item.releaseYear <= endYear) and 
        (genre == None or genre == item.genre)):
        return True
    return False

def FILTER_ARTIST(item, name: str, genre: int):    
    name = name.replace(" ", "").lower()
    itemName = item.name.replace(" ", "").lower()
    if ((name == "" or itemName == name) and
        (genre == None or genre == item.genre)):
        return True
    return False

def FIND(lista, id = None, name = None, callback = None):
    encontrado = False
    itemEncontrado = None
    cont = 0
    while not encontrado and cont < len(lista):
        item = lista[cont]
        if (item.id == id) or (item.name == name):
            if callback != None:
                callback()
            else:          
                itemEncontrado = item
            encontrado = True
        cont += 1
    return itemEncontrado