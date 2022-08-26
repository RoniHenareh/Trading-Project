#projekt, v2
 
from operator import itemgetter, attrgetter
import yfinance as yf
from yfinance import ticker

class Aktie: 
    def __init__(self, ticker):
        
        self.ticker = yf.Ticker(ticker)
        
        self.hitta_namn()
        self.hitta_pe()
        self.hitta_ps()
        self.hitta_beta()
        self.hitta_soliditet()
    
    def __repr__(self): 
        return f'{self.namn} {self.beta} {self.pe} {self.ps} {self.soliditet}' #det som är med i rangordningen

    def hitta_namn(self):
        self.namn = self.ticker.info['shortName']
        if self.namn == None:
            self.namn = 'inte tillgängligt'
    
    def hitta_pe(self):
        self.pe = self.ticker.info['forwardPE']
        if self.pe == None:
            self.pe = 'inte tillgängligt'

    def hitta_ps(self):
        self.ps = self.ticker.info['priceToSalesTrailing12Months']
        if self.ps == None:
            self.ps = 'inte tillgängligt'

    def hitta_beta(self):
        self.beta = self.ticker.info['beta']
        if self.beta == None:
            self.beta = 'inte tillgängligt'

    def hitta_soliditet(self):
        self.soliditet = self.ticker.info['debtToEquity']
        if self.soliditet == None:
            self.soliditet = 'inte tillgängligt'

    def hitta_skillnad(self, period):
        self.skillnad = self.ticker.history(period)
        hög = max(list(self.skillnad['High']))
        låg = min(list(self.skillnad['Low']))
        return ((hög-låg)/hög) * 100

    def hitta_högsta(self, period):
        self.högsta = self.ticker.history(period)
        hög = max(list(self.skillnad['High']))
        return hög

    def hitta_lägsta(self, period):
        self.lägsta = self.ticker.history(period)
        låg = min(list(self.skillnad['Low']))
        return låg

def rätt_tecken(fråga, lägsta, högsta):

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

def rätt_namn(fråga):

    Korrekt_inmatning = False
    
    while not Korrekt_inmatning:
        ticker = input(fråga)
        Korrekt_inmatning = True
        try:
            aktie = Aktie(ticker)
            return aktie
        except KeyError:
            Korrekt_inmatning = False
            print('\nVänligen ange en korrekt aktieticker')

def rätt_period(period):

    Korrekt_inmatning = False
    
    while not Korrekt_inmatning:
        svar = input(period)
        Korrekt_inmatning = True
        lista = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
        if svar in lista:
            return svar
        else:
            print('\nVänligen en korrekt period')
            Korrekt_inmatning = False

def main(): 

    fortsätt = True
    
    aktie = rätt_namn('Vänligen välj en aktie från NASDAQ börsen: ')

    aktierna = []
    aktierna.append(aktie)

    while fortsätt:
        val = rätt_tecken(('\n1 - Fundamental analys\n2 - Teknisk analys\n3 - Rangordning på beta\n4 - Välj en till aktie\n5 - Avsluta\n'), 1, 5)

        if val == 1:
            print('\nFundamental analys för',aktie.namn,'\nföretagets soliditet är',aktie.soliditet, '\nföretagets p/e-tal är',aktie.pe,'\nföretagets p/s-tal är', aktie.ps)

        elif val == 2:
            period = rätt_period('\nange ett tidsintervall: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max\nför att ta reda den procentuella skillnaden mellan det högsta och lägsta priset samt det lägsta/högsta priset under vald period : ')
    
            print('\nTeknisk analys för',aktie.namn,'\nkursutveckling',aktie.hitta_skillnad(period),'%','\nbetavärde',aktie.beta,'\nlägsta kurs',aktie.hitta_lägsta(period),'\nhögsta kurs', aktie.hitta_högsta(period))

        elif val == 3:
            print('Rangordning av aktier med avseende på dess betavärde')
            sorterad_lista = sorted(aktierna, key = attrgetter('beta'),reverse = True)
            for a in sorterad_lista:
                print(a)

        elif val == 4:
            aktie_tmp = rätt_namn('välj en till aktie:')
            hittad_aktie = False
            for a in aktierna:
                if aktie.namn == aktie_tmp.namn:
                    aktie = a  
                    hittad_aktie = True
                    break
            if not hittad_aktie:
                aktie = aktie_tmp
                aktierna.append(aktie)

        elif val == 5:
            fortsätt = False

main()

