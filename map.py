import world,os

class MapReader:
    def __init__(self,sourcepath):
        self.file = open(sourcepath,os.O_RDONLY)
        
    def checkheader(self):
        