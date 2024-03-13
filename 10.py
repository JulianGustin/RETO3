# Punt_10_Taller1

Dist = float
VelUsb = float
VelVeh = float
VelSon  = float
VelLuz = float
Time = float

print("Hola, ¿quieres saber que tanto le tomaría a la luz")
print("al sonido en el aire,")
print("al vehículo comercial más veloz")
print("y a Usain Bolt recorrer cierta distancia?")
Dist = float( input( "Entonces digita tu distancia elegida en km") )

VelLuz = 300000
VelSon = 1235.52
VelVeh = 435
VelUsb = 44.72

Time = Dist / VelLuz
print("\n A la luz le tomaría:", Time, "horas para recorrer esa distancia.")
Time = Dist / VelSon
print("\n Al sonido en el aire le tomaría:", Time, "horas para recorrer esa distancia.")
Time = Dist / VelVeh
print("\n Al vehículo comercial más rápido le tomaría:", Time, "horas para recorrer esa distancia.")
Time = Dist / VelUsb
print("\n A Usain Bolt le tomaría:", Time, "horas para recorrer esa distancia.")

print("\n Eso es todo, gracias por usar este programa")