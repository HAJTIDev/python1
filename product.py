class Product:
    def __init__(self,id,imie,cena,):
        self.id=id
        self.imie=imie
        self.cena=cena
    
    def print_info(self):
        print("produkt:",self.imie," id:",self.id," cena:",self.cena )

product=Product(1,'Woda',10.99)
product.print_info()