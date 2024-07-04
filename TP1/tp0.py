import random

def adivinar(num_iter):

    numero = random.randint(1,10)
    #print(numero)
    for i in range(1,num_iter+1):
        data_in = input("Adivine el número que va a salir (de 0 a 10): ")
        
        if(numero == int(data_in)):
            print("¡Acertaste en {} intentos!".format(i))
            break
        else:
            if(i==num_iter):
                print("\nNo lograste adivinar en {} intentos\n" .format(i))
            else:
                print("No tuviste suerte. Intenta de nuevo\n")



################## MAIN #########################
iteraciones = input("BIENVENIDO AL PROGRAMA PARA ADIVINAR.\nIngrese la cantidad de intentos: ")
print("\n")

adivinar(int(iteraciones))
