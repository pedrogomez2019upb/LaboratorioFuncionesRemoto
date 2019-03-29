#Se declara la definición
def a_power_b(base,exp):
    #Se añade el try
    try:
            
        #Si el exponente es 1 entonces solamente retorne la base
        if(exp==1):
            return(base)
            #Si la base es diferente a uno entonces retornar un valor que multiplica la base
            #con la función y con esto hacer una recursion de la base con el exponente menos 1
        if(exp!=1):
            return(base*a_power_b(base,exp-1))
    except:
        #Se imprime el error
        print("Sorry, the program doesnt work.")


while True:
    a=int(input("Welcome! We are going to elevate a number. To continue press any number , if not press 0: "))
    if a==0:
        print("Goodbye!")
        break
    else:
        base=int(input("Enter base: "))
        exp=int(input("Enter the exponential value: "))
        print("Result:",a_power_b(base,exp))
#Desarrollado por Pedro Gómez / ID:000396221
