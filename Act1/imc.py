# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-03-14
# RLAB-23-02-09-0044-2
#

# Liberias
from sys import argv

# Uso del programa
if len(argv) <2:
    print("Uso del programa: \n")
    print("python imc.py peso altura \n")
    print("*** El peso debe ser expresado en Kg ***")
    print("*** La altura debe ser expresada en cm ***\n")
    print("Ejemplo : \n")
    print("Para una persona que pesa 81 Kg y mide 181 cm usamos : \n") 
    print("python imc.py 81 181\n")   
    exit()

# Variables con validación
if float(argv[1]) <1 :
    print("El peso no puede ser 0")
    exit()
else:
    peso = float(argv[1])

if float(argv[2]) <1 :
    print("La altura no puede ser 0")
    exit()
else:
    altura = float(argv[2])/100 # convierte cm --> mt

imc = float(peso/(altura**2))

# Condicionales
if imc < 18.5 and imc >= 16 :
    print(f"Su IMC es {round(imc,2)}")
    print("La Clasificación OMS es Bajo Peso")
elif imc >= 18.5 and imc < 25 :
    print(f"Su IMC es {round(imc,2)}")
    print("La Clasificación OMS es Adecuado")
elif imc >= 25 and imc < 30 :
    print(f"Su IMC es {round(imc,2)}")
    print("La Clasificación OMS es Sobrepeso")
elif imc >= 30 and imc < 35 :
    print(f"Su IMC es {round(imc,2)}")
    print("La Clasificación OMS es Obesidad Grado I")
elif imc >= 35 and imc < 40 :
    print(f"Su IMC es {round(imc,2)}")
    print("La Clasificación OMS es Obesidad Grado II")
elif imc >= 40 and imc < 50 :
    print(f"Su IMC es {round(imc,2)}")
    print("La Clasificación OMS es Obesidad Grado III")
else :
    print("Valores fuera de rango, favor ingresar datos reales.")