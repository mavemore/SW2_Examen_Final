# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import src.cotizador as cot

class Test(unittest.TestCase):
	#Incluya una pequeña descripción de lo que se prueba.
	def test_cotizador_ID(self):
		self.assertEqual('','')

	def test_cotizar_seguro_ciudad_valida(self):
		valor = cot.cotizar_seguro("Guayaquil", 18, "mujer", "casado", "osteoporosis", 0)
		self.assertEqual(valor,'El valor calculado de su cotización es de 50.00')		

	def test_cotizar_seguro_ciudad_no_valida(self):
		valor = cot.cotizar_seguro("Esmeraldas", 18, "mujer", "casado", "osteoporosis", 0)
		self.assertEqual(valor,'Saludcita no opera en la ciudad ingresada.')

	def test_cotizar_seguro_dependientes_fuera_rango(self):
		valor = cot.cotizar_seguro("Guayaquil", 18, "mujer", "casado", "osteoporosis", 10)
		self.assertEqual(valor,'No se puede realizar una cotización para el valor ingresado de dependientes.')

	def test_cotizar_seguro_dependientes_excedentes(self):
		valor = cot.cotizar_seguro("Guayaquil", 18, "mujer", "casado", "osteoporosis", 9)
		self.assertEqual(valor,'Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud.')

	def test_cotizar_seguro_dependientes_sin_dependientes(self):
		valor = cot.cotizar_seguro("Guayaquil", 18, "mujer", "casado", "osteoporosis", 0)
		self.assertEqual(valor,'El valor calculado de su cotización es de 50.00')

	def test_cotizar_seguro_dependientes_1_dependiente(self):
		valor = cot.cotizar_seguro("Guayaquil", 18, "mujer", "casado", "osteoporosis", 1)
		self.assertEqual(valor,'El valor calculado de su cotización es de 80.00')

	def test_cotizar_seguro_dependientes_2_dependiente(self):
		valor = cot.cotizar_seguro("Guayaquil", 18, "mujer", "casado", "osteoporosis", 2)
		self.assertEqual(valor,'El valor calculado de su cotización es de 110.00')

	def test_cotizar_seguro_dependientes_3_dependiente(self):
		valor = cot.cotizar_seguro("Guayaquil", 18, "mujer", "casado", "osteoporosis", 3)
		self.assertEqual(valor,'El valor calculado de su cotización es de 120.00')

	def test_cotizar_seguro_dependientes_4_dependiente(self):
		valor = cot.cotizar_seguro("Guayaquil", 18, "mujer", "casado", "osteoporosis", 4)
		self.assertEqual(valor,'El valor calculado de su cotización es de 140.00')

	def test_cotizar_seguro_edad_fuera_rango(self):
		valor = cot.cotizar_seguro("Guayaquil", 0, "mujer", "casado", "osteoporosis", 0)
		self.assertEqual(valor,'La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años.')


if __name__ == '__main__':
	unittest.main()