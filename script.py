# leer el archivo
texto = open("texto.txt", "r")

texto = texto.readlines()
variables = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ_"
numeros = "1234567890"
operaciones = "+-%*/^"
parentesis_iniciales = 0
parentesis_terminales = 0


# for loop del analisis
for z in range(0, len(texto)):
    i = 0
    texto[z].replace(" ", "")
    while i <= len(texto[z])-1:
        if texto[z][i] in variables:
            print(texto[z][i], "variable")
        elif texto[z][i] in numeros or (texto[z][i] == "-" and texto[z][i+1] in numeros):
            if texto[z][i+1] in numeros or texto[z][i+1] == ".":
                # manejo de numeros reales
                numero = ""
                numero_real = False
                while texto[z][i] in numeros or texto[z][i] == "." or (texto[z][i] == "-" and texto[z][i+1] in numeros) or (texto[z][i] == "E" and texto[z][i+1] in numeros) or (texto[z][i] == "E" and texto[z][i+1] == "-" and texto[z][i+2] in numeros):
                    numero += texto[z][i]
                    i = i + 1
                    if texto[z][i] == ".":
                        numero_real = True
                i = i-1
                if numero == "":
                    print("error: numero entero mal declarado")
                else:
                    if numero_real:
                        print(numero, "numero real")
                    else:
                        print(numero, "numero entero")
            else:
                print(texto[z][i], "numero entero")
        elif texto[z][i] == "/" and texto[z][i+1] == "/":
            print(texto[z][i:len(texto[z])], "comentario")
            break

        elif texto[z][i] == "=":
            if texto[z][i+1] in variables or texto[z][i+1] in numeros or texto[z][i+1] == "-" or texto[z][i+1] == "(":
                print(texto[i], "asignacion")
            else:
                if texto[z][i+1] == " " and (texto[z][i+2] in variables or texto[z][i+2] in numeros or texto[z][i+2] == "-" or texto[z][i+2] == "("):
                    print(texto[z][i], "asignacion")
                else:
                    print(
                        "error: sintaxis incorrecta en cuanto al simbolo", texto[z][i])
                    break
        elif texto[z][i] in operaciones:
            if texto[z][i+1] in variables or texto[z][i+1] in numeros or texto[z][i+1] == "-" or texto[z][i+1] == "(":
                if texto[z][i] == "*":
                    print(texto[z][i], "multiplicacion")

                elif texto[z][i] == "+":
                    print(texto[z][i], "suma")

                elif texto[z][i] == "-":
                    print(texto[z][i], "resta")
                elif texto[z][i] == "/":
                    print(texto[z][i], "division")
                elif texto[z][i] == "^":
                    print(texto[z][i], "potencia")
                elif texto[z][i] == "%":
                    print(texto[z][i], "mod")

            else:
                print(
                    "error: sintaxis incorrecta en cuanto al simbolo", texto[z][i])
                break

        elif texto[z][i] == "(":
            print(texto[z][i], "parentesis que abre")
            parentesis_iniciales += 1
        elif texto[z][i] == ")":
            print(texto[z][i], "parentesis que cierra")
            parentesis_terminales += 1
        i += 1
    if parentesis_iniciales != parentesis_terminales:
        print("error: no se cierran todos los parentesis")
