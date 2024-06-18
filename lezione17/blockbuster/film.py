class Film:

    def __init__(self, id:int, title:str):

        self.id = id
        self.title = title
    
    def setID(self, id:int):

        self.id = id
    
    def SetTitle(self, title:str):

        self.title = title
    
    def getId(self):

        return self.id
    
    def getTitle(self):

        return self.title
    
    def isEqual(self, otherFilm:str):

        if self.id == otherFilm:
            return True
        else:
            return False
    
