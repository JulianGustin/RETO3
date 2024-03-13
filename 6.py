#Punt_6_Taller1

Letra: str
vocales = ("a", "e")
print("Hola, se que quieres aprender el abecedario y sus \"elementos\"")
print("por lo que te ayudaré diciendote si es una vocal o consonante cuando insertes una letra")

Letra = (input("Ahora por favor dime una letra del abecedario español"))

if Letra.isdigit() == True:
    print("Eso es un número, genio")
else:
    if Letra == "a":
        print("Esa es una vocal")
    elif Letra == "e":
        print("Esa es una vocal")
    elif Letra == "i":
        print("Esa es una vocal")
    elif Letra == "o":
        print("Esa es una vocal")
    elif Letra == "u":
        print("Esa es una vocal")
    elif Letra == "A":
        print("Esa es una vocal")
    elif Letra == "E":
        print("Esa es una vocal")
    elif Letra == "I":
        print("Esa es una vocal")
    elif Letra == "O":
        print("Esa es una vocal")
    elif Letra == "U":
        print("Esa es una vocal")
    elif len(Letra) > 1:
        print("Eso nisiquiera es una letra, sabelotodo")
    elif Letra == " ":
        print("Eso es un espacio")
    else:
        print("Esa es una consonante")