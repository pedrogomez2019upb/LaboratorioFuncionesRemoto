#Se declara la definición
def a_power_b(base,exp):
    #Si el exponente es 1 entonces solamente retorne la base
    if(exp==1):
        return(base)
        #Si la base es diferente a uno entonces retornar un valor que multiplica la base
        #con la función y con esto hacer una recursion de la base con el exponente menos 1
    if(exp!=1):
        return(base*a_power_b(base,exp-1))
        
print("Result:",a_power_b(2,6))

#Desarrollado por Pedro Gómez / ID:000396221