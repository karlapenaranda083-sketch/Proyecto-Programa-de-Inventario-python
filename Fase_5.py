#Este programa calcula la cantidad de artículos que se deben pedir para reabastecer el inventario de una tienda
#comparando el stock actual con el stock mínimo requerido.

print("Bienvenido al sistema de reabastecimiento de inventario\n")

#Funcion para pedir la cantidad de cada artículo al usuario, con validación de entrada
def pedir_cantidad(nombre):
    while True:
        texto = input(f"Ingrese {nombre}: ")
        try:
            valor = int(texto)
            if valor > 0:
                return valor
            else:
                print("Error: debe ser un entero positivo mayor a cero.")
        except ValueError:
            print("Error: ingrese un número entero válido.")

a = pedir_cantidad("el stock actual de Teclados")
b = pedir_cantidad("el stock actual de Mouse")
c = pedir_cantidad("el stock actual de Monitores")
d = pedir_cantidad("el stock actual de Cargadores")
e = pedir_cantidad("el stock actual de Audifonos")

#Aquí pongo la matriz con los datos de los artículos
inventario = [
    [101,"Teclado",a,10],
    [102,"Mouse",b,10],
    [103,"Monitor",c,7],
    [104,"Cargador",d,15],
    [105,"Audifonos",e,5]
    ]

#Función para calcular la cantidad exacta a pedir de cada artículo
def calcular_pedido(stock_actual, stock_mínimo):
    if stock_actual < stock_mínimo:
        return stock_mínimo-stock_actual
    else:
        return 0

#Proceso principal
print('\nREPORTE DE REABASTECIMIENTO\n')

for artículo in inventario:
    código = artículo[0]
    nombre = artículo[1]
    stock_actual = artículo[2]
    stock_mínimo = artículo[3]


    cantidad_pedir= calcular_pedido(stock_actual, stock_mínimo)

#Mostrar los resultados
    print(f"Artículo: {nombre}")
    print(f"Stock actual: {stock_actual}")
    print(f"Stock mínimo: {stock_mínimo}")

    if cantidad_pedir > 0:
        print(f"Cantidad a pedir: {cantidad_pedir}\n")

    else:
        print("No se requiere reabastecimiento\n")

print("------------------------------")
