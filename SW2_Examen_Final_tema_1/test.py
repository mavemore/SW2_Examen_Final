# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from src.cotizador import *

class Test(unittest.TestCase):
	#Incluya una pequeña descripción de lo que se prueba.
	def test_cotizador_ID(self):
		self.assertEqual('','')

	def test_cotizador_0(self):
		self.assertEquals(calcular_cuota_basica(0),30)

	def test_cotizador_1(self):
		self.assertEquals(calcular_cuota_basica(1),60)

	def test_cotizador_2(self):
		self.assertEquals(calcular_cuota_basica(2),90)

	def test_cotizador_3(self):
		self.assertEquals(calcular_cuota_basica(3),100)

	def test_cotizador_4(self):
		self.assertEquals(calcular_cuota_basica(4),120)

	def test_cotizador_5(self):
		calculo = cotizar_seguro('Guayaquil',18,'hombre','soltero','',0)
		self.assertEquals('El valor calculado de su cotización es de 70.00',calculo )

	def test_cotizador_6(self):
		calculo = cotizar_seguro('Guayaquil',22,'hombre','soltero','',0)
		self.assertEqual('El valor calculado de su cotización es de 70.00', calculo)

	def test_cotizador_7(self):
		calculo = cotizar_seguro('Guayaquil',30,'hombre','casado','',5)
		self.assertEqual('Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud.', calculo)

	def test_cotizador_8(self):
		calculo = cotizar_seguro('Guayaquil',51,'hombre','soltero','infarto',0)
		self.assertEqual('El valor calculado de su cotización es de 80.00', calculo)

	def test_cotizador_9(self):
		calculo = cotizar_seguro('Guayaquil',70,'hombre','soltero','cancer',0)
		self.assertEqual('El valor calculado de su cotización es de 80.00', calculo)
		
	def test_cotizador_10(self):
		calculo = cotizar_seguro('Guayaquil',21,'mujer','casado','',0)
		self.assertEqual('El valor calculado de su cotización es de 50.00', calculo)

	def test_cotizador_11(self):
		calculo = cotizar_seguro('Guayaquil',21,'mujer','casado','',1)
		self.assertEqual('El valor calculado de su cotización es de 80.00', calculo)

	def test_cotizador_12(self):
		calculo = cotizar_seguro('Guayaquil',21,'mujer','casado','',2)
		self.assertEqual('El valor calculado de su cotización es de 110.00', calculo)

	def test_cotizador_13(self):
		calculo = cotizar_seguro('Guayaquil',21,'mujer','casado','',3)
		self.assertEqual('El valor calculado de su cotización es de 120.00', calculo)

	def test_cotizador_14(self):
		calculo = cotizar_seguro('Guayaquil',21,'mujer','casado','',4)
		self.assertEqual('El valor calculado de su cotización es de 140.00', calculo)

	def test_cotizador_15(self):
		calculo = cotizar_seguro('Guayaquil',21,'mujer','soltero','',0)
		self.assertEqual('El valor calculado de su cotización es de 40.00', calculo)

	def test_cotizador_16(self):
		calculo = cotizar_seguro('Guayaquil',50,'mujer','soltero','osteoporosis',0)
		self.assertEqual('El valor calculado de su cotización es de 65.00', calculo)

	def test_cotizador_17(self):
		calculo = cotizar_seguro('Guayaquil',60,'mujer','soltero','diabetes',0)
		self.assertEqual('El valor calculado de su cotización es de 30.00', calculo)

	def test_cotizador_18(self):
		calculo = cotizar_seguro('Guayaquil',76,'mujer','soltero','osteoporosis',0)
		self.assertEqual('La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años.', calculo)

	def test_cotizador_19(self):
		calculo = cotizar_seguro('Guayaquil',45,'mujer','casado','cancer',11)
		self.assertEqual('No se puede realizar una cotización para el valor ingresado de dependientes.', calculo)

	def test_cotizador_20(self):
		calculo = cotizar_seguro('Galapagos',18,'mujer','casado','',2)
		self.assertEqual('Saludcita no opera en la ciudad ingresada.', calculo)

if __name__ == '__main__':
	unittest.main()