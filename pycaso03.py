# ==========================================
# SISTEMA DE CONTROL DE PARQUEADERO
# Caso de Estudio 03 - Primer Semestre (Con DEF)
# ==========================================

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar ingreso de vehículo")
    print("2. Registrar salida de vehículo")
    print("3. Consultar disponibilidad y % de ocupación")
    print("4. Registrar ficha perdida")
    print("5. Ver resumen semanal (Precálculo)")
    print("6. Salir")

def registrar_vehiculo(lista_placas, lista_tipos, motos_actuales, bicis_actuales, cap_motos, cap_bicis):
    print("\n--- REGISTRO DE INGRESO ---")
    tipo = input("Tipo de vehículo (1 para Moto, 2 para Bicicleta): ")
    placa = input("Ingrese la placa o identificación (dejar en blanco si no tiene): ")
    
    if tipo == "1":
        if motos_actuales < cap_motos:
            motos_actuales = motos_actuales + 1
            if placa == "":
                lista_placas.append("SIN PLACA")
                print("AVISO: Ingreso registrado sin placa (cuenta como novedad).")
            else:
                lista_placas.append(placa)
            lista_tipos.append("Moto")
            print("¡Ingreso de Moto registrado con éxito!")
            print("Cupos disponibles de motos:", cap_motos - motos_actuales)
        else:
            print("ALERTA: No hay cupos disponibles para Motos.")
    elif tipo == "2":
        if bicis_actuales < cap_bicis:
            bicis_actuales = bicis_actuales + 1
            if placa == "":
                lista_placas.append("SIN PLACA")
                print("AVISO: Ingreso registrado sin placa (cuenta como novedad).")
            else:
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
    if len(lista_placas) == 0:
        print("AVISO: No hay vehículos dentro del parqueadero actualmente.")
        return motos_actuales, bicis_actuales
        
    placa_salida = input("Ingrese la placa del vehículo que va a salir: ")
    encontrado = 0  
    
    for i in range(len(lista_placas)):
        if lista_placas[i] == placa_salida:
            encontrado = 1
            tipo_vehiculo = lista_tipos[i]
            
            lista_placas.pop(i)
            lista_tipos.pop(i)
            
            if tipo_vehiculo == "Moto":
                motos_actuales = motos_actuales - 1
            else:
                bicis_actuales = bicis_actuales - 1
                
            print("¡Salida registrada con éxito para el vehículo:", placa_salida)
            break  
            
    if encontrado == 0:
        print("AVISO: No se encontró ningún vehículo registrado con esa placa.")
        
    return motos_actuales, bicis_actuales

def consultar_disponibilidad(motos_actuales, bicis_actuales, cap_motos, cap_bicis):
    print("\n--- ESTADO ACTUAL Y % DE OCUPACIÓN ---")
    
    # Cálculos solicitados en las diapositivas
    pct_motos = (motos_actuales / cap_motos) * 100
    pct_bicis = (bicis_actuales / cap_bicis) * 100
    
    print(f"Motos ocupadas: {motos_actuales} de {cap_motos} (Libres: {cap_motos - motos_actuales}) | Ocupación: {pct_motos:.1f}%")
    print(f"Bicicletas ocupadas: {bicis_actuales} de {cap_bicis} (Libres: {cap_bicis - bicis_actuales}) | Ocupación: {pct_bicis:.1f}%")
    
    # Alerta requerida si la ocupación es >= 90%
    if pct_motos >= 90:
        print("⚠️ ALERTA: La zona de Motos ha superado el 90% de ocupación.")
    if pct_bicis >= 90:
        print("⚠️ ALERTA: La zona de Bicicletas ha superado el 90% de ocupación.")

def registrar_ficha_perdida(fichas_perdidas):
    print("\n--- REGISTRO DE FICHA PERDIDA ---")
    fichas_perdidas = fichas_perdidas + 1
    print("Se ha registrado una ficha perdida. Total acumulado:", fichas_perdidas)
    print("Nota: Se requiere verificación adicional con el personal de seguridad.")
    return fichas_perdidas

def resumen_semanal():
    print("\n--- RESUMEN SEMANAL (PRECÁLCULO) ---")
    # Datos oficiales de la tabla del caso de estudio
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    ingresos = [118, 126, 132, 121, 109]
    
    total_ingresos = sum(ingresos)
    promedio = total_ingresos / len(dias)
    
    print(f"Ingresos diarios: Lunes={ingresos[0]}, Martes={ingresos[1]}, Miércoles={ingresos[2]}, Jueves={ingresos[3]}, Viernes={ingresos[4]}")
    print(f"Promedio de ingresos semanales: {promedio:.1f}")
    print(f"Día de mayor ingreso: Miércoles (con {max(ingresos)} ingresos y 96% de ocupación máxima).")

def main():
    CAPACIDAD_MOTOS = 60
    CAPACIDAD_BICIS = 30

    motos_actuales = 0
    bicis_actuales = 0
    fichas_perdidas = 0

    lista_placas = []
    lista_tipos = []

    print("=== PARQUEADERO CAMPUS SEGURO ===")

    while True:
        mostrar_menu()
        opcion = input("Digite una opción (1 a 6): ")
        
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
            fichas_perdidas = registrar_ficha_perdida(fichas_perdidas)
        elif opcion == "5":
            resumen_semanal()
        elif opcion == "6":
            print("\nSaliendo del programa. ¡Mucho éxito con tu entrega!")
            break
        else:
            print("ERROR: Opción no válida. Ingrese un número del 1 al 6.")

if __name__ == "__main__":
    main()