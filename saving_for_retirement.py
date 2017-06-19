import numpy as np

def hodnota_uspor(mzda_start, obdobie, narast_mzdy, sadzba_start, rocne_zvysenie_sadzby, rocny_vynos):
    """
    Funkcia vracia buducu hodnotu uspor, ktore boli vytvorene pravidelnym
    investovanim casti mzdy.

    Vstupne parametre:
    ------------------
    mzda_start (int)
        Pociatocna hodnota mesacnej cistej mzdy pri investovani.

    obdobie (int)
        Pocet rokov, pocas ktorych sa budu odkladane prispevky akumulovat a zhodnocovat.

    narast_mzdy (float)
        Percentualny rocny narast cistej mesacnej mzdy. Ak mzda rocne porastie o 3 %,
        hodnota tohto parametra je 0.03.

    sadzba_start (float)
        Percentualna cast mzdy, ktora je akumulovana a investovana. Ak si zo mzdy odlozime
        rocne 10 %, hodnota tohto parametra je 0.10.

    rocne_zvysenie_sadby (float)
        Rocna zmena prispevkovej sadzby. Jej hodnota je aplikovana najskor v druhom roku
        sporenia (investovania). Vyjadruje pravidelnu zmenu prispevkovej sadzby
        v percentualnych bodoch.

    rocny_vynos (float):
        Anualizovany vynos dosiahnuty pri investovani. Je vyjadreny ako percento v desatinnom
        tvare, t.j. pri rocnom vynose 7 % je hodnota tohto parametra 0.07.

    """

    def mzdovy_profil(pociatocna_mzda, pocet_rokov, rast_mzdy):
        """Vrati pole, ktore je tvorene mesacnou mzdou pri danom raste mzdy pocas urceneho poctu rokov."""
        
        mzda = []
        for a in range(pocet_rokov):
            for b in range(12):
                mzda.append(round(pociatocna_mzda, 2))
            pociatocna_mzda = pociatocna_mzda * (1 + rast_mzdy)
##        print('Mzdovy profil:\n***********')
##        print(mzda)    
        return mzda

    #profil = mzdovy_profil(1200, 10, 0.1)

    def sadzba_prispevkov(pociatocna_sadzba, pocet_rokov, bodovy_narast=0):
        """Vrati pole, ktore je tvorene vyskou prispevkovej sadzby."""

        sadzba = []
        for a in range(pocet_rokov):
            for b in range(12):
                sadzba.append(round(pociatocna_sadzba, 2))
            pociatocna_sadzba = pociatocna_sadzba + bodovy_narast
##        print('Sadzba prispevkov:\n***********')
##        print(sadzba)
        return sadzba

    #prisp = vyska_prispevkov(0.1, 10, 0.01)

    def vyska_prispevkov(mzda, sadzba):
        """Vrati pole, ktore je tvorene absoultnou vyskou prispevkov."""

        prispevky = []
        for item in zip(mzda, sadzba):
            prispevky.append(item[0] * item[1])

##        print('Vyska prispevkov:\n***********')
##        print(prispevky)
        return prispevky

    def buduca_hodnota(prispevky, rocne_zhodnotenie):
        future_value = []
        obdobie = len(prispevky)

        for a in range(obdobie):
            future_value.append(np.fv(rocne_zhodnotenie/12, obdobie - a - 1, 0, -prispevky[a]))

        return round(sum(future_value), 2)

    #test = buduca_hodnota([100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0], 0.05)

    vyvoj_mzdy = mzdovy_profil(mzda_start, obdobie, narast_mzdy)
    vyvoj_prispevkov = sadzba_prispevkov(sadzba_start, obdobie, rocne_zvysenie_sadzby)
    hodnota_prispevkov = vyska_prispevkov(vyvoj_mzdy, vyvoj_prispevkov)
    nasporene = buduca_hodnota(hodnota_prispevkov, rocny_vynos)

    return nasporene

#hodnota_uspor(mzda_start, obdobie, narast_mzdy, sadzba_start, rocne_zvysenie_sadzby, rocny_vynos):

print(hodnota_uspor(100000/12, 15, 0.03, 0.1, 0, 0.06))
