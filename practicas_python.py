#Diferecinia de def y lambda y como utilizarlas (ejemplos)

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)



sumar = lambda a, b: a + b

resultado = sumar(5, 3)
print(resultado)



# Estudiando las variables
nombre = "Abner"
edad = 30
ciudad = "Agua Prieta, Sonora"
objetvo = "Convertirme en especialista en CiberSeguridad"

print("Hola, soy", nombre)
print("Tengo", edad, "años")
print("Vivo en la ciudad de", ciudad)
print("Mi objetivo en la vida es", objetvo)



#Estudiando el input
nombre = input("¿Como te llamas?: ")
edad = input("¿Cuantos años tines?: ")
ciudad = input("¿En donde vives?: ")
meta_profecional = input("¿Cual es tu meta profecional?: ")

print()
print("Hola,", nombre)
print("Tienes", edad, "años")
print("Vives en la ciuadad de", ciudad)
print("Tu meta profecional es ser", meta_profecional)



#Calculdora
numero1 = int(input("Primer numero"))
numero2 = int(input("Seguno numero"))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print("\nResultados:")
print("suma: ", suma)
print("resta: ", resta)
print("multiplicacion: ", multiplicacion)
print("Division: ", division)


#Calculadora para sacar año de nacimiento
edad = int(input("¿Que edad tienes?: "))
año_actual = int(input("Año actual: "))
año_nacimiento = (año_actual) - (edad)

print("Tienes", edad, "años")
print("El año actual es", año_actual)
print("Naciste aproximadamente en el año de:", año_nacimiento)