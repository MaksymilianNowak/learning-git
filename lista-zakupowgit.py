print("Lista Zakupów")
sklep={"Piekarnia":["Chleb","Pączek","Bułki"]}
sklep1={"Warzywniak":["Marchew","Seler","Rukola"]}
for rzeczy in sklep:
    print("Wchodzę do piekarni i kupuje",(sklep["Piekarnia"]))
for rzeczy in sklep1:
    print("Wchodzę do warzywniaka i kupuje",(sklep1["Warzywniak"]))
print("W sumie kupuje",(len(sklep["Piekarnia"]))+(len(sklep1["Warzywniak"])))
print("SMS dodatkowe zakupy")
sklep2= {"Owoce":["Arbuz","Banan","Cytryna"]}
for rzeczy in sklep2:
    print("Wchodzę do Warzywniaka i kupuję",(sklep2["Owoce"]))
print("W sumie kupuje",len(sklep["Piekarnia"])+(len(sklep1["Warzywniak"]))+(len(sklep2["Owoce"])))
print("Poprosze o paragon")
for i in range(0,101):
    print(i)
