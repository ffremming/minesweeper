class Celle:
    def __init__ (self,x,y):
        self.x = x  
        self.y = y
        self.bombe = False
        self.naboer = []
        self.antall_bomber_nabo = 0
        self.flagget = False
        self.aapnet = False
        self.tegn = None
        self.oppdater_tegn()

    def aapne(self):
        if not self.bombe:
            self.aapnet = True
            for nabo in self.naboer:
                nabo.oppdater()
                
            self.oppdater()
            return True
        else:
            return False

    def sett_bombe (self):
        self.bombe = True
    
    def sjekk_bombe (self):
        return self.bombe

    def flagg(self):
        self.flagget = True
        self.oppdater_tegn()
    
    def avflagg (self):
        self.flagget = False

    def sett_nabo(self,nabo):
        self.naboer.append(nabo)

    def hent_antall_bomber(self):
        teller = 0
        for x in self.naboer:
            if x.sjekk_bombe():
                teller += 1
                
        self.antall_bomber_nabo = teller

    def hent_aapnet_nabo(self):
        for x in self.naboer:
            
            if x.sjekk_aapnet():
                
                return True 
        return False

    def er_aapnet(self):
        return self.aapnet

    def hent_tegn(self):
        return self.tegn

    def oppdater_tegn(self):
        if self.flagget == True:
            self.tegn = "¤"

        elif self.aapnet and self.bombe == False:
            self.tegn = f"{self.antall_bomber_nabo}"
        else:
            
            if self.hent_aapnet_nabo():
                if self.antall_bomber_nabo == 0 and not self.bombe:
                    self.tegn = "0"
                else:
                    self.tegn =f"{self.antall_bomber_nabo}"
            else:
                self.tegn = "-"

    def hent_x(self):
        return self.x

    def hent_y(self):
        return self.y

    def oppdater(self):
        (self.hent_antall_bomber())
       
        self.oppdater_tegn()
        

    def hent_naboer(self):
        return self.naboer

    def sjekk_aapnet(self):
        return self.aapnet

    def __str__(self):
        return f"{self.x},{self.y}"