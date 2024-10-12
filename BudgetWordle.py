import random

wörter = ["auto", "willi", "rudi", "rainer", "schanze", "rita", "emalla"]

def spiel():
    wort = random.choice(wörter)
    versuche = 10
    erraten = ["_"] * len(wort)

    while versuche > 0:
        if "_" not in erraten:
            print("Sehr gut! Du hast das Wort " + wort + " erraten!")
            break

        print("Aktuelles Wort: " + " ".join(erraten))
        print("Aktuelle Versuche: " + str(versuche))
        guess = input("Rate einen Buchstaben: ").lower()

        if guess in wort:
            for i in range(len(erraten)):
                if guess == wort[i]:
                    erraten[i] = guess
            print("Gute Guess!")
        else:
            print("Das ist leider nicht enthalten :(")
            versuche = versuche - 1



spielen = input("Willst du ein Wort raten?(Y|N): ")

while spielen == "Y":
    spiel()
    spielen = input("Willst du ein Wort raten?(Y|N): ")
