# Escriba en pantalla el tipo de dato que retorna la expresión 4 < 2
print(4<2)

# Almacene en una variable el nombre de una persona y al final muestre en la consola el me nsaje: “Bienvenido [nombrePersona]”
nombrePersona = " Pythonators "
print("Bienvenido" + nombrePersona)

# Evalúe si un número es par o impar y muestre en la consola el mensaje.
number = 2
if(number % 2 == 0):
    print('par')
else:
    print("impar")

#Almacene dos números y evalúe si el primero es mayor que el segundo. El resultado debe verse en la consola.

cajita1 = 4 
cajita2 = 3
print(cajita1 > cajita2)

# Convierta dólares a pesos.

dolar = 10
peso = 58
print(dolar * peso)

# Convierta grados celsius a Fahrenheit

celsius = 32
Fahrenheit = (celsius * 9/5) + 32
print(str(Fahrenheit) + "°F" )

# Almacene cuatro notas 90,95,77, 92 y las promedie. Al final debe decir su calificación en letras A, B,C,D, E ó F. 

promedio = (90+95+77+92)/4 
if(promedio >= 90 ):
   print("A")
elif(promedio < 90 and promedio > 85):
    print("B")   
elif(promedio < 80 and promedio > 75):
    print("C")
elif(promedio < 70 and promedio > 65):
        print("D")
elif(promedio < 60 and promedio > 55):
        print("E")
elif(promedio < 50 and promedio > 45):
       print("F")

# Que almacene monto, cantidad de cuotas, y porcentaje de interés anual de un préstamo y calcule la cuota mensual. (Amortizar mediante el sistema francés)



        