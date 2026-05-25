from random import randint

from celle import Celle

class Rutenett:
    def __init__(self,x,y):
        self.x = x  
        self.y = y
        self.rutenett = self.konstruer()
        self.koble_sammen()
        self.poeng = 0
        self.avslutt = False
        self.ant_bomber = 0

    def konstruer (self):
        teller = 0
        tom_matrise = []
        for y in range(self.y):
            tom_rad = []
            for x in range(self.x):
                celle=Celle(x,y)
                
                if randint(0,2) == 1:   
                    celle.sett_bombe()
                    teller += 1
                    
                tom_rad.append(celle )
            tom_matrise.append(tom_rad)
        self.ant_bomber = teller
        return tom_matrise


    def koble_sammen(self):
        for y in self.rutenett:
            for x in y:
                self.etabler_naboer(x)

    def hent_celle(self,x,y):
        return self.rutenett[y][x]


    def etabler_naboer(self,celle):
        x = celle.hent_x()
        y = celle.hent_y()

        naboliste= []
        if (x+1 >= 0 and y >= 0) and x+1 <= self.x -1 and  y<= self.y -1 :
            naboliste.append(self.hent_celle(x+1,y))

        if (x -1>= 0 and y >= 0) and x -1<= self.x -1 and  y<= self.y -1 :
            naboliste.append(self.hent_celle(x-1,y))  

        if (x >= 0 and y +1>= 0) and x <= self.x -1 and  y+1<= self.y -1 :
            naboliste.append(self.hent_celle(x,y+1))

        if (x >= 0 and y-1 >= 0) and x <= self.x -1 and  y-1<= self.y -1 :
            naboliste.append(self.hent_celle(x,y-1))

        if (x+1 >= 0 and y+1 >= 0) and x +1<= self.x -1 and  y+1<= self.y -1  :
            naboliste.append(self.hent_celle(x+1,y+1))

        if (x-1 >= 0 and y-1 >= 0) and x-1 <= self.x -1 and  y-1<= self.y -1 :
            naboliste.append(self.hent_celle(x-1,y-1))

        if (x+1 >= 0 and y-1 >= 0) and x+1 <= self.x -1 and  y-1<= self.y -1 :
            naboliste.append(self.hent_celle(x+1,y-1))

        if (x-1 >= 0 and y+1 >= 0) and x-1 <= self.x -1 and  y+1<= self.y -1 :
            naboliste.append(self.hent_celle(x-1,y+1))
        
        for nabo in naboliste:
                celle.sett_nabo(nabo)

    def skriv(self):
        teller = 0
        print("\n\n\n\n\n")
        print("poeng: ",self.poeng)
        print("  ",end ="")
        for x in range (self.x):
            if x < 10:
                x = "0" + f"{x}"
            print(x,end = "  ")
        print("\n")
        for y in self.rutenett:
        
            print(teller,end = " ")
            for x in y:
                print(x.hent_tegn(),end = "   ")
            print("\n")
            teller += 1

    def oppdater(self):
        for y in self.rutenett:
            for x in y:
                x.oppdater()
        if self.avslutt:
            return "avslutt"
        else:
            return self.poeng


    def gjett(self,x,y):
        if not (self.rutenett[y][x]).er_aapnet():
                self.poeng += 1

        if (self.rutenett[y][x]).aapne():
            if not (self.rutenett[y][x]).er_aapnet():
                self.poeng += 1
        else:
            self.avslutt = True
                
    def sjekk_åpnet(self):
        for y in self.rutenett:
            for x in y:
                print(x.sjekk_aapnet())

    def hent_avslutt(self):
        return self.avslutt

    def avslutt_spill(self):
        self.avslutt = True
        self.poeng = self.ant_bomber

    def flagg(self,x,y):
        self.rutenett[y][x].flagg()

    def hent_poeng(self):
        return self.poeng


    def sjekk_alle_flagget(self):
        for y in self.rutenett:
            for x in y:
                if x.sjekk_bombe():
                    if x.hent_tegn() != "¤":
                        return False
        return True

                    


rut = Rutenett(5,5)
#rut.skriv()
#rut.gjett(4,4)
#print(rut.oppdater())
#rut.skriv()
"""assert len(rut.hent_celle(1,0).hent_naboer()) == 5

for y in range(5):
    for x in range (5):
        print("rute:",x,y)
        for x in rut.hent_celle(x,y).hent_naboer():
            print(x)
    

assert len(rut.hent_celle(2,0).hent_naboer()) == 5
assert len(rut.hent_celle(3,0).hent_naboer()) == 5
assert len(rut.hent_celle(0,0).hent_naboer()) == 3
assert len(rut.hent_celle(4,0).hent_naboer()) == 3
assert len(rut.hent_celle(1,0).hent_naboer()) == 5"""

    #print(x)
#rut.sjekk_åpnet()
#rut.gjett(1,3)
#rut.oppdater()
#rut.skriv()

#rut.gjett(3,4)
#rut.skriv()

#print(rut.hent_celle(4,4))
