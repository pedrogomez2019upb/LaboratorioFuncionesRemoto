#Primero declaramos la función a utilizar
def is_prime(number):
    #Se crea un try para que revise errores
    try:           
        #Se crea un for para números primos y su contador que empice desde cero
        counter = 0
        for i in range(1,number+1):
            if (number% i)==0:
                counter = counter + 1
        if counter==2:
            #Se imprime 1
            print ("1")
        else:
            #Se imprime 0
            print ("0")
    except:
        #Se imprime -1 para que indique que hubo algún error
        print("-1")

#Se crea un counter para saber cuantas veces ha hecho el proceso
counter=0
#Se crea un while para que vaya haciendo el procedo varias veces 
while True:
    a=int(input("Welcome! We are going to check if your number is prime. To continue press any number , if not press  a number equal or less to 0: "))
    if a<=0:
        print("Goodbye!")
        #Se imprime el valor final del counter
        print("The number of times you've got a prime number is : {}".format(counter))
        is_prime(counter)
        break
    else:
        if a > 0:
            #Cada vez que consiga un primo se suma el contador
            counter=counter + 1
            number=int(input("Enter number: "))
            print(("The number is: {}".format(is_prime(number))))
#Desarrollado por Pedro Gómez / ID:000396221