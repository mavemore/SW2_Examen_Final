# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import src.cotizador as cot

class Test(unittest.TestCase):
	#Incluya una pequeña descripción de lo que se prueba.
	def test_cotizador_ID(self):
		self.assertEqual('','')

	def test1(self):
		respuesta = cot.cotizar_seguro('Guayaquil',19,'mujer','casado','',0)
		self.assertEqual('El valor calculado de su cotización es de 50.00', respuesta)

	def test2(self):
		respuesta = cot.cotizar_seguro('Guayaquil',19,'mujer','casado','',1)
		self.assertEqual('El valor calculado de su cotización es de 80.00', respuesta)

	def test3(self):
		respuesta = cot.cotizar_seguro('Guayaquil',19,'mujer','casado','',2)
		self.assertEqual('El valor calculado de su cotización es de 110.00', respuesta)

	def test4(self):
		respuesta = cot.cotizar_seguro('Guayaquil',19,'mujer','casado','',3)
		self.assertEqual('El valor calculado de su cotización es de 120.00', respuesta)

	def test5(self):
		respuesta = cot.cotizar_seguro('Guayaquil',19,'mujer','casado','',4)
		self.assertEqual('El valor calculado de su cotización es de 140.00', respuesta)

	def test6(self):
		respuesta = cot.cotizar_seguro('Guayaquil',20,'mujer','soltero','',0)
		self.assertEqual('El valor calculado de su cotización es de 40.00', respuesta)

	def test7(self):
		respuesta = cot.cotizar_seguro('Guayaquil',21,'hombre','soltero','',0)
		self.assertEqual('El valor calculado de su cotización es de 70.00', respuesta)

	def test8(self):
		respuesta = cot.cotizar_seguro('Guayaquil',50,'mujer','soltero','osteoporosis',0)
		self.assertEqual('El valor calculado de su cotización es de 65.00', respuesta)

	def test9(self):
		respuesta = cot.cotizar_seguro('Guayaquil',50,'hombre','soltero','infarto',0)
		self.assertEqual('El valor calculado de su cotización es de 80.00', respuesta)

	def test10(self):
		respuesta = cot.cotizar_seguro('Guayaquil',70,'mujer','soltero','diabetes',0)
		self.assertEqual('El valor calculado de su cotización es de 90.00', respuesta)

	def test11(self):
		respuesta = cot.cotizar_seguro('Guayaquil',70,'hombre','soltero','cancer',0)
		self.assertEqual('El valor calculado de su cotización es de 80.00', respuesta)

	def test12(self):
		respuesta = cot.cotizar_seguro('Guayaquil',85,'mujer','soltero','diabetes',0)
		self.assertEqual('La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años.', respuesta)

	def test13(self):
		respuesta = cot.cotizar_seguro('Guayaquil',25,'hombre','casado','',6)
		self.assertEqual('Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud.', respuesta)

	def test14(self):
		respuesta = cot.cotizar_seguro('Guayaquil',45,'mujer','casado','cancer',11)
		self.assertEqual('No se puede realizar una cotización para el valor ingresado de dependientes.', respuesta)

	def test15(self):
		respuesta = cot.cotizar_seguro('Esmeraldas',24,'mujer','casado','',1)
		self.assertEqual('Saludcita no opera en la ciudad ingresada.', respuesta)


if __name__ == '__main__':
	unittest.main()