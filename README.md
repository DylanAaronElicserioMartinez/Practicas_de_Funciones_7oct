# Practicas_de_Funciones_7oct
Practicas

#Codigo 1 y 2

#1°En Python una funcion es definida usando la palabra def como palabra clave

#2°Para llamar a una funcion, use la funcion nombrada y seguida de parentesis

print(" ")#imprime en la pantalla un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar

print(" ")#imprime en la pantalla un espacio en blanco

n = input("Ingresa Cual quier cosa a imprimir:")#le ponemos un valor a n con la funcion input

def f(n):#definimos una funcion que seria f

    print(n)#ingresamos el valor n a imprimir a la funcion definida
    
f(n)#imprimimos la funcion f 

![image](https://github.com/user-attachments/assets/3197c567-6e4b-4b11-8c48-6ddbbd2cc77c)

![image](https://github.com/user-attachments/assets/0b1ffbcb-b2ff-4a71-9228-2fc73e05a84b)

#Codigo 3

#3°El siguiente ejemplo tiene una función con un argumento (fname). Cuando se llama a la función, pasamos un nombre, que se usa dentro de la función para imprimir el nombre completo

print(" ")#imprime en la pantalla un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar

print(" ")#imprime en la pantalla un espacio en blanco

fname=input("ingresa tu nombre o lo que sea:")#le ponemos un valor a fname con la funcion input

def f():#definimos una funcion que seria f

  print(fname + " Refsnes")#ingresamos el valor fname a imprimir a la funcion definida
  
f()#imprimimos la funcion f 

![image](https://github.com/user-attachments/assets/3d4eccff-c9f1-4864-ab6d-70120f404a1c)

![image](https://github.com/user-attachments/assets/d64a3ade-a2bc-4bb9-9bb1-79d6995c76fa)

#Codigo 4

#4°De forma predeterminada, se debe llamar a una función con la cantidad correcta de argumentos. Lo que significa que si su función espera 2 argumentos, debe llamar a la función con 2 argumentos, ni más ni menos.

print(" ")#imprime en la pantalla un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar

print(" ")#imprime en la pantalla un espacio en blanco

def f(fname, lname):#definimos una funcion que seria f

  print(fname + " " + lname)#ingresamos el valor fname a imprimir a la funcion definida
  
f("Emil", "Refsnes")#imprimimos la funcion f como tiene los 2 argumentos a pedir si funcionara el programa

![image](https://github.com/user-attachments/assets/c2fcf9f5-d0f4-466e-8144-435c2ccf93c7)

![image](https://github.com/user-attachments/assets/1dd8e8f1-f1bb-4e7d-8e86-39a6f7216ab8)

#Codigo 5

#5° Esta función espera 2 argumentos, pero solo obtiene 1

print(" ")#imprime en la pantalla un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar

print(" ")#imprime en la pantalla un espacio en blanco

def f(fname, lname):#definimos una funcion que seria f

  print(fname + " " + lname)#ingresamos el valor fname a imprimir a la funcion definida
  
f("Emil")#imprimimos la funcion f aunque como aqui falta un argumento saldra error

![image](https://github.com/user-attachments/assets/b516841c-ab11-44c0-997b-9c49446ea237)

![image](https://github.com/user-attachments/assets/e3648482-7c31-4fbc-9731-ad7add1ce1f4)

#Codigo 6

#6°Si no sabe cuántos argumentos se pasarán a su función, agregue un * antes del nombre del parámetro en la definición de la función.

#De esta manera, la función recibirá una tupla de argumentos y podrá acceder a los elementos en consecuencia:

#Si se desconoce el número de argumentos, agregue un * antes del nombre del parámetro

print(" ")#imprime en la pantalla un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar

print(" ")#imprime en la pantalla un espacio en blanco

def f(*niños):#definimos la funcion f "niños"

  print("El niño más pequeño es: " + niños[2])#imprimimos en pantalla la funcion f que seria el texto dentro de print mas que tambien imprimimos el 2do valor que seria linux por que se empieza en 0 como son 3 valores
  seria 0, 1, 2.
  
f("Emil", "Tobias", "Linus")#imprimimos la funcion f pero como antes especificamos el valor o tupla solo se imprimira ese.

![image](https://github.com/user-attachments/assets/829afb1c-f2d8-4199-ac73-28fd45594758)

![image](https://github.com/user-attachments/assets/0d585ab9-8da3-4479-b0c4-13bab7482220)

#Codigo 7

#7°También puede enviar argumentos con la sintaxis clave = valor.De esta forma no importa el orden de los argumentos.

print(" ")#imprime en la pantalla un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar

print(" ")#imprime en la pantalla un espacio en blanco

def f(child3, child2, child1):#definimos la funcion f que seria child1,child2,child3

  print("El niño más pequeño es: " + child3)#imprimimos en pantalla el texto que esta dentro de " " y tambien se impriume el argumento seleccionado que seria child3 
  
f(child1 = "Emil", child2 = "Tobias", child3 = "Linus")#imprimimos la funcion f pero como antes especificamos el valor o tupla solo se imprimira ese.

![image](https://github.com/user-attachments/assets/4fd92774-4507-4cb6-beec-85159ff69ed0)

![image](https://github.com/user-attachments/assets/e74efb70-5275-484c-a07a-69301e7df3e6)

#Codigo 8

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

![image](https://github.com/user-attachments/assets/3f45d624-6701-46d5-9f14-c391d83a705e)

![image](https://github.com/user-attachments/assets/02d9b646-35fc-465c-96cd-22089fc3fa6e)

#Codigo 9

#9°Valor de parámetro predeterminado

#El siguiente ejemplo muestra cómo utilizar un valor de parámetro predeterminado.

#Si llamamos a la función sin argumento, usa el valor predeterminado:

print(" ")#imprime en la pantalla un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar

print(" ")#imprime en la pantalla un espacio en blanco

p=input("ingresa por favor de donde eres (país):")#le ponemos un valor a n con la funcion input

def f():#definimos la funcion f

  print("yo soy de " + p )#imprimimos la funcion f que seria el texto dentro de " " y tambien el valor p
  
f()#imprimimos la funcion f y tambien el valor de p

f("Brazil")#no se imprime porque esta lleno

f("Pakistan")#no se imprime porque esta lleno

f("Iran")#no se imprime porque esta lleno

![image](https://github.com/user-attachments/assets/34f0fd02-09ed-49b5-a113-6febad867e19)

![image](https://github.com/user-attachments/assets/7d46a94e-401e-4ce7-9541-1906e2e96f09)

#Codigo 10

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

![image](https://github.com/user-attachments/assets/a51cfb70-fa89-483a-aa27-df7be9f830c4)

![image](https://github.com/user-attachments/assets/d0d16195-abfb-421b-9fd1-ffff5a063ea8)

#Codigo 11

#11°Regresa Valores Para permitir que una función devuelva un valor, utilice la declaración de retorno:

print(" ")#imprime en la pantalla un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar

print(" ")#imprime en la pantalla un espacio en blanco

def my_function(x):

    """Devuelve el valor recibido como argumento."""
    
    return x

print(my_function(3))  # Imprime 3

print(my_function(5))  # Imprime 5

print(my_function(9))  # Imprime 9

![image](https://github.com/user-attachments/assets/cc825336-a92f-44f5-8827-b341ba58d5fa)

![image](https://github.com/user-attachments/assets/5b4af087-3cf8-486d-8b18-6f2c0bdfad83)

#Codigo 12

#12°La declaración del pass Las definiciones de función no pueden estar vacías, pero si por alguna razón tiene una definición de función sin contenido, ingrese la instrucción pass para evitar recibir un error.

print(" ")#imprime en la pantalla un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar

print(" ")#imprime en la pantalla un espacio en blanco

def myfunction():

    """Función vacía que evita un error usando pass."""
    
    pass

![image](https://github.com/user-attachments/assets/a1f11332-f0a5-4c14-b022-8986f853414b)

![image](https://github.com/user-attachments/assets/addec019-979f-4fbe-a893-0d7b5992b735)

#Codigo 13

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

![image](https://github.com/user-attachments/assets/e4730f32-980c-463f-ad06-aaca13f76cf5)

![image](https://github.com/user-attachments/assets/767dddbf-d49e-4dc8-9c6f-f26b114d6f9c)

#Codigo 14

#14°Sin , / en realidad se le permite usar argumentos de palabras clave incluso si la función espera argumentos posicionales:

print(" ")#imprime en la pantalla un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar

print(" ")#imprime en la pantalla un espacio en blanco

def my_function(x):

    """Función que acepta un argumento que puede ser posicional o de palabra clave."""
    
    print(x)

my_function(x=3)  # Imprime 3

![image](https://github.com/user-attachments/assets/54d8fafa-443e-482b-a85b-1c4a398a5213)

![image](https://github.com/user-attachments/assets/e19d4d6d-fbd7-4933-923c-8c3b0f2bb2e9)

#Codigo 15

#15°Pero al agregar , / obtendrá un error si intenta enviar un argumento de palabra clave:

print(" ")#imprime en la pantalla un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar

print(" ")#imprime en la pantalla un espacio en blanco

def my_function(x, /):

    """Función que acepta solo un argumento posicional, generando error si se usa palabra clave."""
    
    print(x)

# my_function(x=3)  # Esto generará un error

![image](https://github.com/user-attachments/assets/808ca405-4fa6-48b8-b244-d0d0c8db889a)

![image](https://github.com/user-attachments/assets/0ac83701-e7cb-4892-840d-68e6ce7e5978)

#Codigo 16

#16°Argumentos de solo palabras clave Para especificar que una función solo puede tener argumentos de palabras clave, agregue *, antes de los argumentos:

print(" ")#imprime en la pantalla un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar

print(" ")#imprime en la pantalla un espacio en blanco

def my_function(*, x):

    """Función que acepta solo argumentos de palabra clave."""
    
    print(x)

my_function(x=3)  # Imprime 3

![image](https://github.com/user-attachments/assets/b7342e50-a2e6-4cf0-a99a-e563ab1a1f76)

![image](https://github.com/user-attachments/assets/c7e495b1-f524-47a7-b70f-b9d5c87fa971)

#Codigo 17

#17°Sin el *, se le permite utilizar argumentos posicionales incluso si la función espera argumentos de palabras clave:

print(" ")#imprime en la pantalla un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar

print(" ")#imprime en la pantalla un espacio en blanco

def my_function(x):

    """Función que acepta un argumento posicional."""
    
    print(x)

my_function(3)  # Imprime 3

![image](https://github.com/user-attachments/assets/9e7f0cec-25cd-4feb-b065-3fea5709f9fd)

![image](https://github.com/user-attachments/assets/b4ea39b9-e4b5-4f21-8419-91564d0f3156)

#Codigo 18

#18°Pero al agregar *, / obtendrás un error si intentas enviar un argumento posicional:

print(" ")#imprime en la pantalla un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar

print(" ")#imprime en la pantalla un espacio en blanco

def my_function(*, x):

    """Función que solo acepta argumentos de palabra clave, generando error si se usa posicional."""
    
    print(x)

# my_function(3)  # Esto generará un error

![image](https://github.com/user-attachments/assets/672f719d-71bb-4284-b449-8759a6dd66ea)

![image](https://github.com/user-attachments/assets/63c6f663-d0b5-41a9-a64c-a88e24e66e1e)

#Codigo 19

#19°Combine solo posicional y solo palabras clave Puede combinar los dos tipos de argumentos en la misma función.

#Cualquier argumento antes de / es solo posicional y cualquier argumento después de * es solo de palabra clave.

print(" ")#imprime en la pantalla un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar

print(" ")#imprime en la pantalla un espacio en blanco

def my_function(a, b, /, *, c, d):

    """Función que combina argumentos posicionales y de palabra clave."""
    
    print(a + b + c + d)

my_function(5, 6, c=7, d=8)  # Imprime 26

![image](https://github.com/user-attachments/assets/5c9af182-b68b-4dae-8ccd-f7f3ecfabb0d)

![image](https://github.com/user-attachments/assets/d156a5bf-c716-4b91-bd6b-a7744492d129)

#Codigo 20

#20°Mucho texto.

print(" ")#imprime en la pantalla un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime en la pantallada mi nombre completo mi semestre y grupo y mi control escolar

print(" ")#imprime en la pantalla un espacio en blanco

def tri_recursion(k):

    """Función recursiva que calcula la suma de números desde k hasta 1."""
    
    if k > 0:
    
        result = k + tri_recursion(k - 1)
        
        print(result)
        
    else:
    
        result = 0
        
    return result

print("\n\nRecursion Example Results")

tri_recursion(6)

![image](https://github.com/user-attachments/assets/abe4c86b-2e8d-4cca-a370-0d0628e955fb)

![image](https://github.com/user-attachments/assets/884f9f78-36ee-4d89-9734-67cb7841e7ff)
