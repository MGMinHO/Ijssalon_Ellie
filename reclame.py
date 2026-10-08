from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro."
    return uitvoer

print(aanbieding_1("aardbei", 4, 0.1))


def inkomsten_totaal(inkomsten, btw = 0.09):
    totaal = sum(inkomsten)
    bedrag_btw = totaal * btw
    totaal_na_btw = totaal - bedrag_btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag_btw} euro btw betaald dient te worden."
    return uitvoer

print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345]))


def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return (laagste, hoogste)

print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))


def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst) / len(mijn_lijst)
    uitvoer = f"De gemiddelde inkomsten van deze week zijn {totaal} euro."
    return uitvoer

print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))


def meervoudig(invoer_lijst):
    uitvoer = laag_en_hoog(invoer_lijst)
    return uitvoer

print(meervoudig([10, 5, 3, 2, 1, 2, 9]))


def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(*korte_lijst)
    return uitvoer

print(combinatie([10, 5, 3, 2, 1, 2, 9]))