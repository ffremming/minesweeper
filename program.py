from rutenett import Rutenett

def program():
    a,b = input("skriv inn dimensjonene for spillet ditt: x,b :  ").split(",")
    rutenett = Rutenett(int(a),int(b))
    
    while not rutenett.hent_avslutt():
        rutenett.skriv()
        print("hvis du vil flagge - skriv f,ellers skriv koordinat: ")
        
        inp = (input("skriv koordinat(x,y) eller f ")).split(",")
        if inp == ["f"]:
            x,y = (input("skriv koordinat(x,y) for flagg")).split(",")
            rutenett.flagg(int(x),int(y))
        else:
            x,y = inp
            rutenett.gjett(int(x),int(y))

        if rutenett.sjekk_alle_flagget():
            rutenett.skriv()
            print("Du fant alle bombene!")
            rutenett.avslutt_spill()
    

    print(f"spillet er over, poengsum: {rutenett.hent_poeng()}")
program()