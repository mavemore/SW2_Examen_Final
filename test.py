# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import src.cotizador as cot

class Test(unittest.TestCase):
	#Las pruebas para la funcion cuota basica
	def test_cotizador_A(self):
		self.assertEqual(0,cot.calcular_cuota_basica(35))

	def test_cotizador_B(self):
		self.assertEqual(30,cot.calcular_cuota_basica(0))

	def test_cotizador_C(self):
		self.assertEqual(60,cot.calcular_cuota_basica(1))

	def test_cotizador_D(self):
		self.assertEqual(90,cot.calcular_cuota_basica(2))

	def test_cotizador_E(self):
		self.assertEqual(100,cot.calcular_cuota_basica(3))

	def test_cotizador_F(self):
		self.assertEqual(120,cot.calcular_cuota_basica(4))

	def test_cotizador_G(self):
		self.assertEqual(cot.calcular_valores_adicionales(17,"mujer", "soltero",""),0)

	def test_cotizador_H(self):
		self.assertEqual(cot.calcular_valores_adicionales(18,"mujer", "casado",""),20)

	def test_cotizador_I(self):
		self.assertEqual(cot.calcular_valores_adicionales(18,"mujer", "soltero",""),10)

	def test_cotizador_J(self):
		self.assertEqual(cot.calcular_valores_adicionales(18,"hombre", "soltero",""),40)

	def test_cotizador_K(self):
		self.assertEqual(cot.calcular_valores_adicionales(41,"mujer", "soltero","osteoporosis"),35)

	def test_cotizador_L(self):
		self.assertEqual(cot.calcular_valores_adicionales(41,"hombre", "soltero","infarto"),50)

	def test_cotizador_M(self):
		self.assertEqual(cot.calcular_valores_adicionales(70,"mujer", "soltero","cancer"),60)

	def test_cotizador_N(self):
		self.assertEqual(cot.calcular_valores_adicionales(70,"hombre", "soltero","cancer"),50)

	def test_cotizador_O(self):
		self.assertEqual("Saludcita no opera en la ciudad ingresada.",cot.cotizar_seguro("",70,"hombre", "soltero","cancer",5))

	def test_cotizador_P(self):
		self.assertEqual("No se puede realizar una cotización para el valor ingresado de dependientes.",cot.cotizar_seguro("Guayaquil",70,"hombre", "soltero","cancer",50))

	def test_cotizador_Q(self):
		self.assertEqual("La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años.",cot.cotizar_seguro("Guayaquil",80,"hombre", "soltero","cancer",4))

	def test_cotizador_R(self):
		self.assertEqual("El valor calculado de su cotización es de 40.00",cot.cotizar_seguro("Guayaquil",18,"mujer", "soltero","cancer",0))
if __name__ == '__main__':
	unittest.main()