#Primero declaramos la función a utilizar
def perfect_number(n):
    #Creamos un contador para que cuente la suma        
    sum = 0
    for i in range(1, n):
        #Va sumando al contador para saber si el residuo es cero
        if(n % i == 0):
            sum = sum + i
    #Si la suma de los divisores es igual a n entonces es un número perfecto
    if (sum == n):
        print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")
#Se llama la función para ejecutarla
perfect_number(28)
#Desarrollado por Pedro Gómez / ID:000396221