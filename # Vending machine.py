# Vending machine

import datetime  # ← Se requiere para guardar la fecha en el historial

is_active = True
total_money = 0
product_price = 0
change = 0
user_input = None
PRODUCTS = {
    1: {"name": "Galleta",
        "price": 1200},
    2: {"name": "Botella con Agua",
        "price": 2500},
    3: {"name": "Paquete de Papas Fritas",
        "price": 3600},
    4: {"name": "Pan",
        "price": 900}
}
DENOMINATIONS = [100, 200, 500, 1000, 2000, 5000, 10000]
Historial_para_las_compras = "historial_para_las_compras.txt"

def main():
    global is_active
    global user_input  
    while is_active:
        initialize()
        show_menu()
        input_money()
        if user_input == -1:
            print("Programa finalizando...")
            is_active = False
            print("regrese pronto")
        else:
            select_product()
            validate_payment()
            return_change()
        
def initialize():
    global total_money
    global product_price
    global change
    global user_input
    total_money = 0
    product_price = 0
    change = 0
    user_input = None
    
def show_menu():
    print("\n" + "*" * 40 )
    print("Máquina Expendidora ")
    print("Productos Disponibles")
    print("Código \t| Precio \t| Nombre")
    print("-" * 40)
    for code in PRODUCTS.keys():
        name = PRODUCTS[code]["name"]
        price = PRODUCTS[code]["price"]
        print(f"{code} \t\t| $ {price} \t| {name}")

def input_money():
    print("Por favor, ingrese su dinero.")
    print("Denominaciones válidas: $", DENOMINATIONS)
    print("Ingrese -1 para salir del programa")
    print("Ingrese 0 para seleccionar producto")
    global user_input
    global total_money
    while user_input != -1 and user_input != 0:
        user_input = int(input("\t: "))
        if user_input in DENOMINATIONS:
            total_money += user_input
            print("Saldo actual: $", total_money)
        elif user_input != -1 and user_input != 0:
            print("Valor no válido. Ingrese una denominación válida. ")
            print(DENOMINATIONS)
   
def select_product():
    global user_input
    global product_price
    user_input = None
    while user_input != 0:
        user_input = int(input("Ingrese el código del producto (0 para cancelar la compra): "))
        if user_input in PRODUCTS.keys():
            product_price = PRODUCTS[user_input]["price"]
            product_name = PRODUCTS[user_input]["name"]
            print(f"Usted ha seleccionado \"{product_name}\". Precio: ${product_price}")
            break
        elif user_input != 0:
            print("El código ingresado no es válido. Intente de nuevo.")
        elif user_input == 0:
            print("Compra cancelada...")
            break
    

def validate_payment():
    global user_input
    global total_money
    global product_price
    if user_input != 0:
        if total_money >= product_price:
            print("Su compra ha sido procesada.")
            print("Retire su producto.")
            # Guardar historial aquí
            nombre_producto = PRODUCTS[user_input]["name"]
            guardar_historial(nombre_producto, product_price, total_money, total_money - product_price)
        else:
            print("Dinero insuficiente.")
            print(f"Su saldo es ${total_money}.")
            user_input = 0
            product_price = 0

def return_change():
    global DENOMINATIONS
    global user_input
    global total_money
    global product_price
    global change
    change = total_money - product_price
    print(f"Su cambio es ${change}")
    sorted_denominations = sorted(DENOMINATIONS, reverse=True)
    change_dens = {}
    for den in sorted_denominations:
        n = change // den
        if n != 0:
            change_dens[den] = n
            change %= den
    for key, value in change_dens.items():
        if value != 0:
            print(f"\t{value} x ${key}")


def guardar_historial(nombre_producto, precio, dinero_ingresado, cambio):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"{fecha} | Producto: {nombre_producto} | Precio: ${precio} | Ingresado: ${dinero_ingresado} | Cambio: ${cambio}\n"
    with open(Historial_para_las_compras, "a", encoding="utf-8") as archivo:
        archivo.write(linea)


if __name__ == '__main__':
    main()