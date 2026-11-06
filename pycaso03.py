# ==========================================
# SISTEMA DE CONTROL DE PARQUEADERO
# Caso de Estudio 03 - Primer Semestre (Con DEF)
# ==========================================

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar ingreso de vehículo")
    print("2. Registrar salida de vehículo")
    print("3. Consultar disponibilidad")
    print("4. Salir")

def registrar_vehiculo(lista_placas, lista_tipos, motos_actuales, bicis_actuales, cap_motos, cap_bicis):
    print("\n--- REGISTRO DE INGRESO ---")
    tipo = input("Tipo de vehículo (1 para Moto, 2 para Bicicleta): ")
    placa = input("Ingrese la placa o identificación: ")
    
    # Validación con if para evitar registros vacíos
    if placa == "":
        print("ERROR: La placa o identificación no puede estar vacía.")
    else:
        if tipo == "1":
            if motos_actuales < cap_motos:
                motos_actuales = motos_actuales + 1
                lista_placas.append(placa)
                lista_tipos.append("Moto")
                print("¡Ingreso de Moto registrado con éxito!")
                print("Cupos disponibles de motos:", cap_motos - motos_actuales)
            else:
                print("ALERTA: No hay cupos disponibles para Motos.")
        elif tipo == "2":
            if bicis_actuales < cap_bicis:
                bicis_actuales = bicis_actuales + 1
                lista_placas.append(placa)
                lista_tipos.append("Bicicleta")
                print("¡Ingreso de Bicicleta registrado con éxito!")
                print("Cupos disponibles de bicicletas:", cap_bicis - bicis_actuales)
            else:
                print("ALERTA: No hay cupos disponibles para Bicicletas.")
        else:
            print("ERROR: Tipo de vehículo no válido.")
            
    return motos_actuales, bicis_actuales

def registrar_salida(lista_placas, lista_tipos, motos_actuales, bicis_actuales):
    print("\n--- REGISTRO DE SALIDA ---")
    placa_salida = input("Ingrese la placa del vehículo que va a salir: ")
    
    encontrado = 0  # Variable de control
    
    # Ciclo for para buscar en la lista de placas
    for i in range(len(lista_placas)):
        if lista_placas[i] == placa_salida:
            encontrado = 1
            tipo_vehiculo = lista_tipos[i]
            
            # Eliminamos el elemento de las listas usando su posición (índice)
            lista_placas.pop(i)
            lista_tipos.pop(i)
            
            # Actualizamos los contadores de ocupación
            if tipo_vehiculo == "Moto":
                motos_actuales = motos_actuales - 1
            else:
                bicis_actuales = bicis_actuales - 1
                
            print("¡Salida registrada con éxito para el vehículo:", placa_salida)
            break  # Rompemos el ciclo porque ya encontramos el vehículo
            
    if encontrado == 0:
        print("AVISO: No se encontró ningún vehículo registrado con esa placa.")
        
    return motos_actuales, bicis_actuales

def consultar_disponibilidad(motos_actuales, bicis_actuales, cap_motos, cap_bicis):
    print("\n--- ESTADO ACTUAL DEL PARQUEADERO ---")
    print("Motos ocupadas:", motos_actuales, "de", cap_motos, "(Libres:", cap_motos - motos_actuales, ")")
    print("Bicicletas ocupadas:", bicis_actuales, "de", cap_bicis, "(Libres:", cap_bicis - bicis_actuales, ")")

# Función principal que coordina todo el programa
def main():
    CAPACIDAD_MOTOS = 60
    CAPACIDAD_BICIS = 30

    motos_actuales = 0
    bicis_actuales = 0

    lista_placas = []
    lista_tipos = []

    print("=== PARQUEADERO CAMPUS SEGURO ===")

    # Ciclo principal con while
    while True:
        mostrar_menu()
        opcion = input("Digite una opción (1 a 4): ")
        
        if opcion == "1":
            motos_actuales, bicis_actuales = registrar_vehiculo(
                lista_placas, lista_tipos, motos_actuales, bicis_actuales, CAPACIDAD_MOTOS, CAPACIDAD_BICIS
            )
        elif opcion == "2":
            motos_actuales, bicis_actuales = registrar_salida(
                lista_placas, lista_tipos, motos_actuales, bicis_actuales
            )
        elif opcion == "3":
            consultar_disponibilidad(motos_actuales, bicis_actuales, CAPACIDAD_MOTOS, CAPACIDAD_BICIS)
        elif opcion == "4":
            print("\nSaliendo del programa. ¡Mucho éxito con tu entrega!")
            break
        else:
            print("ERROR: Opción no válida. Ingrese un número del 1 al 4.")

# Punto de ejecución del script
if __name__ == "__main__":
    main()