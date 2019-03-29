#Primero declaramos la función a utilizar
def almost_perfect_number(n):
    #Creamos un contador para que cuente la suma        
    sum = 0
    for i in range(1, n):
        #Va sumando al contador para saber si el residuo es cero
        if(n % i == 0):
            sum = sum + i
    #Si la suma de los divisores es menor o igual a mismo numero menor a 3 entonces
    #el número es casi perfecto
    if (sum <= (n-3)):
        print("The number is not almost a perfect number!")
    else:
        print("The number is almost a perfect number!")
#Se llama la función para ejecutarla
almost_perfect_number(20)
#Desarrollado por Pedro Gómez / ID:000396221