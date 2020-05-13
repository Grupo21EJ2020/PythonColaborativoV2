class XboxOne():
    def __init__(self, version,color):
        self.version = version
        self.color = color
    
    def imprimirinfo(self):
        print(f"Version: {self.version} Color: {self.color}")
