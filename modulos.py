def mensajeBienvenida(ancho):
    print(
        "=" * ancho + "\n" +
        "BIENVENIDO/A AL SISTEMA DE INSCRIPCIÓN DE SKILLMATCH".center(ancho) + "\n" +
        "=" * ancho + "\n" +
        "En este sistema vas a registrar tu participación en el proyecto.".center(ancho) + "\n" +
        "Los datos a solicitar serán:".center(ancho) + "\n" +
        "- Datos personales (nombre y DNI)".center(ancho) + "\n" +
        "- Selección de habilidades en distintos lenguajes".center(ancho) + "\n" +
        "- Breve cuestionario de validación de nivel".center(ancho) + "\n" +
        "- Años de experiencia en IT".center(ancho) + "\n" +
        "- Estado de equipo (si ya tenés o no)".center(ancho) + "\n\n" +
        "Con esta información se organizarán los equipos equilibradamente.".center(ancho) + "\n" +
        "=" * ancho
    )


def validarNombre(nombre):
    while len(nombre) < 3:
        print("El nombre es demasiado corto, ingrese nuevamente")
        nombre = input("Ingrese su nombre: ").title()
    return nombre


def validarDNI(dni, listaDNI):
    dni = dni.replace(".", "")
    while not dni.isdigit():
        print("El DNI debe estar compuesto solo de numeros. Ingrese nuevamente.")
        dni = input("Ingrese su DNI: ").replace(".", "")
    while len(dni) < 7 or len(dni) > 8:
        print("El DNI debe tener entre 7 y 8 caracteres. Ingrese nuevamente.")
        dni = input("Ingrese su DNI: ").replace(".", "")
    while dni in listaDNI:
        print("El DNI ya se encuentra registrado. Ingrese nuevamente.")
        dni = input("Ingrese su DNI: ").replace(".", "")
    return dni


def cargaParticipantes(listaNombre, listaDNI, equipo):
    nombre = input("Ingrese su nombre: ").title()
    nombre = validarNombre(nombre)
    listaNombre.append(nombre)
    dni = input("Ingrese su DNI: ").replace(".", "")
    dni = validarDNI(dni, listaDNI)
    listaDNI.append(dni)
    equipo.append(dni)


def registrar_exp(exp):
    if exp <= 1:
        valor = 1  # trainee
    elif exp <= 2:
        valor = 2  # junior
    elif exp <= 5:
        valor = 4  # semi senior
    else:
        valor = 6  # senior
    return valor


def pregExperienciaIt():
    preg = input("Ingrese la cantidad de años de experiencia que tiene en Informática: ")
    while not preg.isdigit():
        preg = input("Ingresá la cantidad de años usando solo números: ")
    respuesta = registrar_exp(int(preg))
    return respuesta

def validar_numero(mensaje, minimo, maximo):
    num_str = input(mensaje)
    while not num_str.isdigit() or int(num_str) < minimo or int(num_str) > maximo:
        print(f"Tiene que ser un número entre {minimo} y {maximo}.")
        num_str = input(mensaje)
    return int(num_str)


def cargar_habilidades():
    lenguajes = ["Python", "Java", "C++", "JavaScript", "PHP", "C#"]

    niveles = ["Nulo"] * len(lenguajes)
    respuestas_correctas = [0] * len(lenguajes)
    fila_habs = [0] * len(lenguajes)

    print("\nLenguajes para evaluar:")
    for i in range(len(lenguajes)):
        print(f"{i+1}. {lenguajes[i]}")

    cant = validar_numero("¿En cuántos de estos lenguajes tenés conocimiento? (1-6): ", 1, 6)

    preguntas = [
        ["(Python) ¿Qué imprime print(len([1,2,3]))?\nA) 2\nB) 3\nC) 4",
         "(Python) ¿Qué palabra clave define una función?\nA) def\nB) fun\nC) lambda",
         "(Python) ¿Qué estructura recorre una lista?\nA) while\nB) for\nC) switch"],

        ["(Java) ¿Tipo primitivo entero?\nA) String\nB) int\nC) Integer",
         "(Java) ¿Palabra clave para herencia?\nA) implements\nB) inherits\nC) extends",
         "(Java) ¿Método de entrada estándar?\nA) System.console\nB) System.in\nC) System.input"],

        ["(C++) ¿Biblioteca de E/S básica?\nA) <stdio.h>\nB) <iostream>\nC) <string>",
         "(C++) ¿Operador de inserción en stream?\nA) <<\nB) >>\nC) <--",
         "(C++) ¿Estructura condicional?\nA) when\nB) if\nC) guard"],

        ["(JS) ¿Palabra para variable mutable?\nA) let\nB) const\nC) var",
         "(JS) ¿Tipo de dato para 'true'?\nA) string\nB) boolean\nC) number",
         "(JS) ¿Método para longitud de string?\nA) .size()\nB) .length\nC) .count()"],

        ["(PHP) ¿Variables comienzan con?\nA) $\nB) #\nC) @",
         "(PHP) ¿Concatenación de strings?\nA) +\nB) .\nC) &",
         "(PHP) ¿Impresión estándar?\nA) echo\nB) printLine\nC) out"],

        ["(C#) ¿Palabra para propiedades automáticas?\nA) prop\nB) getset\nC) get; set;",
         "(C#) ¿Método de entrada de consola?\nA) Console.In()\nB) Console.ReadLine()\nC) Console.Read()",
         "(C#) ¿Estructura de selección múltiple?\nA) match\nB) switch\nC) choose"]
    ]

    respuestas_correctas_lista = [
        ["B", "A", "B"],
        ["B", "C", "B"],
        ["B", "A", "B"],
        ["A", "B", "B"],
        ["A", "B", "A"],
        ["C", "B", "B"]
    ]

    elegidos = []

    i = 0
    while i < cant:
        valido = False
        while not valido:
            opcion = validar_numero("\nEligí del listado anterior el lenguaje que conocés. Te haremos unas preguntas sobre el mismo para evaluar tu nivel. Seleccioná uno del 1 al 6: ", 1, 6)
            lenguaje_index = opcion - 1

            if lenguaje_index in elegidos:
                print("Ya elegiste ese lenguaje. Elegí otro distinto.")
            else:
                valido = True

        elegidos.append(lenguaje_index)

        print(f"\nPreguntas sobre {lenguajes[lenguaje_index]}:")
        aciertos = 0

        for pregunta_num in range(3):
            pregunta = preguntas[lenguaje_index][pregunta_num]
            correcta = respuestas_correctas_lista[lenguaje_index][pregunta_num]
            respuesta = input(pregunta + "\nTu respuesta (A/B/C): ").replace(" ","").upper()#chequear
            while respuesta not in ["A", "B", "C"]:
                print("Opción inválida. Responda A, B o C.")
                respuesta = input("Tu respuesta (A/B/C): ").replace(" ","").upper() #chequear
            if respuesta == correcta:
                aciertos += 1

        respuestas_correctas[lenguaje_index] = aciertos
        fila_habs[lenguaje_index] = 1
        #chequear
        if aciertos == 3:
            niveles[lenguaje_index] = "Avanzado"
        elif aciertos == 2:
            niveles[lenguaje_index] = "Intermedio"
        elif aciertos == 1:
            niveles[lenguaje_index] = "Básico"
        else:
            niveles[lenguaje_index] = "Nulo"

        print(f"Resultado de {lenguajes[lenguaje_index]}: {aciertos}/3 - Nivel: {niveles[lenguaje_index]}")
        i += 1

    print("\nTus resultados finales:")
    for i in range(len(lenguajes)):
        if niveles[i] != "nulo":
            print(f"{lenguajes[i]}: {niveles[i]} ({respuestas_correctas[i]}/3)")

    return lenguajes, niveles, respuestas_correctas, fila_habs


def pregEquipos(contador, equipo, listaNombres, listaDNIs, habilidades_matriz, niveles_matriz, exp_lista):
    preg = input("¿Tienes un equipo ya armado? (si/no)\n=> ").lower().replace(" ","")#chquear
    while preg not in ["si", "no"] :
        preg = input("Perdón, no entendí. ¿Tienes un equipo ya armado? (si/no)\n=> ").lower().replace(" ","")

    if preg == "si":
        total = validar_numero("¿Cuántos integrantes tiene tu equipo (incluyéndote)? (minimo 2 - maximo 5): ", 2, 5)
        faltan = total - contador
        print(f"Faltan cargar {faltan} integrante(s) de tu equipo.")

        for k in range(faltan):
            print(f"\n--- Ingresá la información del integrante #{k+1} ---")
            cargaParticipantes(listaNombres, listaDNIs, equipo)
            lenguajes, niveles, respuestas_correctas, fila_habs = cargar_habilidades()
            habilidades_matriz.append(fila_habs)
            niveles_matriz.append(niveles)
            exp = pregExperienciaIt()
            exp_lista.append(exp)

        print("\nTu equipo quedó conformado con los DNIs:", equipo)
    else:
        print("Te asignaremos con gente que le falte integrantes")
        print("Tu equipo parcial es:", equipo)


def main():
    mensajeBienvenida(80)
    listaDNIs = []
    listaNombres = []
    habilidades_matriz = []
    niveles_matriz = []
    exp_lista = []
    equipos_declarados = []
    equipo = []
    cargaParticipantes(listaNombres, listaDNIs, equipo)

    print("\n=== Evaluación de habilidades ===")
    lenguajes, niveles, respuestas_correctas, fila_habs = cargar_habilidades()
    habilidades_matriz.append(fila_habs)
    niveles_matriz.append(niveles)

    experienciaLaboral = pregExperienciaIt()
    exp_lista.append(experienciaLaboral)

    pregEquipos(contador=1, equipo=equipo,
                listaNombres=listaNombres, listaDNIs=listaDNIs,
                habilidades_matriz=habilidades_matriz, niveles_matriz=niveles_matriz,
                exp_lista=exp_lista)

    if len(equipo) > 0:
        equipos_declarados.append(equipo[:])

    nuevo = input("\n¿Querés cargar un nuevo participante? (si/no): ").lower()
    while nuevo not in ["si", "no"]:
        nuevo = input("Responda si/no: ").lower()

    while nuevo == "si":
        equipo = []
        cargaParticipantes(listaNombres, listaDNIs, equipo)

        print("\n=== Evaluación de habilidades ===")
        lenguajes, niveles, respuestas_correctas, fila_habs = cargar_habilidades()
        habilidades_matriz.append(fila_habs)
        niveles_matriz.append(niveles)

        experienciaLaboral = pregExperienciaIt()
        exp_lista.append(experienciaLaboral)

        pregEquipos(contador=1, equipo=equipo,
                    listaNombres=listaNombres, listaDNIs=listaDNIs,
                    habilidades_matriz=habilidades_matriz, niveles_matriz=niveles_matriz,
                    exp_lista=exp_lista)

        if len(equipo) > 0:
            equipos_declarados.append(equipo[:])

        nuevo = input("\n¿Querés cargar un nuevo participante? (si/no): ").lower()
        while nuevo not in ["si", "no"]:
            nuevo = input("Responda si/no: ").lower()

    print("\n=== Fin de inscripción ===")
    print("Participantes cargados:", len(listaDNIs))
    print("Equipos declarados (solo DNIs):", equipos_declarados)


