import os
import platform

##CLI leegmaken
def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

uber_service = {
    "Uber Black": 2.00,
    "Uber Van": 3.50,
    "Uber X": 1.50
}

user = {
 "preference": "Uber X",
 "history": []
}

def hoofdmenu():
    """Deze functie vraagt de gebruiker een keuze te maken in het menu"""
    print(f'Je hebt momenteel \"{set_service}\" als voorkeur ingesteld \n')
    keuze = int(input("Welkom terug in de Uber-app! Wat kunnen we vandaag voor je doen?"
                      "\n1: Een nieuwe rit boeken "
                      "\n2: Mijn service voorkeur aanpassen "
                      "\n3: Mijn ritten geschiedenis inzien "
                      "\n4: De applicatie afsluiten\n"))
    return keuze

while True:
    clear_screen()
    set_service = user["preference"]
    menu_choice = hoofdmenu()

    while menu_choice == 1:
        clear_screen()
        def get_service():
            """Vraagt de gebruiker om zijn/haar voorkeur te gebruiken of een geldige Uber-service te kiezen en geeft die terug."""
            user_preference = int(input(f"Wil je voor deze rit \"{user["preference"]}\" gebruiken?: \n1:Ja \n2:Nee "))
            while user_preference ==1:
                return user["preference"]
            if user_preference ==2:
                print('Onze services zijn:')
            for service in uber_service:
                print(f"- {service}")
            user_choice = input("Welke service wil je gebruiken? ")
            user_choice = user_choice.title()
            while user_choice not in uber_service:
                print(f"{user_choice} is een ongeldige keuze.")
                user_choice = input("Welke service wil je gebruiken? ")
            return user_choice



        def travel_distance():
            """Vraagt hoeveel kilometer de gebruiker wil reizen en geeft dat terug als float."""
            distance = float(input("Hoeveel KM wil je reizen? "))
            return distance

        def total_cost(afstand, prijs_per_km):
            """Bereken de totale ritprijs op basis van afstand en prijs per kilometer."""
            return afstand * prijs_per_km


        # variabelen
        ride = get_service()
        price_per_km = uber_service[ride]
        clear_screen()
        afstand = travel_distance()
        totaal = total_cost(afstand, price_per_km)
        user["history"].append((ride, afstand, totaal))
        clear_screen()
        # Output
        print(f'U heeft gekozen voor {ride}. De kosten voor uw rit van {afstand} kilometer(s) zijn €{totaal:.2f}')
        herhalen = int(input("Wil je nog een rit boeken?: \n1: Ja \n2: Nee "))
        if herhalen ==1:
            print("U kunt nog een rit boeken")
        elif herhalen ==2:
            break

    if menu_choice == 2:
        clear_screen()
        def fav_ride():
            """Vraagt de gebruiker om zijn/haar voorkeur voor de service."""
            print(f'Uw huidige favoriete service is \"{set_service}\"')
            print('Onze services zijn:')
            for service in uber_service:
                print(f"- {service}")
            favorite = input("Welke service wil je instellen als standaard? ")
            favorite = favorite.title()
            while favorite not in uber_service:
                print(f"{favorite} is een ongeldige keuze.")
                favorite = input("Welke service wil je instellen als standaard? ")
            return favorite
        user["preference"] = fav_ride()

    elif menu_choice == 3:
        clear_screen()
        nummer = 0
        if not user["history"]:
            print("Je hebt nog geen ritten gemaakt.")
        for service, aantal_km, prijs in user["history"]:
            nummer +=1
            print(f'Rit: {nummer} - €{prijs:.2f} - Je hebt {aantal_km} kilometer gereisd met de dienst "{service}".')

    elif menu_choice == 4:
        clear_screen()
        print("Afsluiten voltooid. De applicatie is succesvol afgesloten.")
        break
