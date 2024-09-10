class SamochodElektryczny:
    def __init__(self,max_zasieg):
        self.max_zasieg= max_zasieg
        self.zasieg_chwilowy=max_zasieg

    def laduj(self):
        self.zasieg_chwilowy=self.max_zasieg

    def czyda(self,kilometry):
        if self.zasieg_chwilowy <kilometry:
            print("nie dojedzie się jest tylko",self.zasieg_chwilowy)
            
    def jedz(self,kilometry):
        self.czyda(kilometry)
        if kilometry <self.zasieg_chwilowy:
            print(kilometry)
            self.zasieg_chwilowy-=kilometry
    
            
s1=SamochodElektryczny(300)
s1.jedz(50)
s1.jedz(60)
s1.jedz(100)