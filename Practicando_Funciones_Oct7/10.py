#10°Pasar una lista como argumento Puede enviar cualquier tipo de argumento de datos a una función (cadena, número, lista, diccionario, etc.) y será tratado como el mismo tipo de datos dentro de la función.
print(" ")#imprime en la pantalla un espacio en blanco
print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar
print(" ")#imprime en la pantalla un espacio en blanco
def f(food):
    #imprime cada elemento de la lista pasado como argumento
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
f(fruits)