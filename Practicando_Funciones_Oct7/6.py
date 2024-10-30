#6°Si no sabe cuántos argumentos se pasarán a su función, agregue un * antes del nombre del parámetro en la definición de la función.
#De esta manera, la función recibirá una tupla de argumentos y podrá acceder a los elementos en consecuencia:
#Si se desconoce el número de argumentos, agregue un * antes del nombre del parámetro
print(" ")#imprime en la pantalla un espacio en blanco
print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar
print(" ")#imprime en la pantalla un espacio en blanco
def f(*niños):#definimos la funcion f "niños"
  print("El niño más pequeño es: " + niños[2])#imprimimos en pantalla la funcion f que seria el texto dentro de print mas que tambien imprimimos el 2do valor que seria linux por que se empieza en 0 como son 3 valores seria 0, 1, 2.
f("Emil", "Tobias", "Linus")#imprimimos la funcion f pero como antes especificamos el valor o tupla solo se imprimira ese.