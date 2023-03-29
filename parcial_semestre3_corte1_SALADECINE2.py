#print(f"El precio final para {num_boletas} boleta(s) en la sala {tipo_sala} a las {hora_dia} {sufijo} y con {tipo_pago} como medio de pago y reserva {'sí' if tiene_reserva.lower() == 'sí' else 'no'} es: {precio_final + recargo_reserva:,.0f} pesos.")

tipo_sala = input("Ingrese el tipo de sala (Dinamix, 3D, 2D): ")
num_boletas = int(input("Ingrese el número de boletas: "))
hora_dia = int(input("Ingrese la hora del día (en formato 24 horas): "))
tipo_pago = input("Ingrese el tipo de pago (CinemaCard o Otros): ")
tiene_reserva = input("¿Tiene reserva? (Sí o No): ")

# aca transformo a horas a las usadas regularmente
if hora_dia >= 12:
    sufijo = "PM"
    hora_dia = hora_dia - 12
else:
    sufijo = "AM"
    
    
    if hora_dia == 0:
        hora_dia = 12
    
precio_base = 0
if tipo_sala.lower() == "dinamix":
    if hora_dia >= 5 and hora_dia < 11:
        precio_base = 28200  # 50% de aumento en horas pico
    else:
        precio_base = 18800  # 10% de descuento en horas no pico
elif tipo_sala.lower() == "3d":
    if hora_dia >= 5 and hora_dia < 11:
        precio_base = 19375  # 25% de aumento en horas pico
    else:
        precio_base = 15500  # 10% de descuento en horas no pico
elif tipo_sala.lower() == "2d":
    if hora_dia >= 5 and hora_dia < 11:
        precio_base = 14125  # 25% de aumento en horas pico
    else:
        precio_base = 11300  # 10% de descuento en horas no pico
else:
    print("Tipo de sala no válido")
    exit()

descuento_boletas = 0
if num_boletas >= 3:
    descuento_boletas = (num_boletas - 3) * 500

descuento_tarjeta = 0
if tipo_pago.lower() == "cinemacard":
    descuento_tarjeta = 0.05

recargo_reserva = 0
if tiene_reserva.lower() in ["sí", "si"]:
    recargo_reserva = 2000 * num_boletas

precio_final = (precio_base * num_boletas - descuento_boletas) * (1 - descuento_tarjeta)

print(f"El precio final para {num_boletas} boleta(s) en la sala {tipo_sala} a las {hora_dia}{sufijo} y con {tipo_pago} como medio de pago y reserva {'sí' if tiene_reserva.lower() in ['sí', 'si'] else 'no'} es: {precio_final + recargo_reserva:,.0f} pesos.")

print ("creadores Diego Rueda, Cristian Gonzales")
