# Tendencia e Innovacion en Tecnologias Agricolas (TEA)

contador = 0 
sumatoria = 0
while True:
    try:
        input_str = input ("Ingrese un número: ")
        if(input_str == 'done'):
            break
        else:
            contador = contador + 1
            sumatoria = sumatoria + int(input_str)
            promedio = sumatoria / contador
    except:
        print("Error, debe ingresar un número")
        continue
print("Contador:", contador)
print("Sumatoria:", sumatoria)
print("Proedio:", sumatoria / contador)