# SIN FUNCIONES:
# num1 = float(input("Ingresa el primer número: "))
# num2 = float(input("Ingresa el segundo número: "))
# operacion = str(input("¿Quieres realizar una suma, resta, multiplicación o división?: "))

# if operacion == "suma":
#     suma = num1 + num2
#     print(f"El resultado de la suma es {suma}")
    
# elif operacion == "resta":
#     resta = num1 - num2
#     print(f"El resultado de la resta es {resta}")
    
# elif operacion == "multiplicacion":
#     multiplicacion = num1 * num2
#     print(f"El resultado de la multiplicación es {multiplicacion}")

# elif operacion == "division":
#     division = num1 / num2
#     print(f"El resultado de la división es {division}")
    
# else:
#     print("Escoja una operación válida")
    
    
# USANDO UNA FUNCIÓN:
def calculadora(): # Se usa la función para reutilizar el código sin necesidad de repetirlo. Si en el futuro quiero ejecutar la calculadora en otro programa, solo necesito llamar a calculadora().
                   # Los argumentos en una función sirven para pasarle datos desde fuera de estas, pero aquí todos los valores se obtienen dentro de la función. 
    try: #El bloque try permite ejecutar código que podría generar errores en entrada de datos sin detener el programa abruptamente.
        num1 = float(input("Ingresa el primer número: ")) # input() devuelve siempre texto, por lo que se necesita convertir a formato número antes de hacer cálculos.
        num2 = float(input("Ingresa el segundo número: "))
        operacion = input("¿Quieres realizar una suma, resta, multiplicación o división?: ").strip().lower() #strip() elimina espacios en blanco extra al inicio o final del texto ingresado por el usuario. Mientras que lower() convierte las entradas a minúsculas para que por ejemplo "SUMA", "Suma", "suMa", etc. sean reconocidos correctamente como "suma".
                                                                                                             # strip() y lower() van al final porque el input() debe ejecutarse primero antes de poder estos dos. Todo va en secuencia lógica.
        operaciones = { # Un diccionario es una estructura eficiente para relacionar claves y valores, y evita el uso de múltiples if-elif. Permite agregar más operaciones fácilmente con solo añadir nuevas claves y valores.
            "suma": num1 + num2,
            "resta": num1 - num2,
            "multiplicacion": num1 * num2,
            "multiplicación": num1 * num2,
            "division": num1 / num2 if num2 != 0 else "Error: No se puede dividir por cero", # Este if evita el error matemático de división por cero, que haría que el programa se detuviera inesperadamente. Devuelve mensaje en vez de producir un error crítico.
            "división": num1 / num2 if num2 != 0 else "Error: No se puede dividir por cero",
        }

        resultado = operaciones.get(operacion, "Operación no válida") # .get() busca la clave en el diccionario y devuelve su valor en una sola línea. Si el usuario escribe una operación que no esté en el diccionario, entonces recibirá el mensaje especificado.
        print(f"El resultado es: {resultado}" if isinstance(resultado, (int, float)) else resultado) # isinstance comprueba si el resultado es un número antes de imprimir. Si el resultado es un mensaje de error como los ya mencionados, simplemente imprime el error sin agregar "El resultado es:".

    except ValueError: # Value Error ocurre cuando se intenta convertir texto en número y no es posible.
        print("Error: Ingresa valores numéricos válidos")
# return no es necesario aquí porque la función imprime el resultado directamente, por lo que no es necesario guardar el resultado en return para luego imprimirlo. Hay que entender que return funciona así: devuelve un valor a la parte del código que llamó a la función.
# Cuando usamos return, la función no imprime directamente el resultado, sino que devuelve un valor.
calculadora() # Sin esta línea el código no se ejecuta automáticamente cuando corro el archivo. Es decir, como la función tiene print(), entonces al llamarla de esta forma muestra el resultado.
              # No es necesario almacenar ni procesar nada con un return, ya que la función recibe los datos, realiza los cálculos y muestra el resultado en pantalla. Simplemente llamo la función y listo. 
