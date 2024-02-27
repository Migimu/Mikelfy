from pathlib import Path

def absPath(file):
    path = str(Path(__file__).parent.parent.absolute() / file)
    return path

def FILTER(item, name: str, startYear: int, endYear: int, genre: int):    
    name = name.replace(" ", "").lower()
    itemName = item.name.replace(" ", "").lower()
    if ((name == "" or itemName == name) and 
        (startYear == None or item.releaseYear >= startYear) and 
        (endYear == None or item.releaseYear <= endYear) and 
        (genre == None or item.genre == genre)):
        return True
    return False

# def GET_ICON(item):    
#     if ((name == "" or item.name == name) and 
#         (startYear == None or item.releaseYear >= startYear) and 
#         (endYear == None or item.releaseYear <= endYear) and 
#         (genre == None or item.genre == genre)):
#         return True
#     return False
