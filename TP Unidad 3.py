# 1 -
nombre = input("Ingrese nombre del cliente: ")

while not nombre.isalpha():
    print("El nombre debe tener solo letras")
    nombre = input("Ingrese nombre del cliente: ")

productos_a_comprar = input("Ingrese la cantidad de productos que quiere comprar: ")

while (not productos_a_comprar.isdigit()) or (int(productos_a_comprar) <= 0):
    print("ingrese un numero entero mayor que 0")
    productos_a_comprar = input("Ingrese la cantidad de productos que quiere comprar: ")

cantidad_productos = int(productos_a_comprar)

total_sin_descuento = 0
total_con_descuento = 0

for i in range(cantidad_productos):

    precio = (input("Ingrese precio del producto: "))
    while not precio.isdigit():
        print("Ingrese un valor numerico")
        precio = (input("Ingrese precio del producto: "))
    precio = int(precio)

    descuento = input("El precio tiene algun descuento?: S/N").lower()
    while descuento not in ("s", "n"):
        print("Debe ingresar S o N")
        descuento = input("El precio tiene algun descuento?: S/N").lower()
    
    total_sin_descuento += precio
    
    if descuento == "s":
        precio_c_desc = precio * 0.9
    else:
        precio_c_desc = precio
        
    total_con_descuento += precio_c_desc

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_productos

print(f"El total de la compra sin descuentos es de: ${total_sin_descuento:.2f}")
print(f"El total de la compra con descuentos es de: ${total_con_descuento:.2f}")
print(f"Usted a ahorrado: ${ahorro:.2f}")
print(f"El promedio de la compra es de: ${promedio:.2f}")

# 2 -

usuario = "alumno"
clave = "python123"
login_correcto = False

for intento in range (1,4):
    print(f"Intento {intento} de 3")
    usuario_ingresado = input("Usuario: ")
    clave_ingresada = input("Clave :")
    
    if usuario_ingresado == usuario and clave_ingresada == clave:
        print("Login correcto")
        login_correcto = True
        break
    else:
        print("Usuario o clave incorrecta!")

if not login_correcto:
    print("Cuenta bloqueda")
    
if login_correcto:
    opcion = 0
    while opcion != 4:
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion_string = input("Opción: ") 
        
        while not opcion_string.isdigit():
            print("Error: Ingrese un numero valido")
            opcion_string = input("Opcion: ")
            
        opcion = int(opcion_string)
        
        if opcion < 1 or opcion > 4:
            print("Elegir una opcion entre 1 y 4.")
            continue
        
        if opcion == 1:
            print("Estado de inscripcion: Activo")
        elif opcion == 2:
            nueva_clave = input("Ingrese su nueva clave: ")
            if len(nueva_clave) < 6:
                print("La clave debe tener minimo 6 caracteres")
            else:
                confirmacion = input("Confirme su nueva clave: ")
                if confirmacion == nueva_clave:
                    clave = nueva_clave
                    print("Cambio exitoso")
                else:
                    print("Las claves no coinciden")                
        elif opcion == 3:
            print("Hoy sera un gran dia")
        elif opcion == 4:
            print("Salir")
            break
        
# 3 -

operador = input("Ingrese nombre del operador: ")

while not operador.isalpha():
    print("El operador debe tener solo letras")
    operador = input("Ingrese nombre del operador: ")
    

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

opcion = 0
while opcion != 5:
    print("1) Reservar Turno")
    print("2) Cancelar Turno")
    print("3) Ver agenda del dia")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")
    
    opcion_str = input("Opcion: ")
    
    while not opcion_str.isdigit():
        print("Ingrese un numero del 1 al 5")
        opcion_str = input("Opcion: ")
    
    opcion = int(opcion_str)
    
    if opcion < 1 or opcion > 5:
        print("Opcion fuera de rango")
        continue

    if opcion == 1:
        dia_str = input("Elegir dia: 1_Lunes, 2_Martes: ")
        while not dia_str.isdigit():
            print("Ingrese 1 o 2")
            dia_str = input("Elegir dia: 1_Lunes, 2_Martes: ")
            
        dia = int(dia_str)
        if dia < 1 or dia > 2:
            print("Dia fuera de rango")
        else:
            paciente = input("Nombre del paciente: ")
            while not paciente.isalpha():
                print("Ingrese solo letras")
                paciente = input("Nombre del paciente: ")
                
            if dia == 1:
                if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                    print("Este paciente ya tiene turno el lunes.")
                else:
                    if lunes1 == "":
                        lunes1 = paciente
                    elif lunes2 == "":
                        lunes2 = paciente
                    elif lunes3 == "":
                        lunes3 = paciente
                    elif lunes4 == "":
                        lunes4 = paciente
                    else:
                        print("No hay turnos disponibles el lunes.")
            else:
                if paciente == martes1 or paciente == martes2 or paciente == martes3:
                    print("Ese paciente ya tiene turno el martes.")
                else:
                    if martes1 == "":
                        martes1 = paciente
                    elif martes2 == "":
                        martes2 = paciente
                    elif martes3 == "":
                        martes3 = paciente
                    else:
                        print("No hay turnos disponibles el martes.")
    elif opcion == 2:
        dia_str = input("Elegir dia para cancelar: 1_Lunes, 2_Martes: ")
        while not dia_str.isdigit():
            print("Ingrese 1 o 2")
            dia_str = input("Elegir dia para cancelar: 1_Lunes, 2_Martes: ")

        dia = int(dia_str)
        if dia < 1 or dia > 2:
            print("Dia fuera de rango")
        else:
            paciente = input("Nombre del paciente a cancelar: ")
            while not paciente.isalpha():
                print("Ingrese solo letras")
                paciente = input("Nombre del paciente a cancelar: ")

            encontrado = False

            if dia == 1:
                if paciente == lunes1:
                    lunes1 = ""
                    encontrado = True
                elif paciente == lunes2:
                    lunes2 = ""
                    encontrado = True
                elif paciente == lunes3:
                    lunes3 = ""
                    encontrado = True
                elif paciente == lunes4:
                    lunes4 = ""
                    encontrado = True
            else:
                if paciente == martes1:
                    martes1 = ""
                    encontrado = True
                elif paciente == martes2:
                    martes2 = ""
                    encontrado = True
                elif paciente == martes3:
                    martes3 = ""
                    encontrado = True

            if encontrado:
                print("Turno cancelado correctamente.")
            else:
                print("No se encontró un turno con ese nombre en ese dia.")
    elif opcion == 3:
        dia_str = input("Ver agenda de: 1_Lunes, 2_Martes: ")
        while not dia_str.isdigit():
            print("Ingrese 1 o 2")
            dia_str = input("Ver agenda de: 1_Lunes, 2_Martes: ")

        dia = int(dia_str)
        if dia < 1 or dia > 2:
            print("Dia fuera de rango")
        else:
            if dia == 1:
                print("Agenda Lunes:")
                print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
                print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
                print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
                print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
            else:
                print("Agenda Martes:")
                print("Turno 1:", martes1 if martes1 != "" else "(libre)")
                print("Turno 2:", martes2 if martes2 != "" else "(libre)")
                print("Turno 3:", martes3 if martes3 != "" else "(libre)")
    elif opcion == 4:
        ocupados_lunes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1
        libres_lunes = 4 - ocupados_lunes

        ocupados_martes = 0
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1
        libres_martes = 3 - ocupados_martes

        print("Lunes - ocupados:", ocupados_lunes, "libres:", libres_lunes)
        print("Martes - ocupados:", ocupados_martes, "libres:", libres_martes)

        if ocupados_lunes > ocupados_martes:
            print("Lunes tiene más turnos.")
        elif ocupados_martes > ocupados_lunes:
            print("Martes tiene más turnos.")
        else:
            print("Hay empate en cantidad de turnos.")
            
    elif opcion == 5:
        print("Cerrando sistema...")

# 4 -

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

agente = input("Nombre del agente: ")
while not agente.isalpha():
    print("Error: solo se permiten letras.")
    agente = input("Nombre del agente: ")
    
racha_forzar = 0
    
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    print(f"Energía: {energia}  Tiempo: {tiempo}  Cerraduras abiertas: {cerraduras_abiertas}  Alarma: {alarma}")

    opcion_str = input("1) Forzar cerradura  2) Hackear panel  3) Descansar\nOpción: ")
    while not opcion_str.isdigit():
        print("Error: ingrese un número válido.")
        opcion_str = input("Opción: ")

    opcion = int(opcion_str)
    if opcion < 1 or opcion > 3:
        print("Error: opción fuera de rango.")
        continue

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        if energia < 40 and not alarma:
            riesgo_str = input("Riesgo de alarma. Elija un número del 1 al 3: ")
            while not riesgo_str.isdigit():
                print("Error: ingrese un número entre 1 y 3.")
                riesgo_str = input("Riesgo de alarma. Elija un número del 1 al 3: ")

            riesgo = int(riesgo_str)
            while riesgo < 1 or riesgo > 3:
                print("Error: el número debe ser entre 1 y 3.")
                riesgo_str = input("Riesgo de alarma. Elija un número del 1 al 3: ")
                while not riesgo_str.isdigit():
                    print("Error: ingrese un número entre 1 y 3.")
                    riesgo_str = input("Riesgo de alarma. Elija un número del 1 al 3: ")
                riesgo = int(riesgo_str)

            if riesgo == 3:
                alarma = True
                print("¡La alarma se ha activado!")

        if racha_forzar == 3:
            alarma = True
            print("¡Alarma activada por forzar 3 veces seguidas! No se abre la cerradura.")
        else:
            if not alarma:
                cerraduras_abiertas += 1
                print("Lograste abrir una cerradura.")

    elif opcion == 2:
        racha_forzar = 0
        energia -= 10
        tiempo -= 3

        print("Iniciando hackeo del panel...")
        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso hackeo paso {i+1}, código parcial: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3 and not alarma:
            cerraduras_abiertas += 1
            print("¡Hackeo exitoso! Se abrió una cerradura.")

    elif opcion == 3:
        racha_forzar = 0
        tiempo -= 1

        if alarma:
            energia -= 10
            print("Descansás bajo alarma. Pierdes energía extra.")
        else:
            energia += 15
            if energia > 100:
                energia = 100
            print("Descansás y recuperas energía.")
    
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("La alarma bloqueó la bóveda. DERROTA por bloqueo.")
        break

if cerraduras_abiertas == 3:
    print("¡VICTORIA! Abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA. Te quedaste sin energía o sin tiempo.")
elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
    print("DERROTA por bloqueo de la alarma.")

# 5 - 

nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
turno_gladiador = True

print("=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    opcion_str = input("Elige acción:\n1. Ataque Pesado\n2. Ráfaga Veloz\n3. Curar\nOpción: ")

    while not opcion_str.isdigit():
        print("Ingrese un número válido.")
        opcion_str = input("Opción: ")

    opcion = int(opcion_str)
    if opcion < 1 or opcion > 3:
        print("opción fuera de rango.")
        continue
    
    if opcion == 1:
        if vida_enemigo < 20:
            danio = danio_pesado * 1.5
            print("Golpe Critico!")
        else:
            danio = danio_pesado
            
        vida_enemigo -= danio
        print(f"Atacaste al enemigo por {danio} puntos de daño!")
        
    elif opcion == 2:
        print(">> Inicias unas rafaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
            
    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print(f"Te curaste 30 puntos de vida. Vida actual: {vida_jugador}. Pociones restantes: {pociones}")
        else:
            print("¡No quedan pociones!")


    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"El enemigo te atacó por {danio_enemigo} puntos de daño.")
        
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")


