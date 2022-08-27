guardian=100

#ciclo while
print("***MENU***")
print("1.saludar")
print("2.despedir")
print("0.salir")
while(guardian!=0):
    guardian=int(input("Digita una opcion")) 
    
    if(guardian==1):
        print("hola")
    elif(guardian==2):
        print("chao")
    elif(guardian==0):
        break
    else:
        print("Digite una opcion valida")  
else:
    print("termine")
