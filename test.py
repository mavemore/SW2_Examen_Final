# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import src.cotizador

class Test(unittest.TestCase):
	#Unit Tests para Calcular Cuota Basica
	def test_cotizador_1(self):
		resultado = src.cotizador.calcular_cuota_basica(0)
		self.assertEqual(resultado,30)
	def test_cotizador_2(self):
		resultado = src.cotizador.calcular_cuota_basica(1)
		self.assertEqual(resultado,60)
	def test_cotizador_3(self):
		resultado = src.cotizador.calcular_cuota_basica(2)
		self.assertEqual(resultado,90)
	def test_cotizador_4(self):
		resultado = src.cotizador.calcular_cuota_basica(3)
		self.assertEqual(resultado,100)
	def test_cotizador_5(self):
		resultado = src.cotizador.calcular_cuota_basica(4)
		self.assertEqual(resultado,120)

	#Unit Tests para Calcular Valores Adicionales
	def test_cotizador_6(self):
		resultado = src.cotizador.calcular_valores_adicionales(20, 'mujer', 'casado', '')
		self.assertEqual(resultado,20)
	def test_cotizador_7(self):
		resultado = src.cotizador.calcular_valores_adicionales(20, 'mujer', 'soltero', '')
		self.assertEqual(resultado,10)
	def test_cotizador_8(self):
		resultado = src.cotizador.calcular_valores_adicionales(20, 'hombre', 'casado', '')
		self.assertEqual(resultado,0)
	def test_cotizador_9(self):
		resultado = src.cotizador.calcular_valores_adicionales(20, 'hombre', 'soltero', '')
		self.assertEqual(resultado,40)
	def test_cotizador_10(self):
		resultado = src.cotizador.calcular_valores_adicionales(45, 'mujer', '', 'osteoporosis')
		self.assertEqual(resultado,35)
	def test_cotizador_11(self):
		resultado = src.cotizador.calcular_valores_adicionales(45, 'mujer', '', '')
		self.assertEqual(resultado,0)
	def test_cotizador_12(self):
		resultado = src.cotizador.calcular_valores_adicionales(45, 'hombre', '', 'infarto')
		self.assertEqual(resultado,50)
	def test_cotizador_13(self):
		resultado = src.cotizador.calcular_valores_adicionales(45, 'hombre', '', '')
		self.assertEqual(resultado,0)
	def test_cotizador_14(self):
		resultado = src.cotizador.calcular_valores_adicionales(65, 'hombre', '', 'cancer')
		self.assertEqual(resultado,50)
	def test_cotizador_15(self):
		resultado = src.cotizador.calcular_valores_adicionales(65, 'mujer', '', 'cancer')
		self.assertEqual(resultado,60)
	def test_cotizador_16(self):
		resultado = src.cotizador.calcular_valores_adicionales(65, 'hombre', '', 'diabetes')
		self.assertEqual(resultado,50)
	def test_cotizador_17(self):
		resultado = src.cotizador.calcular_valores_adicionales(65, 'mujer', '', 'diabetes')
		self.assertEqual(resultado,60)

	#Unit Tests para Cotizar Seguros
	def test_cotizador_18(self):
		resultado = src.cotizador.cotizar_seguro('Guayaquil', 20, 'mujer', 'casado', '', 1)
		self.assertEqual(resultado,"El valor calculado de su cotización es de 80.00")
	def test_cotizador_19(self):
		resultado = src.cotizador.cotizar_seguro('Guayaquil', 17, 'mujer', 'casado', '', 1)
		self.assertEqual(resultado,"La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años.")
	def test_cotizador_20(self):
		esperado = "Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud."
		resultado = src.cotizador.cotizar_seguro('Guayaquil', 20, 'mujer', 'casado', '', 5)
		self.assertEqual(resultado, esperado)
	def test_cotizador_21(self):
		resultado = src.cotizador.cotizar_seguro('Guayaquil', 20, 'mujer', 'casado', '', 10)
		self.assertEqual(resultado,"No se puede realizar una cotización para el valor ingresado de dependientes.")
	def test_cotizador_22(self):
		resultado = src.cotizador.cotizar_seguro('New York', 20, 'mujer', 'casado', '', 4)
		self.assertEqual(resultado,"Saludcita no opera en la ciudad ingresada.")

if __name__ == '__main__':
	unittest.main()