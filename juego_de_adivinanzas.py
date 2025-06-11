import random

def juego_de_adivinanzas():
    try:
        rango_maximo = int(input("selecciona un numero para definir el nivel de dificultad:"))
        if rango_maximo <1 :
            print("El numero debe ser mayor a 0")
            return
    except ValueError:
        print("Entrada no valida, Debe ser un numero entero.")
        return

    numero_a_adivinar = random.randint ( 1, rango_maximo)
    intentos_maximos = rango_maximo // 20 if rango_maximo >= 20 else 1
    vector_resultados = ["fallo"] * rango_maximo
    vector_resultados[numero_a_adivinar - 1] = "correcto"
    intentos_realizados = 0
    acertado = False
    print(f"\nTienes {intentos_maximos} intentos para adivinar un número entre 1 y {rango_maximo}")

    while intentos_realizados < intentos_maximos:
        entrada = input (f"\nIntento #{intentos_realizados + 1} Ingresa tu número: ")
        try:
            intento = int(entrada)
            if intento < 1 or intento > rango_maximo:
                print("Número fuera de rango")
            else:
                intentos_realizados += 1
                if intento == numero_a_adivinar:
                    print(f"Felicidades, Adivinaste el numero ({intento}) en {intentos_realizados} intento(s)")
                    print(f"Resultado en vector: {vector_resultados[intento - 1]}")
                    acertado = True
                    break
                elif intento < numero_a_adivinar:
                    print("El numero es mayor")
                else:
                    print("El numero es menor")
        except ValueError:
            intentos_realizados += 1
            print("Entrada no es valida, Debes ingresar un numero entero")

    if not acertado:
        print(f"\nSe te acabaron los intentos. El número era {numero_a_adivinar}")
        print(f"Resultado en vector: {vector_resultados[numero_a_adivinar - 1]}")
juego_de_adivinanzas()

            