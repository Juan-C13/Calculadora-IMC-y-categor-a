#Problema1
#Juan Esteban Clavijo García - 202225709

def calcularValoresPaciente(n,p,a):
    IMC=p/(a*a)
    if IMC<18.5:
        c="Infrapeso"
    elif IMC<25:
        c="Normal"
    else:
        c="Sobrepeso"
        
    print("PACIENTE:",n)
    print("IMC:",IMC)
    print("Categoria:",c)
    print("")

calcularValoresPaciente("Alex Valencia",68.3,1.72)
calcularValoresPaciente("María Caicedo",55.1,1.62)
calcularValoresPaciente("Juan Morales",90.1,1.71)
