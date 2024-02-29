from pathlib import Path

def absPath(file):
    path = str(Path(__file__).parent.parent.parent.absolute() / file)
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