import sqlite3, os
import msvcrt

file_name = 'leerlingen.sqlite3' 
if(os.path.exists(f"{file_name}.db")): 
    os.remove(f"{file_name}.db") 

conn = sqlite3.connect(f"{file_name}.db")
c = conn.cursor()

c.execute(
    '''CREATE TABLE Leerlingen (Id INTEGER PRIMARY KEY, Voornaam, Achternaam)''')
c.execute("INSERT INTO Leerlingen VALUES ('Brent', 'Verlinden')")
c.execute("INSERT INTO Leerlingen VALUES ('Arne', 'Meylemans')")
c.execute("INSERT INTO Leerlingen VALUES ('Thijs', 'Verbelen')")
c.execute("INSERT INTO Leerlingen VALUES ('Senne', 'Weygers')")

print("Kies 1 van volgende opties:")
print("N: Voeg een nieuwe leerling toe.")
print("V: Sorteer de leerlingen op hun voornaam.")
print("A: Sorteer de leerlingen op hun achternaam.")
print("X: verwijder een leerling op basis van het id.")
print("D: Verwijder een leerling op basis van de voornaam.")
print("S: Stop het programma.")

keuze = input("\nKies een optie uit het bovenstaande menu: ")
print("")

while keuze != "S":
    if keuze == "N":
      Voornaam = input("Geef de voornaam van de leerling: ")
      Achternaam = input("Geef de achternaam van de leerling: ")
      c.execute("INSERT INTO Leerlingen(Voornaam, Achternaam) VALUES (?,?)", (Voornaam, Achternaam))
    elif keuze == "V":
      c.execute(
            '''SELECT Id,Voornaam,Achternaam FROM leerlingen ORDER BY Voornaam''')
    elif keuze == "A":
      c.exectute('''SELECT Id, Voornaam, Achternaam FROM leerlingen ORDER BY Achternaam''')
    elif keuze == "X":
      Verwijder_via_id = input("Geef het id in van de leerling die u wilt verwijderen: ")
      c.execute("DELETE FROM Leerlingen(Id) WHERE Id=?", (Verwijder_via_id))
    else:
      Verwijder_via_naam = input("Geef de naam in van de leerling die u wiltverwijderen: ")
      c.execute("DELETE FROM Leerlingen(Voornaam) WHERE Voornaam=?", (Verwijder_via_naam))
      .fetchall()
      if(len(lln)>1):
        print("Welke leerlingen?") 
        for i in range(len(lln)): 
          print(f'{i+1}: {lln[i][1]} {lln[i][2]}') 
        id = (lln[int(input("Nummer: "))-1][0],) 
        c.execute('DELETE FROM Leerlingen WHERE Id=?', id) 
        else: 
          c.execute('DELETE FROM Leerlingen WHERE Voornaam=?', ingevenVoornaam)

    keuze = input("\nKies een optie uit het bovenstaande menu, je hoeft geen enter te gebruiken om te bevestigen: ")
    keuze = msvcrt.getch().decode("utf-8").upper() 
    print("") 

    conn.commit()