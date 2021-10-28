import os

def Behuzas():
        print("                  ", end="")

def Menu():
        os.system("clear")
        print("\n\n")
        Behuzas()
        print("\u001b[42m                               \u001b[0m")
        Behuzas()
        print("\u001b[42m  \u001b[0m                           \u001b[42m  \u001b[0m")
        Behuzas()
        print("\u001b[42m  \u001b[0m       \u001b[37m1. Jatek            \u001b[42m  \u001b[0m")
        Behuzas()
        print("\u001b[42m  \u001b[0m       \u001b[37m2. Pontok           \u001b[42m  \u001b[0m")
        Behuzas()
        print("\u001b[42m  \u001b[0m       \u001b[37m3. Kilépés          \u001b[42m  \u001b[0m")
        Behuzas()
        print("\u001b[42m  \u001b[0m                           \u001b[42m  \u001b[0m")
        Behuzas()
        print("\u001b[42m                               \u001b[0m")
        print("")

def Stats():
        os.system("clear")
        print("\n\n")
        Behuzas()
        print("\u001b[42m                               \u001b[0m")
        Behuzas()
        print("\u001b[42m  \u001b[0m\u001b[37mNév         \u001b[42m  \u001b[0m\u001b[37mPont         \u001b[42m  \u001b[0m")
        Behuzas()
        print("\u001b[42m                               \u001b[0m")
        file = open("score.txt", "r")
        for line in file:
                line = line.split(':')
                Behuzas()
                print("\u001b[42m  \u001b[0m\u001b[31m " + line[0], end="")
                for i in range(11 - len(str(line[0]))):
                        print("\u001b[0m \u001b[0m", end="")
                print("\u001b[42m  \u001b[0m\u001b[31m " + line[1][:-1], end="")
                for i in range(13 - len(str(line[1]))):
                        print("\u001b[0m \u001b[0m", end="")
                print("\u001b[42m  \u001b[0m")
        file.close()
        Behuzas()
        print("\u001b[42m                               \u001b[0m")
        print("")
        Behuzas()
        input("Tovább...")
        os.system("python3 main.py")
        exit()

def ShipEnd(pont:int, name:str):
        if int(pont) < 10:
                kiirott = "000" + str(pont)
        elif int(pont) < 100:
                kiirott = "00" + str(pont)
        elif int(pont) < 1000:
                kiirott = "0" + str(pont)
        else:
                kiirott = str(pont)
        os.system("clear")
        print("\n\n")
        Behuzas()
        print("\u001b[42m                                                    \u001b[0m")
        Behuzas()
        print("\u001b[42m  \u001b[0m                                                \u001b[42m  \u001b[0m")
        Behuzas()
        print("\u001b[42m  \u001b[0m Gratulálok! " + kiirott + " pontot szereztél!             \u001b[42m  \u001b[0m")
        Behuzas()
        print("\u001b[42m  \u001b[0m Játék vége.                                    \u001b[42m  \u001b[0m")
        Behuzas()
        print("\u001b[42m  \u001b[0m                                                \u001b[42m  \u001b[0m")
        Behuzas()
        print("\u001b[42m                                                    \u001b[0m")
        Behuzas()
        input("Tovább...")
        os.system("python3 main.py")
