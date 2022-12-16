def sumar_tres_numeros(num1, num2, num3):
  resultado = num1 + num2 + num3
  return resultado


# Llamamos a la función y le pasamos tres números como argumentos
resultado = sumar_tres_numeros(1, 2, 3)

# Imprimimos el resultado
print(resultado)


###        PARTE DOS        ####


class Coche:
  def __init__(self, num_puertas):
    self.num_puertas = num_puertas

  def agregar_puerta(self):
    self.num_puertas += 1

# Creamos un objeto de la clase Coche con 2 puertas
miCoche = Coche(2)

# Añadimos una puerta al coche
miCoche.agregar_puerta()

# Imprimimos el número de puertas del coche
print(miCoche.num_puertas)