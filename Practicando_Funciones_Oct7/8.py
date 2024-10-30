#8°Argumentos arbitrarios de palabras clave, **kwargs
#Si no sabe cuántos argumentos de palabras clave se pasarán a su función, agregue dos asteriscos: ** antes del nombre del parámetro en la definición de la función.
#De esta manera, la función recibirá un diccionario de argumentos y podrá acceder a los elementos en consecuencia:
#Si se desconoce el número de argumentos de palabras clave, agregue un doble ** antes del nombre del parámetro:
print(" ")#imprime en la pantalla un espacio en blanco
print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar
print(" ")#imprime en la pantalla un espacio en blanco
def f(**niño):#definimos la funcion f que seria niño pero agregamos 2* para conocer el numero del argumento.
  print("El niño más pequeño es: " + niño["lname"])#imprimimos la funcion f que seria el texto dentro de " " y tambien el argumento niño mas otro argumento que sea considerado como su nombre
f(fname = "Tobias", lname = "Bruno")#imprimimos la funcion f y tambien el argumento Bruno porque anterior mente fue seleccionado
