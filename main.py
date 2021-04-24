'''
   Daniel Felipe Villa Rengifo
   Lenguaje Utilizado: Python
   Tema: Programación Orientada a Objetos. Herencia.
   Fuentes de referencias:
     1. https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/
     2. https://www.programiz.com/python-programming/inheritance
'''

# Ejemplo 1:
print('------------------------------------------------------')
print('\n# Ejemplo 1:')

# Herecia Simple:
print('\n# Herecia Simple:')

'''
Vamos a proceder a crear dos clases,
una principal y una secundaria,
en esta última vamos a agregar la función de
presentarse accediendo a los atributos de la clase padre.

-> Literalmente Haremos un ejemplo de persona y procedencia:
     hablando de castas: (parafraseo: Linaje de una persona)
'''

## Definimos una clase:
print('\n## Definimos una clase:')

class Persona(object):
  '''
  Aqui se definen: (Atributos)
  1. Nombre de la persona
  2. Apellido (Atributo Importante en ejemplo)
  '''
  def __init__(self, nombre, apellido):
    '''
    Con en metodo constructor __init__
    definiremos los atributos:
      Nombre y Apellido
    '''
    self.nombre = nombre
    self.apellido = apellido

## Definimos una segunda clase:
print('\n## Definimos una segunda clase:')
print('\m# Definimos la lista de linaje:')
linajes_lista = ['Vega', 'Velarde', 'Barreda', 'Polanco', 'Villa', 'Velasco', 'Fernández', 'Villegas', 'Dávila', 'Enríquez', 'Gutiérrez', 'Guzmán', 'Meneses', 'Fierro', 'Miranda', 'Morenilla', 'Torres', 'Valencia', 'Vargas', 'Vélez', 'Zúñiga', 'Cossío']
print(linajes_lista)

class Casta(Persona): # Entre parentesis definimos la clase Padre o principal
  # Lo que conviete a Casta en una clase hija o secundaria
  '''
  en esta clase llamamos a la principal,
  la cual almacena nuestros datos
  el principal es apellido,
  en el cual especificara la casta de la persona en cuestión.
  (Solo definiremos algunos apellidos correspondientes a
  los colonos (Nobles) o sangre española "Conquistadores de america")
  '''
  def linaje(self):
    '''
    Recorremos una muestra de algunos nombres antiguamente
    nobles españoles y colonos, para ver si es de familia de casta noble,
    sino solo imprimira el nombre y su apellido
    '''
    # Definimos la lista de linaje:
    linajes_lista = ['Vega', 'Velarde', 'Barreda', 'Polanco', 'Villa', 'Velasco', 'Fernández', 'Villegas', 'Dávila', 'Enríquez', 'Gutiérrez', 'Guzmán', 'Meneses', 'Fierro', 'Miranda', 'Morenilla', 'Torres', 'Valencia', 'Vargas', 'Vélez', 'Zúñiga', 'Cossío']
    for i in linajes_lista:
      if i == self.apellido:
        print(f'Mi nombre es {self.nombre} y gracias a que mi apellido es {self.apellido} pertenezco a la casta noble o colona española antigua.')
        break
    else:
      print(f'Mi nombre es {self.nombre} y mi apellido es {self.apellido}')

## Definimos el nombre y apellido del usuario:
nom = input('Ingrese su Primer o Segundo Nombre (Primer letra en mayuscula)')
ap = input('Ingrese su Primer o Segundo Apellido (Primer letra en mayuscula)')

## Ingresamos los valores a la clase padre:
print('\n## Ingresamos los siguiente valores a la clase padre:')
print('\n')
print('Primer o Segundo Nombre: ', nom)
print('\n')
print('Primer o Segundo Apellido: ', ap)

user = Casta(nom, ap)
print(f"user = Casta({nom}, {ap})")

## Miramos el resultado en la clase hija (Casta):
print('## Miramos el resultado en la clase hija (Casta):')
user.linaje()

'''
Cómo ves asignamos al objeto “user” la clase “Casta”
que hereda los atributos de “Persona”.
De lo contrario obtendremos un error porque los atributos
nombre y edad pertenecen a Persona.
'''

# Fin del Ejemplo:
print('# Fin del Ejemplo:')
print('------------------------------------------------------')


# Ejemplo 2:
print('------------------------------------------------------')
print('# Ejemplo 2:')

'''
El método Super()
devuelve la referencia de la clase base,
lo que nos permite utilizar la referencia de
la clase base en cualquier clase derivada.

El ejemplo se base en Guardar una cuenta de ahorros
y como esta va generando intereses

'''
## Definimos una clase:
print('## Definimos una clase:')
print('class Cuenta:')
print('Saldo = 0')

class Cuenta:
  '''
  Esta clase cuenta con 3 metodos:
  1. definir saldo
  2. Definir consulta de saldo
  3. Definir Retiros
  4. consignaciones
  ademas cuenta con un atributo = Saldo
  '''
  saldo = 0 # Saldo de la cuenta de ahorros

  # Definimos los metodos:

  def __init__(self, saldo):
    '''
    Aqui definiremos el saldo como un metodo
    para llamarlo e ir agregando a el consignaciones
    '''
    self.saldo
  
  def consulta_saldo(self):
    '''
    Aqui se define el saldo actual de la cuenta
    '''
    print(f'Saldo Actual: {self.saldo}')
  
  def consignacion(self, deposito):
    '''
    en este metodo vamos agregando saldo cada vez
    que llamemos a deposito (dentro de consignacion)
    '''
    self.saldo += deposito
    c = [randint(0,x) for x in range(9)]
    comprobante = "".join(c)
    print(f'{deposito} Consignación exitosa, Tu comprobante es {comprobante}')
  
  def retiro(sef, resta):
    '''
    En este metodo se vamos sustrayendo
    de la cuenta dde ahorros,
    cada vez que el usuario quiera extraer
    un monto especifico (numero entero preferiblemente)
    '''
    cuenta_ahorro
    if resta > self.saldo:

      print(f'Saldo insuficiente = {saldo}, Intente nuevamente')
      return
    
    self.Saldo -= resta # Si lo que saco es menor o igual al saldo, imprimira que el retiro fue exitoso
    print(f'Retiro de {resta} exitoso, !Vuelva pronto¡')

## Definimos una clase hija:
print('## Definimos una clase hija:')

class S_Cuenta(Cuenta):
  '''
  En esta clse definiremos dos metodos
  uno dodne se utlice super()
  y el segundo, son los intereses de tu cuenta
  
  El interes del banco, par alos poseedores de cuentas de ahorros,
  el porocentaje es de 7.5%
  '''
  tarifa = 7.5

  def __init__(self, saldo):
    '''
    Devolera la referencia de la clase padre = (Cuenta)

    '''
    super().__init__(saldo)

  def interes(self, m):
    '''
    Aqui definimos el interes que la cuenta genera con la formula, 
    añadiendolo a el P.A.P.A del SIA
    '''
    print("Interes = %.2f" %(self.saldo * (self.saldo * (self.tarifa/100) * m)))

## Imprimimos los resultado:
print('## Imprimimos los resultado:')

cuenta_ahorro = S_Cuenta(1000)
cuenta_ahorro.retiro(400)
cuenta_ahorro.consulta_saldo()
cuenta_ahorro.interes(4.3)
# Fin del mett