
"""
main.py: první projekt do Engeto Online Python Akademie

author: Rene Raszyk
email: 2004reno2004@gmail.com
"""


TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

uzivatele = ("bob", "ann", "mike", "liz")
heslo = ("123", "pass123", "password123", "pass123")

uzivatelske_jmeno = input("\nusername: ")
uzivatelske_heslo = input("password: ")

for index, name in enumerate(uzivatele):
    if name == uzivatelske_jmeno and uzivatelske_heslo == heslo[index]:
        print("----------------------------------------")
        print("Welcome to the app,", uzivatelske_jmeno)
        print("We have 3 texts to be analyzed.")
        print("----------------------------------------")
        break
else:
    print("unregistered user, terminating the program..\n")
    exit()

druh_text = input("Enter a number btw. 1 and 3 to select: ")
print("----------------------------------------")

if (not druh_text.isdigit()) or (not 1 <= int(druh_text) <= 3):
    print("Wrong number, terminating the program..")
    exit()

druh_text = int(druh_text) - 1

pocet_slov = 0
pocet_vsech_slov = 0
pocet_velkych_slov = 0
pocet_malych_slov = 0
delka = 0
pocet_vseho_velkyho = 0
pocet_cisel = 0
suma_cisel = 0
cetnosti = {}

slova = TEXTS[int(druh_text)].split(" ")

for pocet in slova:

    pocet = pocet.strip(".?,!-\n")
    delka = len(pocet)

    if delka == 0:
        continue
    else:
        pocet_vsech_slov += 1
        if pocet.isupper():     # opravit 1 -
            pocet_vseho_velkyho += 1
            
        if pocet.istitle():
            pocet_velkych_slov += 1
            
        if pocet.islower():
            pocet_malych_slov += 1
            
        if pocet.isnumeric():
            pocet_cisel += 1
            suma_cisel = suma_cisel + int(pocet)    # opravit - 1
        
        if delka in cetnosti:
            cetnosti[delka] = cetnosti[delka] + 1
        else:
            cetnosti[delka] = 1
        

print("There are",pocet_vsech_slov,"words in the selected text.")
print("There are",pocet_velkych_slov,"titlecase words.")
print("There are",pocet_vseho_velkyho,"uppercase words.")
print("There are",pocet_malych_slov,"lowercase words.")
print("There are",pocet_cisel,"numeric strings.")
print("The sum of all the numbers",suma_cisel)
print("----------------------------------------")
print("LEN|  OCCURENCES  |NR.")
print("----------------------------------------")

mezera = " "
vypis_mezer = " "
hvezda = "*"
vypis_hvezd = str()

serazeni = sorted(cetnosti)

for pocet in serazeni:
    cislo_cetnosti = cetnosti[pocet]

    for _ in range(cislo_cetnosti):
        vypis_hvezd = vypis_hvezd + hvezda

    if pocet < 10:
        vypis_mezer = vypis_mezer + mezera
    
    print(f"{vypis_mezer}{pocet}| {vypis_hvezd:<20} |{cetnosti[pocet]}")
    
    vypis_hvezd = ""
    vypis_mezer = " "
    
print("\n")