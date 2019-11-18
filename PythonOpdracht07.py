import sqlite3

conn = sqlite3.connect("leerlingen.sqlite3")
c = conn.cursor()

c.execute(
    '''CREATE TABLE Leerlingen (Id INTEGER PRIMARY KEY, Voornaam, Achternaam)''')
c.execute("INSERT INTO Leerlingen VALUES ('Brent', 'Verlinden')")
c.execute("INSERT INTO Leerlingen VALUES ('Arne', 'Meylemans')")
c.execute("INSERT INTO Leerlingen VALUES ('Thijs', 'Verbelen')")
c.execute("INSERT INTO Leerlingen VALUES ('Senne', 'Weygers')")

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
   if keuze = "N":
        Voornaam = input("Geef de voornaam van de leerling:")
        Achternaam = input("Geef de achternaam van de leerling:")
        c.execute("INSERT INTO Leerlingen VALUES (?,?)", Voornaam, Achternaam)
    elif keuze = "V":
        c.execute(
            '''SELECT Id,Voornaam,Achternaam FROM Leerlingen ORDER BY Voornaam''')
    elif keuze = "A":
