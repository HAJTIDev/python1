class SamochodBenzynowy:
    def __init__(self,benzyna,spalanie):
        self.benzyna=benzyna
        self.spalanie=spalanie
        self.chwilowy_zbiornik=0
        self.chwilowka=0

    def zatankuj(self,ilosc):
        self.ilosc=ilosc
        self.chwilowy_zbiornik+=ilosc
        self.chwilowka=self.chwilowy_zbiornik
        print("zatankowano",ilosc)
        print("aktualnie w baku jest",self.chwilowy_zbiornik)
        print("moze sie zmieścić jeszcze",self.benzyna-self.chwilowy_zbiornik)

    def sprawdz(self,odl):
        self.odl=odl
        if self.chwilowka < (self.odl/100)*self.spalanie:
            print("braknie paliwa")
        else:
            print("da się na spokojnie, zostanie jeszcze",self.chwilowka-(odl/100)*self.spalanie)
            self.chwilowka=self.chwilowy_zbiornik
            
    def jedz(self,kilometry):
        self.kilometry=kilometry
        self.chwilowy_zbiornik-=(kilometry/100)*self.spalanie
        print("zostalo jeszcze",self.chwilowy_zbiornik)


s1=SamochodBenzynowy(50,2)
s1.zatankuj(20)
s1.sprawdz(10)
s1.jedz(20)