#Condiciones multiples

sensorNivelAgua=int(input("Digite el nivel de agua de la represa: "))

if sensorNivelAgua>0 and sensorNivelAgua <=150:
    print("Muy poca agua, las puertas estan cerradas")
elif sensorNivelAgua >150 and sensorNivelAgua <=400:
    print("Operando normalmente")
elif sensorNivelAgua >400 and sensorNivelAgua<=420:
    print("Precaucion, mucho cuidado, revise el nivel de agua")
elif sensorNivelAgua >420:
    print("Este parche se calento, corre perra correeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee.................")    
else:
    print("Revise el sensor, medida no valido")          