#16°Argumentos de solo palabras clave Para especificar que una función solo puede tener argumentos de palabras clave, agregue *, antes de los argumentos:

print(" ")#imprime en la pantalla un espacio en blanco
print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar
print(" ")#imprime en la pantalla un espacio en blanco
def my_function(*, x):
    """Función que acepta solo argumentos de palabra clave."""
    print(x)

my_function(x=3)  # Imprime 3
