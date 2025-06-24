
datos = {
    "datos_entrada":[]
}

def validar_numero(mensaje_input: str):
    return 

def consultar_comprador():
    print(f"[codigo_entrada: {datos["codigo"]}] - [tipo_entrada: {datos["tipo"]}] - [comprador: {datos["nombre"]}]")

while True:
    print("\n---MENU PRINCIPAL---")
    print("[1] - Comprar entrada")
    print("[2] - Consultar comprador")
    print("[3] - Cancelar compra")
    print("[4] - Salir")


if opcion == 1:
    print("\n---MENU DE COMPRA---")
    codigo_entrada = 0
    while True:
        codigo_entrada = validar_numero("Ingrese su codigo de confirmacion: ")
        if len(str(codigo_entrada)) > 6 or len(str(codigo_entrada)) < 6:
               print("El maximo de digitos es de 6")
               continue
        
        codigo_repetido = 0
        for codigo in datos["datos_entradas"]:
            if codigo["ID"] == codigo_entrada:
                print("Este codigo ya existe")
                codigo_repetido = 1
                break
        while True:
             nombre_comprador = input("Ingrese su nombre: ")
             if len(nombre_comprador) == 0:
                  print("El nombre no puede estar vacio")
                  continue
             nombre_repetido = 0
             for nombre in datos["datos_entrada"]:
                  if nombre["nombre"].lower() == nombre.lower:
                       print("Este nombre ya esta registrado")
                  nombre_repetido = 1
                  break
             if nombre_repetido == 0:
                break
        while True:
            tipo = input("Escriba el tipo de entrada (G = General, V = VIP): ")
            if tipo in ["G, V"]:
                break
            print("Tipos disponibles: G (General) y V (VIP)")

        datos["datos_entrada"].append({
            "ID": codigo_entrada
            "nombre": nombre_comprador
            "tipo": tipo
        })
        print("Entrada comprada exitosamente")
             
        
