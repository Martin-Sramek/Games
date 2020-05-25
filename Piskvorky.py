def zadani_jmen_hracu():
    """
    Hráči zadají svá jména.
    Těmito jmény pak budou v průběhu hry oslovováni.
    """

    jmeno_1 = input("Hráči č. 1, zadej svoje jméno: ")
    jmeno_2 = input("Hráči č. 2, zadej svoje jméno: ")

    return jmeno_1, jmeno_2


def vyber_symbolu(jmena_hracu):
    """
    Hráči si vyberou symbol se kterým budou hru hrát.
    Na výběr je pouze symbol "X", nebo "O".
    První hráč si symbol vybere, druhému hráči je symbol přidělen.
    """

    while True:
        hrac_1_symbol = input(f"{jmena_hracu[0]}, s jakým symbolem chceš hrát? Zadej X nebo O: ")
        if hrac_1_symbol == "X" or hrac_1_symbol == "O":
            break

    if hrac_1_symbol == "X":
        hrac_2_symbol = "O"
    else:
        hrac_2_symbol = "X"

    return hrac_1_symbol, hrac_2_symbol


def mrizka(seznam_symbolu):
    """
    Zobrazuje hrací mřížku se symboly jednotlivých hráčů.
    Symboly jsou v mřížce rozmístěny na základě svého indexu v seznamu - proměnná seznam_symbolu.
    """
    print(f"""
        -------------
        | {seznam_symbolu[6]} | {seznam_symbolu[7]} | {seznam_symbolu[8]} |
        -------------
        | {seznam_symbolu[3]} | {seznam_symbolu[4]} | {seznam_symbolu[5]} |
        -------------
        | {seznam_symbolu[0]} | {seznam_symbolu[1]} | {seznam_symbolu[2]} |
        -------------
        """)


def vlozeni_symbolu_do_mrizky(seznam_symbolu, jmena_hracu, symboly_hracu, hrac_1_hraje=False, hrac_2_hraje=False):
    """
    Osloví hráče, aby zadal symbol a vrátí číslo indexu, kam symbol umístit do proměnné seznam_symbolu.
    """
    
    if hrac_1_hraje:
        while True:
            hrac_1_pozice = input(f"Hraje {jmena_hracu[0]} | Zadej číslo neobsazené pozice v mřížce (1-9), kam chceš umístit svůj symbol {symboly_hracu[0]}: ")
            if hrac_1_pozice.isdigit() and int(hrac_1_pozice) in list(range(1, 10)) and seznam_symbolu[int(hrac_1_pozice) - 1] == " ":
                return int(hrac_1_pozice) - 1
            else:
                continue

    if hrac_2_hraje:
        while True:
            hrac_2_pozice = input(f"Hraje {jmena_hracu[1]} | Zadej číslo neobsazené pozice v mřížce (1-9), kam chceš umístit svůj symbol {symboly_hracu[1]}: ")
            if hrac_2_pozice.isdigit() and int(hrac_2_pozice) in list(range(1, 10)) and seznam_symbolu[int(hrac_2_pozice) - 1] == " ":
                return int(hrac_2_pozice) - 1
            else:
                continue

        
def vyhra(seznam_symbolu, symboly_hracu, jmena_hracu):
    """
    Kontroluje, zda někdo vyhrál, nebo zda došlo k remíze.
    """
    hrac_1_vyhra = list(symboly_hracu[0] * 3)
    hrac_2_vyhra = list(symboly_hracu[1] * 3)

    if seznam_symbolu[0:3] == hrac_1_vyhra or seznam_symbolu[3:6] == hrac_1_vyhra or seznam_symbolu[6:9] == hrac_1_vyhra or \
        seznam_symbolu[::3] == hrac_1_vyhra or seznam_symbolu[1::3] == hrac_1_vyhra or seznam_symbolu[2::3] == hrac_1_vyhra or \
        seznam_symbolu[2:7:2] == hrac_1_vyhra or seznam_symbolu[::4] == hrac_1_vyhra:
        print(f"\nBlahopřeji! Vyhrává {jmena_hracu[0]}!")
        return True

    elif seznam_symbolu[0:3] == hrac_2_vyhra or seznam_symbolu[3:6] == hrac_2_vyhra or seznam_symbolu[6:9] == hrac_2_vyhra or \
        seznam_symbolu[::3] == hrac_2_vyhra or seznam_symbolu[1::3] == hrac_2_vyhra or seznam_symbolu[2::3] == hrac_2_vyhra or \
        seznam_symbolu[2:7:2] == hrac_2_vyhra or seznam_symbolu[::4] == hrac_2_vyhra:
        print(f"\nBlahopřeji! Vyhrává {jmena_hracu[1]}!")
        return True

    elif " " not in seznam_symbolu:
        print("\nRemíza!")
        return True

    else:
        return False

def main():
    print("""
Vítej ve hře TicTacToe!

Pravidla určitě znáš. Budeme hrát na desce, která má 9 políček.
Vyhrává hráč, kterému se dříve podaří umístit tři své 
symboly do svislé, vodorovné nebo diagonální souvislé řady.

Takto vypadá naše hrací deska:

            -------------
            | 7 | 8 | 9 |
            -------------
            | 4 | 5 | 6 |
            -------------
            | 1 | 2 | 3 |
            -------------

Každé políčko má svoje číslo. Abys vložil svůj symbol do příslušného políčka,
budeš muset v průběhu hry zadat číslo tohoto políčka.
Pokud tedy budeš chtít např. umístit svůj symbol doprostřed, zadáš číslo 5.

To je vše k pravidlům a pojďme hrát.
    """)

    seznam_symbolu = [" "] * 9
    jmena_hracu = zadani_jmen_hracu()
    print()
    symboly_hracu = vyber_symbolu(jmena_hracu)
    print()
    print(f"{jmena_hracu[0]} hraje s {symboly_hracu[0]}.")
    print(f"{jmena_hracu[1]} hraje s {symboly_hracu[1]}.")

    while True:
        # Kolo hráče 1
        mrizka(seznam_symbolu)
        hrac_1_pozice = vlozeni_symbolu_do_mrizky(seznam_symbolu, jmena_hracu, symboly_hracu, hrac_1_hraje=True)
        seznam_symbolu[hrac_1_pozice] = symboly_hracu[0]
        konec_hry = vyhra(seznam_symbolu, symboly_hracu, jmena_hracu)
        if konec_hry:
            mrizka(seznam_symbolu)
            break

        # Kolo hráče 2
        mrizka(seznam_symbolu)
        hrac_2_pozice = vlozeni_symbolu_do_mrizky(seznam_symbolu, jmena_hracu, symboly_hracu, hrac_2_hraje=True)
        seznam_symbolu[hrac_2_pozice] = symboly_hracu[1]
        konec_hry = vyhra(seznam_symbolu, symboly_hracu, jmena_hracu)
        if konec_hry:
            mrizka(seznam_symbolu)
            break

if __name__ == "__main__":
    main()