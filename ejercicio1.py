medicamentos = 60000
despacho = 8000
edad = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo (A, B, C o D): ")
if tramo == "a":
    tramo = "A"
if tramo == "b":
    tramo = "B"
if tramo == "c":
    tramo = "C"
if tramo == "d":
    tramo = "D"
if edad > 60:
    descuento_med = 0
elif edad <= 30:
    if tramo == "A" or tramo == "B":
        descuento_med = 0.18
    else:
        descuento_med = 0.12
else:
    if tramo == "A" or tramo == "B":
        descuento_med = 0.12
    else:
        descuento_med = 0.08
descuento_des = 0
if tramo == "A" or tramo == "B":
    descuento_des = 0.10
    if edad >= 55:
        descuento_des = 0.15
valor_medicamentos = medicamentos - (medicamentos * descuento_med)
valor_despacho = despacho - (despacho * descuento_des)
print("El valor de medicamentos es:", int(valor_medicamentos))
print("El valor del despacho es:", int(valor_despacho))
