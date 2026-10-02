class Estuche:
    def __init__(self, color, size, material):
        self.color = color
        self.size = size
        self.material = material
        
    def información(self):
        print(f"Tu estuche es de color {self.color}, su tamaño es {self.size} y está hecho de {self.material}.")