import sqlite3

conn = sqlite3.connect("leerlingen.sqlite3")
c = conn.cursor()

c.execute('''CREATE TABLE Leerlingen (Id, Voornaam, Achternaam)''')
c.execute("INSERT INTO Leerlingen VALUES ('1', 'Brent', 'Verlinden')")
c.execute("INSERT INTO Leerlingen VALUES ('2', 'Arne', 'Meylemans')")
c.execute("INSERT INTO Leerlingen VALUES ('3', 'Thijs', 'Verbelen')")
c.execute("INSERT INTO Leerlingen VALUES ('4', 'Senne', 'Weygers')")

conn.commit()

print("Kies 1 van volgende opties:")
print("N: Voeg een nieuwe leerling toe.")
print("V: Sorteer de leerlingen op hun voornaam.")
print("A: Sorteer de leerlingen op hun achternaam.")
print("X: verwijder een leerling op basis van het id.")
print("D: Verwijder een leerling op basis van de voornaam.")
print("S: Stop het programma.")

keuze = input("Kies een optie uit het bovenstaande menu: ")

while keuze != "S"
