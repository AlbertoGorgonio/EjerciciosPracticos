# Contador de palabras en este caso un archivo de texto
def contar_palabras(nombre_archivo):
    
    with open(nombre_archivo, 'r') as archivo:
        texto = archivo.read()
        palabras = texto.split()
        return len(palabras)

# Ejemplo de uso:
archivo = 'ejemplo.txt'
cantidad_palabras = contar_palabras(archivo)
print(f"El archivo contiene {cantidad_palabras} palabras.")
