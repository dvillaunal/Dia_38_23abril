# Programación Orientada a Objetos (OOP) Python:

+ Reto de Hoy:
   >Programación Orientada a Objetos. Herencia.
   [Link de referencia](https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/)

+ __Protocolo:__
   Daniel Felipe Villa Rengifo
   Lenguaje Utilizado: Python
   Tema: Programación Orientada a Objetos. Herencia.
   Fuentes de referencias:
     1. https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/
     2. https://www.programiz.com/python-programming/inheritance

# Herencia Simple y Múltiple:

Cuando hablamos de clases hay una ventaja muy destacable que es la posibilidad de que un objeto perteneciente a una clase sea capaz de heredar los atributos y métodos de otra.

+ ## Herencia Simple:
   
   + La herencia simple tiene lugar cuando una clase hija hereda los atributos y métodos de una única clase padre.
   
   + Y si queremos que nuestra clase herede los atributos o   métodos de otra clase principal (contiene el             constructor ``__init__``)
      
      + __Sintaxis:__
         class NombreDeLaClase(ClasePadre):
            Declaraciones
    
    > Cuando creamos una clase hija no es necesario volver a incluir el constructor __Init__ si la clase padre o principal ya lo contiene.
  
### -> Clase Padre:
  
Para que sea posible la herencia de atributos y métodos de una clase, debe existir la superclase o clase principal de la cual la clase hija o secundaria va a heredar. Es decir, para que exista un hijo debe de existir un padre.
   
  > __Ejemplo:__
   Supongamos que nosotros heredamos algunas virtudes y defectos de nuestros padres. Ellos serían nuestras clases primarias, o base. Y nosotros seríamos la secundaria o hija.

 + ## Herencia Múltiple:

 Los casos de herencia múltiple (al menos en Python) se dan cuando una clase secundaria o hija hereda atributos y metodos de mas de una clase principal o padre. Basta con separar con una coma ambas principales a la hora de crear la clase secundaria
   
  
   __=>Sintaxis:__
  
       class NombreDeLaClase(clase_padre_1, clase_padre_1): 
            Declaraciones


* ### Nota:
   El método ``Super()`` devuelve la referencia de la clase base, lo que nos permite utilizar la referencia de la clase base en cualquier clase derivada.