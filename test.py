# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import src.cotizador

class Test(unittest.TestCase):
	#Mujer soltera, 29 años, Guayaquil con infarto.
	def test_cotizador_1(self):
		cotizado = src.cotizador.cotizar_seguro('Guayaquil',29,'mujer','soltero','infarto',0)
		self.assertEqual(cotizado,"El valor calculado de su cotización es de 40.00")

	#Hombre soltera, 29 años, Guayaquil con infarto.
	def test_cotizador_1(self):
		cotizado = src.cotizador.cotizar_seguro('Guayaquil',29,'mujer','soltero','infarto',0)
		self.assertEqual(cotizado,"El valor calculado de su cotización es de 40.00")
		
if __name__ == '__main__':
	unittest.main()
