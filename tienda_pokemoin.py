#“Tienda Pokémon”
#Eres el encargado de desarrollar un programa para una tienda Pokémon llamada “PokéMarket”. En esta tienda, los entrenadores pueden comprar distintos objetos para sus aventuras.
#Objetivo
#Crear un programa en Python que permita simular el proceso de compra de un entrenador Pokémon, aplicando descuentos según ciertas condiciones y validando correctamente los datos ingresados.
#________________________________________
#Requerimientos
#1.	Mostrar menú de productos: 
#El programa debe mostrar el siguiente menú:
#1. Pokébola → $1000
#2. Poción → $1500
#3. Revivir → $3000
#4. Baya → $500
#5. Finalizar compra
#________________________________________
#2.	Ingreso de productos: 
#•	El usuario debe poder seleccionar productos ingresando el número correspondiente. 
#•	Validar que la opción ingresada sea correcta (entre 0 y 4). 
#•	Si la opción es inválida, mostrar un mensaje de error y volver a pedirla. 
#________________________________________
#3.	Cantidad de productos: 
#•	Por cada producto seleccionado, pedir la cantidad. 
#•	Validar que la cantidad sea un número entero positivo. 
#________________________________________
#4.	Acumulación de compra: 
#•	Calcular el total acumulado de la compra. 
#•	Llevar un contador de la cantidad total de productos comprados. 
#________________________________________
#5.	Sistema de descuentos: 
#Aplicar los siguientes descuentos:
#•	🔹 Si el total de la compra supera los $5000 → aplicar 10% de descuento. 
#•	🔹 Si compra más de 10 productos en total → aplicar un 5% adicional. 
#•	🔹 Si el entrenador compra al menos 3 “Revivir” → aplicar un 15% adicional SOLO sobre ese producto. 
# Los descuentos son acumulables.
#________________________________________
#6.	Uso de bandera (flag): 
#•	Usar una bandera para verificar si el usuario compró al menos un producto antes de finalizar. 
#•	Si no compró nada, mostrar un mensaje:
#"No has realizado ninguna compra." 
#________________________________________
#7.	Manejo de errores: 
#•	Utilizar try-except para evitar que el programa se rompa ante entradas inválidas (por ejemplo, letras en vez de números). 
#________________________________________
#8.	Salida final:
#Mostrar un resumen con: 
#•	Total bruto 
#•	Total de descuentos aplicados 
#•	Total final a pagar 
#•	Cantidad total de productos comprados 
#
#
#
#
#Requerimientos de Git (OBLIGATORIO)
#1.	Crear un repositorio público en GitHub con el nombre: 
#tienda-pokemon
#2.	En la descripción del repositorio, escribir algo como: 
#"Simulación de una tienda Pokémon desarrollada en Python. Proyecto enfocado en el uso de estructuras de control, validación de datos, manejo de errores y control de versiones con Git."
#3.	Aplicar los comandos aprendidos en clases, como por ejemplo: 
#•	git init 
#•	git add 
#•	git commit 
#•	git push 
#•	Uso de mensajes de commit claros (ej: "Agrega menú de productos", "Implementa descuentos", etc.) 
#4.	El repositorio debe incluir: 
#•	El archivo principal del programa (.py)
#5.	Enviar la URL del repositorio a través de AVA. 
contador_producto = 0
acumalordor_precio = 0
import os
os.system("cls") 

nombre = input("bienvenidos a la tienda pokemarket") 
flag = True
while flag:
    print ("pokeball $1000 cada unidad")
    print ("pocion $1500 precio de cada unidad")
    print ("revivir $3000 precio de cada unidad")
    print ("bayas $500 precio cada unidad")
opcion = input("pokeball , pocion , revivir , bayas")
try:
    opcion = int(input("ingrese opcion de el producto que sea comprar entre el 1 y el 4"))
    if opcion == 1:
        contador_producto + contador_producto = 1 
        acumalordor_precio + acumalordor_precio + 1000
    elif opcion == 2:
        contador_producto + contador_producto = 1
        acumalordor_precio + contador_producto = 1500
    elif opcion == 3:
        contador_producto + contador_producto = 1
        acumalordor_precio + acumalordor_precio = 3000
    elif opcion == 4:
        contador_producto + contador_producto = 1
        acumalordor_precio + acumalordor_precio = 500
    else: 
        
        print("producto o menu no encontrado intente con otro numemero de menu")
    pokeball = int(input("ingresa cantidad de el producto"))
    pocion = int(input("ingresa cantidad de el producto"))
    revivir = int(input("ingresa cantidad de el producto")) 
    bayas = int(input("ingresar cantidad de el producto a el llevar")) 
except: 
    print ("")