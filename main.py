import writes, os, ship

writes.Menu()
writes.Behuzas()
valasz = input("A választás száma: ")
if valasz == "1":
        writes.Behuzas()
        name = input("Add meg a neved!: ")
        ship.Game(name)
elif valasz == "2":
        writes.Stats()
elif valasz == "3":
        os.system("clear")
        exit()
else:
        os.system("python3 main.py")
