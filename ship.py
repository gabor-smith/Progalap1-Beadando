import os, time, termios, tty, os, sys, random, writes, fcntl

def CharIn():
        """
                Linux terminál bemenet vizsgálat

                Visszaad egy kh nevű változót ami az aktuálisan leütött karakter (str)-ben,
        """
        kh = ""         # Terminálba leütött billenytű
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

        try:        
            while 1:            
                try:
                        kh = sys.stdin.read(1)
                        break
                except IOError: pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
        return kh

def Makeline():
        """
                Sor készítése és akadály generálása random.

                Visszaad egy (int)-et mint lehetséges hibát (akadály helyét)
                és
                Visszaad egy (str)-t ami a  pálya texturáját takarja
        """
        fail = random.randint(5,44)
        liner = ""      # Sor frissités defaul-ra
        for j in range(50):
                if j < 5:
                        liner += "\u001b[32m\u001b[42mF\u001b[0m"
                elif j == fail:
                        liner += "\u001b[40m\u001b[30mR\u001b[0m"
                elif j > 44:
                        liner += "\u001b[32m\u001b[42mF\u001b[0m"
                else:
                        liner += "\u001b[34m\u001b[44mV\u001b[0m"
        return int(fail), str(liner)

def KeyInput(pos:int) -> int:
        """
                A felhasználó által bevitt utasítást értelmezi és végrehajtja a hozzá tartozó műveletet.

                pos ("Pozició") (int) értékét kapja meg

                Visszaadja a műveletek elvégzését követően a pos váltózó értékét (int)-ben.
        """
        kar = ""        # Megkapott karakter a billentyűzetről
        kar = CharIn()
        if kar == "a":
                pos -= 1
        elif kar == "d":
                pos += 1
        elif kar == "s":
                pos = pos
        elif kar == "q":
                exit()
        return pos

def Test(pos:int, lines:dict, pont:int, name:str) -> int:
        """
                Ez figyeli, hogy a játékos belmegy-e az akadályba illetve, hogy kimegy-e a játékterületről.

                pos ("Pozició") (int) értékét kapja meg
                és
                pont ("Pontszám") (int) értéket kapja meg
                és
                lines ("Sorok") (dict) értékét kapja meg
                ellenőrzés céljából

                Visszaadja a műveletek elvégzését követően a pont változó értékét (int)-ben.
        """
        if pos < 5 or pos > 44 or pos == lines["0f"] or pos == lines["1f"]:
                writes.ShipEnd(pont, name)
        else:
                 pont += 1
        return pont

def Makeline2(pos:int, lines:dict, line):
        """
                Létrehozza a sort amelyben a játékos mozog.

                pos (int), lines (dict), line (str) váltózók felhasználásával.
        """
        for i in range(50):
                if i < 5:
                        line += "\u001b[32m\u001b[42mF\u001b[0m"
                elif i == pos:
                        line += "\u001b[41m\u001b[31mR\u001b[0m"
                elif i == lines["0f"]:
                        line += "\u001b[30m\u001b[40mO\u001b[0m"
                elif i > 44:
                        line += "\u001b[32m\u001b[42mF\u001b[0m"
                else:
                        line += "\u001b[34m\u001b[44mV\u001b[0m"
        print(line)

def ClearRows(liner:str) -> str:
        """
                Legenerálja az akadálymentes sort

                liner (str) felhasználásával.

                Visszaadja a liner módosított változatát.
        """
        for i in range(50):
                if i < 5:
                        liner += "\u001b[32m\u001b[42mF\u001b[0m"
                elif i > 44:
                        liner += "\u001b[32m\u001b[42mF\u001b[0m"
                else:
                        liner += "\u001b[34m\u001b[44mV\u001b[0m"
        return str(liner)

def Game(name:str):
        """
                A játékprogram MAIN része

                name (str) változót kapja meg.
        """
        lines = {"0":"", "0f":"", "1":"", "1f":"", "2":"", "2f":"", "3":"", "3f":"", "4":"", "4f":"", "5":"", "5f":"", "6":"", "6f":"", "7":"", "7f":"", "8":"", "8f":"", "9":"", "9f":""}
        is_name = False
        pont = 0
        pos = 24
        first = True
        while True:
                try:
                        time.sleep(0.1)
                        line = ""
                        os.system("clear")
                        writes.Behuzas()
                        print("\n\nJátékos: " + name + "   Pont:" + str(pont) + "\n")
                        int(pont)
                        writes.Behuzas()
                        Makeline2(pos, lines, line)
                        if first == True:
                                for i in range(10):
                                        liner = ""
                                        liner = ClearRows(liner)
                                        writes.Behuzas()
                                        print(liner)
                                        lines[str(i)] = liner
                                        int(i)
                                first = False
                        else:
                                for i in range(9):
                                        lines[str(i)] = lines[str(i+1)]
                                        lines[str(i) + "f"] = lines[str(i+1) + "f"]
                                lines[str(9) + "f"], lines[str(9)] = Makeline()
                                for i in range(10):
                                        writes.Behuzas()
                                        print(lines[str(i)])
                        pos = KeyInput(pos)
                        pont = Test(pos, lines, pont, name)
                except KeyboardInterrupt:
                        break
