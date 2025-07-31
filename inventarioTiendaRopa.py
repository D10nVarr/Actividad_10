invetario_general={}
cant_categorias={}

produtos=int(input("Ingrese la cantidad de productos que desee ingresar: "))

for i in range(produtos):
    print(f"\nRegistro del producto {i+1}: ")

    while True:
        codigo=input("Ingrese el codigo del producto: ")
        if codigo not in invetario_general:
            break
        else:
            print("Este código ya esta registrado con otro producto")
    name_product = input("Ingrese el nombre del producto: ")
    categoria=input("Ingrese el categoria del producto: ")
    talla=input("Ingrese el talla del producto: ")
    while True:
        price_unit=float(input("Ingrese el precio unitario del producto: "))
        if price_unit>0:
            break
        else:
            print("El precio ingresado no es válido")
    while True:
        stock=int(input("Ingrese la cantidad del stock del producto: "))
        if stock>0:
            break
        else:
            print("La cantidad ingresada debe ser un número positivo")

    invetario_general[codigo]={
        "Código":codigo,
        "Nombre del producto":name_product,
        "Categoria":categoria,
        "Talla":talla,
        "Precio unitario":price_unit,
        "Cantidad en stock":stock,
    }

    contador=1
    if categoria not in cant_categorias:
        cant_categorias[categoria]=contador
        contador+=1
    else:
        cant_categorias[categoria]=1

print(f"\n-----INVENTARIO GENERAL-----")

for codigo, valor in invetario_general.items():

    print(f"\nRegistro del producto: {codigo}")
    print(f"Nombre del producto: {valor['Nombre del producto']}")
    print(f"Categoria: {valor['Categoria']}")
    print(f"Talla: {valor['Talla']}")
    print(f"Precio unitario: {valor['Precio unitario']}")
    print(f"Cantidad en stock: {valor['Cantidad en stock']}")

print(f"\nBuscador de productos:")

buscador=input("Ingrese el gódigo del producto que desee visualizar: ")

if buscador in invetario_general:
    print(f"\nNombre del producto: {invetario_general[buscador]["Nombre del producto"]}")
    print(f"Categoria: {invetario_general[buscador]["Categoria"]}")
    print(f"Talla: {invetario_general[buscador]["Talla"]}")
    print(f"Precio unitario: {invetario_general[buscador]["Precio unitario"]}")
    print(f"Cantidad en stock: {invetario_general[buscador]["Cantidad en stock"]}")
else:
    print("El código del producto no existe")

print(f"\n-----Valor total del inventario-----")
suma_total=0

for i in invetario_general.values():
    sum_temp=i["Cantidad en stock"]*i["Precio unitario"]
    suma_total+=sum_temp
print(f"\nEl valor total del inventario asciende a los Q.{suma_total}")

print(f"\n-----Productos por categoria-----")

for categoria, valor in cant_categorias.items():
    print(f"\n Para la categoría {categoria} hay: {valor} productos")


