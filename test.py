# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import src.cotizador as cot

class Test(unittest.TestCase):
	#Incluya una pequeña descripción de lo que se prueba.
	def test_cotizador_ID(self):
		self.assertEqual('','')

	def test_cotizar_seguro_1(self):
		valor = cot.cotizar_seguro("Guayaquil", 18, "mujer", "casado", "osteoporosis", 0)
		self.assertEqual(valor,'El valor calculado de su cotización es de 50.00')		


if __name__ == '__main__':
	unittest.main()