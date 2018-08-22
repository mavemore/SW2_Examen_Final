# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from src.cotizador import *

class Test(unittest.TestCase):
	#Incluya una pequeña descripción de lo que se prueba.
	def test_cotizador_1(self):
		cuota = calcular_cuota_basica(32)
		self.assertEqual(0,cuota)

	def test_cotizador_2(self):
		cuota = calcular_cuota_basica(0)
		self.assertEqual(30,cuota)

	def test_cotizador_3(self):
		cuota = calcular_cuota_basica(1)
		self.assertEqual(60,cuota)

	def test_cotizador_4(self):
		cuota = calcular_cuota_basica(2)
		self.assertEqual(90,cuota)

	def test_cotizador_5(self):
		cuota = calcular_cuota_basica(3)
		self.assertEqual(100,cuota)

	def test_cotizador_6(self):
		cuota = calcular_cuota_basica(4)
		self.assertEqual(120,cuota)

	def test_cotizador_7(self):
		valor_adicional = calcular_valores_adicionales(17,"mujer", "soltero","")
		self.assertEqual(0,valor_adicional)

	def test_cotizador_8(self):
		valor_adicional = calcular_valores_adicionales(18,"mujer", "casado","")
		self.assertEqual(20,valor_adicional)

	def test_cotizador_9(self):
		valor_adicional = calcular_valores_adicionales(18,"mujer", "soltero","")
		self.assertEqual(10,valor_adicional)

	def test_cotizador_10(self):
		valor_adicional = calcular_valores_adicionales(18,"hombre", "soltero","")
		self.assertEqual(40,valor_adicional)

	def test_cotizador_11(self):
		valor_adicional = calcular_valores_adicionales(41,"mujer", "soltero","osteoporosis")
		self.assertEqual(35,valor_adicional)

	def test_cotizador_12(self):
		valor_adicional = calcular_valores_adicionales(41,"hombre", "soltero","infarto")
		self.assertEqual(50,valor_adicional)

	def test_cotizador_13(self):
		valor_adicional = calcular_valores_adicionales(70,"mujer", "soltero","cancer")
		self.assertEqual(60,valor_adicional)

	def test_cotizador_14(self):
		valor_adicional = calcular_valores_adicionales(70,"hombre", "soltero","cancer")
		self.assertEqual(50,valor_adicional)

	def test_cotizador_15(self):
		seguro = cotizar_seguro("Guayaquil"70,"hombre", "soltero","cancer",1)
		self.assertEqual(50,seguro)


if __name__ == '__main__':
	unittest.main()