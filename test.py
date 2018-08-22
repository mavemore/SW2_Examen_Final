# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from src.cotizador import *

class Test(unittest.TestCase):
	"""Probar cuando la ciudad ingresada no es una 
	en las que opera la empresa."""
	def test_cotizador_1(self):
		resultado = cotizar_seguro('Riobamba', 18, 'mujer', 'soltero', 'diabetes', 4)
		self.assertEqual(resultado,'Saludcita no opera en la ciudad ingresada.')

	def test_cotizador_2(self):
		"""Probar cuando hay mas de 9 dependientes."""
		resultado = cotizar_seguro('Guayaquil', 18, 'mujer', 'soltero', 'diabetes', 10)
		self.assertEqual(resultado,'No se puede realizar una cotización para el valor ingresado de dependientes.')

	def test_cotizador_3(self):
		"""Probar cuando hay mas de 4 y menos de 10 ependientes."""
		resultado = cotizar_seguro('Guayaquil', 18, 'mujer', 'soltero', 'diabetes', 6)
		self.assertEqual(resultado,'Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud.')

	def test_cotizador_4(self):
		"""Probar cuando la edad es menor a 18."""
		resultado = cotizar_seguro('Guayaquil', 10, 'mujer', 'soltero', 'diabetes', 3)
		self.assertEqual(resultado,'La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años.')

	def test_cotizador_5(self):
		"""Probar mujer entre 18 y 40 anios casada"""
		resultado = cotizar_seguro('Guayaquil', 30, 'mujer', 'casado', 'diabetes', 0)
		self.assertEqual(resultado,'El valor calculado de su cotización es de 50.00')

	def test_cotizador_6(self):
		"""Probar mujer entre 18 y 40 anios soltera."""
		resultado = cotizar_seguro('Guayaquil', 30, 'mujer', 'soltero', 'diabetes', 0)
		self.assertEqual(resultado,'El valor calculado de su cotización es de 40.00')

	def test_cotizador_7(self):
		"""Probar hombre entre 18 y 40 anios soltero."""
		resultado = cotizar_seguro('Guayaquil', 30, 'hombre', 'soltero', 'diabetes', 0)
		self.assertEqual(resultado,'El valor calculado de su cotización es de 70.00')

	def test_cotizador_8(self):
		"""Probar mujer entre 40 y 60 anios soltera con osteoporosis."""
		resultado = cotizar_seguro('Guayaquil', 50, 'mujer', 'soltero', 'osteoporosis', 0)
		self.assertEqual(resultado,'El valor calculado de su cotización es de 65.00')

	def test_cotizador_9(self):
		"""Probar hombre entre 40 y 60 anios soltero con infarto."""
		resultado = cotizar_seguro('Guayaquil', 50, 'hombre', 'soltero', 'infarto', 0)
		self.assertEqual(resultado,'El valor calculado de su cotización es de 80.00')

	def test_cotizador_10(self):
		"""Probar mujer con mas de 60 anios con cancer"""
		resultado = cotizar_seguro('Guayaquil', 70, 'mujer', 'soltero', 'cancer', 0)
		self.assertEqual(resultado,'El valor calculado de su cotización es de 90.00')

	def test_cotizador_11(self):
		"""Probar hombre con mas de 60 anios con cancer y cero dependientes."""
		resultado = cotizar_seguro('Guayaquil', 70, 'hombre', 'soltero', 'cancer', 0)
		self.assertEqual(resultado,'El valor calculado de su cotización es de 80.00')

	def test_cotizador_12(self):
		"""Probar hombre con mas de 60 anios con cancer y 1 dependiente."""
		resultado = cotizar_seguro('Guayaquil', 70, 'hombre', 'soltero', 'cancer', 1)
		self.assertEqual(resultado,'El valor calculado de su cotización es de 110.00')

	def test_cotizador_13(self):
		"""Probar hombre con mas de 60 anios con cancer y 2 dependientes."""
		resultado = cotizar_seguro('Guayaquil', 70, 'hombre', 'soltero', 'cancer', 2)
		self.assertEqual(resultado,'El valor calculado de su cotización es de 140.00')

	def test_cotizador_14(self):
		"""Probar hombre con mas de 60 anios con cancer y 3 dependientes."""
		resultado = cotizar_seguro('Guayaquil', 70, 'hombre', 'soltero', 'cancer', 3)
		self.assertEqual(resultado,'El valor calculado de su cotización es de 150.00')

	def test_cotizador_15(self):
		"""Probar hombre con mas de 60 anios con cancer y 4 dependientes."""
		resultado = cotizar_seguro('Guayaquil', 70, 'hombre', 'soltero', 'cancer', 4)
		self.assertEqual(resultado,'El valor calculado de su cotización es de 170.00')


if __name__ == '__main__':
	unittest.main()

