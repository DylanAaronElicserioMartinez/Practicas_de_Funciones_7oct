#15°Pero al agregar , / obtendrá un error si intenta enviar un argumento de palabra clave:
print(" ")#imprime en la pantalla un espacio en blanco
print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar
print(" ")#imprime en la pantalla un espacio en blanco
def my_function(x, /):
    """Función que acepta solo un argumento posicional, generando error si se usa palabra clave."""
    print(x)

# my_function(x=3)  # Esto generará un error
