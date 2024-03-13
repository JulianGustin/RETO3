frecuencia = int (input("Onda (Hz): ")) * 10**10
if frecuencia < 3e9:
    print ("Onda de radio")
elif 3e9 <= frecuencia < 3e12:
    print("Microondas")
elif 3e12 <= frecuencia < 4.3e14:
    print ("Infrarrojo")
elif 4.3e14 <= frecuencia < 7.5e14:
    print ("Visible")
elif 7.5e14 <= frecuencia < 3e17:
    print ("Ultravioleta")
elif 3e17 <= frecuencia < 3e19:
    print ("Rayos X")
else:
    print ("Rayos gamma")
