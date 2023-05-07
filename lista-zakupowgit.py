print("Lista Zakupów")
sklep={"Piekarnia":["Chleb","Pączek","Bułki"]}
sklep1={"Warzywniak":["Marchew","Seler","Rukola"]}
for rzeczy in sklep:
    print("Wchodzę do piekarni i kupuje",(sklep["Piekarnia"]))
for rzeczy in sklep1:
    print("Wchodzę do warzywniaka i kupuje",(sklep1["Warzywniak"]))
print("W sumie kupuje",(len(sklep["Piekarnia"]))+(len(sklep1["Warzywniak"])))