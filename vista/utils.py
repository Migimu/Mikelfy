from pathlib import Path

def absPath(file):
    path = str(Path(__file__).parent.parent.absolute() / file)
    return path

def FILTER(item, name: str, startYear: int, endYear: int, genre: int):    
    if ((name == "" or item.name == name) and 
        (startYear == None or item.releaseYear >= startYear) and 
        (endYear == None or item.releaseYear <= endYear) and 
        (genre == None or item.genre == genre)):
        return True
    return False

