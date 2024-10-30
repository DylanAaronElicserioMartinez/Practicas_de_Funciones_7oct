#19°Combine solo posicional y solo palabras clave Puede combinar los dos tipos de argumentos en la misma función.
#Cualquier argumento antes de / es solo posicional y cualquier argumento después de * es solo de palabra clave.
print(" ")#imprime en la pantalla un espacio en blanco
print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar
print(" ")#imprime en la pantalla un espacio en blanco
def my_function(a, b, /, *, c, d):
    """Función que combina argumentos posicionales y de palabra clave."""
    print(a + b + c + d)

my_function(5, 6, c=7, d=8)  # Imprime 26