#Calcular la nota del trimestre a partir de tres notas, luego determinar si aprobó o
# debe recuperar e informarlo


1nota = int(input("Ingrese la primera nota: "))
2nota = int(input("Ingrese la segunda nota: "))
3nota = int(input("Ingrese la tercera nota: "))
promedio = (1nota + 2nota + 3nota) / 3
if promedio >= 70:
    print("Aprobó")
else:
    print("Debe ir a repite")

