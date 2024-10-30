#13°Argumentos sólo posicionales Puede especificar que una función pueda tener SÓLO argumentos posicionales o SÓLO argumentos de palabras clave.
#Para especificar que una función solo puede tener argumentos posicionales, agregue , / después de los argumentos:
#Ícono de validado por la comunidad
print(" ")#imprime en la pantalla un espacio en blanco
print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar
print(" ")#imprime en la pantalla un espacio en blanco
def my_function(x, /):
    """Función que acepta solo un argumento posicional."""
    print(x)

my_function(3)  # Imprime 3