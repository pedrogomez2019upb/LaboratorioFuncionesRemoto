#Primero declaramos la función a utilizar
def is_prime(number):
    #Se crea un for para números primos y su contador que empice desde cero
    counter = 0
    for i in range(1,number+1):
        if (number% i)==0:
            counter = counter + 1
    if counter==2:
        print ("The number {} is prime. Thanks for using this program.".format(number))
    else:
        print ("The number {} is not prime. Thanks for using this program.".format(number))

#Se llama la función para que la ejecute
is_prime(3)
#Desarrollado por Pedro Gómez / ID:000396221