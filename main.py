import subprocess

def ejecutar_prolog(comando, archivo_prolog):
    # Se ajusta el comando correctamente para Prolog
    comando_prolog = f"({comando}), write(D), nl."
    
    # Se ejecutamos el proceso
    proceso = subprocess.Popen(['swipl', '-q', '-s', archivo_prolog, '-g', comando_prolog, '-t', 'halt'],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    salida, error = proceso.communicate()
    
    salida_decodificada = salida.decode('utf-8').strip()
    error_decodificado = error.decode('utf-8').strip()

    if error_decodificado:
        print("Error:", error_decodificado)

    return salida_decodificada



def leer_y_ejecutar_archivo_prolog(ruta_archivo, archivo_prolog):
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                print("-"*90)
                print(f"Ejecutando: {linea}")
                resultado = ejecutar_prolog(linea, archivo_prolog)
                print("Resultado:", resultado)


leer_y_ejecutar_archivo_prolog("problemas.txt", "swish.pl")
