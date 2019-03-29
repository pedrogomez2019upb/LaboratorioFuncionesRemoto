#Primero declaramos la función a utilizar
def is_prime():
    #Se solicita el número
    number=int(input("Hi! We are going to check if your number is prime . Please enter the number: "))
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
is_prime()
#Desarrollado por Pedro Gómez / ID:000396221