print("Prueba de if mas avanzada, el and es para agregar mas condiciones, sin embargo el OR sería algo como una u otra,"
      "es decir, si no se cumple una pero se cumple la otra, la condicion seguiria siendo true" )
print()
print("Ejemplo: "
      "true and true = True "
      "true and false = False "
      "false and false = False "
      "true or true = True "
      "true or false = True "
      "false or false = False "
      "Tener en cuenta que el or, para que se ejecute antes que las demas condiciones se debera poner en parentesis" )
print("Como dato extra, el .upper() es un metodo que sirve para poner todo el string seleccionado en mayuscula, incluyendo la respuesta de la funcion en este caso input,"
      "osea que, da igual si la respuesta se escribe en mayuscula o minuscula siempre se convertira en mayuscula. y lo pongo en esta string como ejemplo".upper())

apetece_helado_input = input("Le apetece comer helado? (Si/No)").upper()

if apetece_helado_input == "Si".upper():
    apetece_helado_input = True
elif apetece_helado_input == "No".upper(): # El elif sería una especie de fusion entre if y else, es para agregar una condicion extra como se ve en este caso #
    apetece_helado_input = False
else:
    print("Te e dicho que digas si si o no, no se que as dicho pero supongo que no ")

tienes_dinero_para_helado_input = input("Tienes dinero para un helado? (Si/No)").upper()

if tienes_dinero_para_helado_input == "Si".upper():
    tienes_dinero_para_helado_input = True
elif tienes_dinero_para_helado_input == "No".upper():
    tienes_dinero_para_helado_input = False
else:
    print("Decime algo coherente flaco")

esta_tu_tia_cerca_tuyo_input = input("Estas con tu tía? (Si/No)").upper()

if esta_tu_tia_cerca_tuyo_input == "Si".upper():
    esta_tu_tia_cerca_tuyo_input = True
elif esta_tu_tia_cerca_tuyo_input == "No".upper():
    esta_tu_tia_cerca_tuyo_input = False
else:
    print("Flaco me estas cansando")

esta_el_señor_heladero_input = input("Esta el heladero? (Si/No)").upper()

if esta_el_señor_heladero_input == "Si".upper():
    esta_el_señor_heladero_input = True
elif esta_el_señor_heladero_input == "No".upper():
    esta_el_señor_heladero_input = False
else:
    print("bueno andate a la concha de tu hermana")

apetece_helado = apetece_helado_input
tienes_dinero_para_helado = tienes_dinero_para_helado_input
esta_tu_tia_cerca_tuyo = esta_tu_tia_cerca_tuyo_input
puedes_permitirtelo = tienes_dinero_para_helado or esta_tu_tia_cerca_tuyo
esta_el_señor_heladero = esta_el_señor_heladero_input

if apetece_helado == True and puedes_permitirtelo == True and esta_el_señor_heladero == True:
    print("Bueno, entonces podes comprarte uno, sorete")
else:
    print("Mejor le doy helado a tu vieja, trolo")
