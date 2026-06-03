#Hands on - Asistente Financiero
"""
Eres un estudiante universitario que recibe una cantidad limitada de dinero para cubrir sus gastos de la semana.
Debes crear un programa que:
Defina cuánto dinero tienes disponible al inicio de la semana.
Registre tres gastos principales:
Transporte
Comida
Material escolar (copias, libros, impresiones, etc.)
Calcule cuánto gastaste en total.
Determine cuánto dinero te queda.
Muestre una recomendación dependiendo de tu situación financiera.
"""
PEP8= "Inicialisamos las variables y le pedimos datos al usuario sobre sus gastos"
dineroInicial = 900
Transporte = int(input("Gasto en transporte: "))
comida = int(imput("Gasto de comida: "))
materialEscolar = int(input("Gasto material escolar:"))

gastoTotal = Transporte + comida + materialEscolar
dineroRestante = dineroInicial - gastoTotal

if (dineroInicial <= dineroRestante):
    print("Gasto menos ya no te queda dinero para la semana")

