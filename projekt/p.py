#projekt 
 
#sorting info från https://docs.python.org/3/howto/sorting.html
from operator import itemgetter, attrgetter

class Aktie:
    def __init__(self, namn, soliditet, pe, ps):
        self.namn = namn
        self.soliditet = soliditet
        self.pe = pe
        self.ps = ps

        self.historik = list() # tillhör objektet Aktie

    def __repr__(self):
        return f'{self.namn} {self.soliditet} {self.pe} {self.ps}' # gör så vi kan rangordna beta
        #annars 
        # <__main__.Aktie object at 0x7ffda4a47ca0>
        # <__main__.Aktie object at 0x7ffda4a47cd0>
        # <__main__.Aktie object at 0x7ffda4a47eb0>

    def lägg_till_historik(self, historikobjekt): # funktion som tar ett historikobjekt
        self.historik.append(historikobjekt) # och stoppar in det i self.historik som då skapar en lista av historik-objekt

    def beräkna_beta(self, omx):
        self.beta = ((self.historik[-1].pris-self.historik[0].pris))/self.historik[0].pris/(omx[-1].index/omx[0].index)
        #fel formel dock

    def beräkna_kursändring(self): #beräknar kursändringen i %
        self.kursändring = (self.historik[-1].pris-self.historik[0].pris)/self.historik[-1].pris
        return self.kursändring

    def största_och_minsta(self): # hittar största och minsta värdet för priset i listan self.historik
        self.min = min([h.pris for h in self.historik])
        self.max = max([h.pris for h in self.historik])
        return # behöver ej return ty värdet finns sparat i objektet
 
class Historik:
    def __init__(self, datum, pris):
        self.datum = datum
        self.pris = pris

    '''def __repr__(self):
        return f'{self.datum} {self.pris}' ''' # behövs ej

class Börs:
    def __init__(self, datum, index):
        self.datum = datum
        self.index = index

    '''def __repr__(self):
        return f'{self.datum} {self.index}' ''' # behövs ej

def första_filen():
     
    f = open('fundamenta.txt', 'r', encoding = 'ASCII')
    lista = f.readlines()
    f.close()

    info_rader = lista

    aktierna = [] # lista av aktie-objekt [namn, soliditet, pe, ps]

    for i in range(0,len(info_rader), 4): #går igenom fundamenta.txt
        #rstrip endast på strängen ty int sköter det på resten
        aktierna.append(Aktie(info_rader[i].rstrip('\n'), int(info_rader[i+1]), int(info_rader[i+2]), float(info_rader[i+3])))

    return aktierna # [Ericsson 30 -1 0.35, Electrolux 40 10 0.4, AstraZeneca 50 22 3.5]

def andra_filen(aktierna):

    # här vill vi dels läsa in kurser.txt (datum, pris)
    # men även tilldela dessa till rätt aktie

    f = open('kurser.txt', 'r', encoding = 'ASCII')
    lista = f.readlines()
    f.close()

    info_rader = lista

    for rad in info_rader:
        if not '\t' in rad: # hittar namn
            for a in aktierna: # från andra filen
                if rad.rstrip('\n') == a.namn: # om aktierna(Ericsson, Electrolux, AstraZeneca) i kurser.txt överresnstämmer med aktierna i aktie-objektet
                    aktie = a # döper vi om dessa till aktie
            continue
        info = rad.split('\t') # skapar en lista med [datum, pris]
        
        aktie.lägg_till_historik(Historik(str(info[0]), float(info[1]))) #lägger till historik från kurser.txt för varje aktie
        #historik för Ericsson, Electrolux, AstraZeneca respektive i listan aktierna

    return 

def tredje_filen():

    # här vill vi läsa in omx.txt (datum, index)
    # detta för att kunna beräkna beta

    f = open('omx.txt', 'r', encoding = 'ASCII')
    lista = f.readlines()
    f.close()

    info_rader = lista

    börs_objekt= []

    for rad in info_rader:
        info = rad.split('\t')
        
        börsen = Börs(str(info[0]), float(info[1]))
        börs_objekt.append(börsen)

    return börs_objekt

def indata(fråga, lägsta, högsta):

    Korrekt_inmatning = False

    while not Korrekt_inmatning:
        svar = input(fråga)
        Korrekt_inmatning = True
        try:
            svar = int(svar)
            if svar >= lägsta and svar <= högsta:
                return svar
            else:
                Korrekt_inmatning = False
                print(f'\nVänligen ange ett alternativ mellan {lägsta} och {högsta}')
        except ValueError:
            Korrekt_inmatning = False
            print(f'\nVänligen ange ett heltal mellan {lägsta} och {högsta}')

def main():
    
    aktierna = första_filen() 
    andra_filen(aktierna) # informationen ovan in i andra_filen 

    omx = tredje_filen() 

    # sparar minne genom att tilldela omx datan när det behövs istället för som instansvariabel
    for a in aktierna: 
        a.beräkna_beta(omx) # beräknar beta
        a.största_och_minsta() # hittar största och minsta värdet för priset i listan self.historik 
         
    sorterad_lista = []

    fortsätt = True

    while fortsätt:
        
        val = indata('\n1 - Fundamental analys\n2 - Teknisk analys\n3 - Rangordning på beta\n4 - Avsluta\n', 1, 4)

        if val == 1:
            
            x = indata('\nFundamental analys kan göras på följande aktier: \n1.Ericsson\n2.Electrolux\n3.AstraZeneca\nVilken aktie vill du göra fundamental analys på?', 1, 3)
            if x == 1:
                for a in aktierna:
                    if a.namn == 'Ericsson':
                        print('\nFundamental analys för', a.namn,'\nföretagets soliditet är', a.soliditet, '\nföretagets p/e-tal är',a.pe,'\nföretagets p/s-tal är',a.ps) 
            elif x == 2:
                for a in aktierna:
                    if a.namn == 'Electrolux':
                        print('\nFundamental analys för', a.namn,'\nföretagets soliditet är', a.soliditet, '\nföretagets p/e-tal är',a.pe,'\nföretagets p/s-tal är',a.ps)
            elif x ==3:
                for a in aktierna:
                    if a.namn == 'AstraZeneca':
                        print('\nFundamental analys för', a.namn,'\nföretagets soliditet är', a.soliditet, '\nföretagets p/e-tal är',a.pe,'\nföretagets p/s-tal är',a.ps)
        elif val == 2:

            y = indata('\nTeknisk analys kan göras på följande aktier: \n1.Ericsson\n2.Electrolux\n3.AstraZeneca\nVilken aktie vill du göra teknisk analys på?', 1, 3)
            if y == 1:    
                for aktie in aktierna:
                    if aktie.namn == 'Ericsson':
                        print('\nTeknisk analys för',aktie.namn,'\nkursutveckling(30 senaste dagarna)',aktie.beräkna_kursändring(),'%','\nbetavärde',aktie.beta,'\nlägsta kurs(30 senaste dagarna)',aktie.min,'\nhögsta kurs(30 senaste dagarna)',aktie.max)
            elif y == 2:
                for aktie in aktierna:
                    if aktie.namn == 'Electrolux':
                        print('\nTeknisk analys för',aktie.namn,'\nkursutveckling(30 senaste dagarna)',aktie.beräkna_kursändring(),'%','\nbetavärde',aktie.beta,'\nlägsta kurs(30 senaste dagarna)',aktie.min,'\nhögsta kurs(30 senaste dagarna)',aktie.max)

            elif y == 3:
                for aktie in aktierna:
                    if aktie.namn == 'AstraZeneca':
                        print('\nTeknisk analys för',aktie.namn,'\nkursutveckling(30 senaste dagarna)',aktie.beräkna_kursändring(),'%','\nbetavärde',aktie.beta,'\nlägsta kurs(30 senaste dagarna)',aktie.min,'\nhögsta kurs(30 senaste dagarna)',aktie.max)
        elif val == 3:
            print('Rangordning av aktier med avseende på dess betavärde')
            sorterad_lista = sorted(aktierna, key = attrgetter('beta'))
            for beta in sorterad_lista:
                print(beta)
        elif val == 4:
            fortsätt = False
            
main()
    

    

