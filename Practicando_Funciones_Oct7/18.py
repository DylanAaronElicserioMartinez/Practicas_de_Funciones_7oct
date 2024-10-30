#18°Pero al agregar *, / obtendrás un error si intentas enviar un argumento posicional:
print(" ")#imprime en la pantalla un espacio en blanco
print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar
print(" ")#imprime en la pantalla un espacio en blanco
def my_function(*, x):
    """Función que solo acepta argumentos de palabra clave, generando error si se usa posicional."""
    print(x)

# my_function(3)  # Esto generará un error