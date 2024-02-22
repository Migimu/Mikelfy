from pathlib import Path

def absPath(file):
    path = str(Path(__file__).parent.parent.absolute() / file)
    return path





