#14°Sin , / en realidad se le permite usar argumentos de palabras clave incluso si la función espera argumentos posicionales:
print(" ")#imprime en la pantalla un espacio en blanco
print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar
print(" ")#imprime en la pantalla un espacio en blanco
def my_function(x):
    """Función que acepta un argumento que puede ser posicional o de palabra clave."""
    print(x)

my_function(x=3)  # Imprime 3