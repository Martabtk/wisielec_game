def wisielec(slowo, podpowiedz):
    slowo = slowo.upper()
    aktualne_slowo = ['_'] * len(slowo)
    punkty = 10
    uzycie_podpowiedzi = False
    znak_podpowiedzi = '!'

    print("Witamy w gRZe Wisielc!")
    print("Zasady gry:")
    print("1. Odgadnij ukryte słowo, podając litery.")
    print(f"2. Za każdą błędną literę tracisz 1 punkt.")
    print(f"3. możesz poprosić o podpowiedź za 2 punkty (wpisz '{znak_podpowiedzi}').")

    print("\n" + "*"*50)

    while '_' in aktualne_slowo and punkty > 0:
        for litera in aktualne_slowo:
            print(litera, end=' ')
        print()

        litera = input("Podaj swoją literę lub całe slowo: ").upper()

        if litera == znak_podpowiedzi:
            if punkty >= 2 and not uzycie_podpowiedzi:
                punkty -= 2
                uzycie_podpowiedzi = True
                print(f"Podpowiedz to: {podpowiedz}")
            elif uzycie_podpowiedzi:
                print("Podpowiedz została już wykorzystana!")
            else:
                print("Nie masz wystarczającej liczby punktów na podpowiedz!")

        elif len(litera) == 1 and litera.isalpha():
            trafiono = False
            for i in range(len(slowo)):
                if slowo[i] == litera:
                    aktualne_slowo[i] = litera
                    trafiono = True

            if not trafiono:
                punkty -= 1
                print(f"Brak litery! Punkty: {punkty}")
        elif len(litera) == len(slowo) and litera.isalpha():
            if litera == slowo:
                aktualne_slowo = list(slowo)
            else:
                punkty -= 1
                print(f"Błędne słowo! Punkty: {punkty}")
        else:
            print("Nieprawidłowe dane! Podaj literę lub całe słowo.")

    for litera in aktualne_slowo:
        print(litera, end=' ')
    print()

    if '_' not in aktualne_slowo:
        print("Gratulacje! Udało ci się odgadnąć słowo.")
    else:
        print(f"Przykro mi, tym razem przegrałeś. Prawidłowe słowo to: {slowo}")

if __name__ == "__main__":
    haslo_gracza1 = input("Graczu 1, podaj hasło do gry: ")
    podpowiedz_gracza1 = input("Graczu 1, podaj podpowiedź do hasła: ")

    print("\n" + "*"*50)

    wisielec(haslo_gracza1, podpowiedz_gracza1)
