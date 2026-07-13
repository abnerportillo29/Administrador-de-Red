calificacion = int(input("¿Caual es tu califiacion?: "))

if calificacion >= 90:
    print("Excelente")

elif calificacion >= 80 and calificacion <90:
    print("Muy bien")

elif calificacion >=70 and calificacion <80:
    print("Aprobaste")

else:
    print("Reprobaste")