# Reto #3 
## Lista de contenidos
1. [Hallar números primos](#hallar-números-primos)
      - [Pseudocodigo](#pseudocódigo-primos)
      - [Flowchart](#flowchart)

# Hallar números primos
## Pseudocódigo primos 
```pseudocode
[variables]
n: natural
i: natural
x: natural

Inicio
n = entrada (“Ingresar número natural”)

  Para Cada i desde 2 hasta n Hacer 
  	x < i 
  	Para Cada x Hacer
  		Si modulo (i,x) = 0 Entonces 
  			Imprima (i “No es primo”)
  		Sino si x = (iˆ0.5)-1 
  			Imprima (i “Es primo”) 
  		Sino 
  			x = x + 1 
  		Fin si
  	Fin Para Cada
  Fin Para Cada 
Fin 

```
## Flowchart
```mermaid
flowchart TD;
A[Inicio]-->B[Entrada]-->C
C[Número n]-->D[Para cada i desde n hasta n]-->E 
E[Para cada x < i]-->F
F{¿Modulo i/x = 0?} -- Si --> G[i no es primo] -->K[Fin]
F -- No --> H{"¿x=(i^0.1) - 1?"} -- Si --> I[Es primo] -->K
H -- No --> J{x=x+1} --> F
```
