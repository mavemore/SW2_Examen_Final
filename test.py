# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import src.cotizador

class Test(unittest.TestCase):
	#Mujer soltera, 29 años, Guayaquil con infarto y 0 dependientes.
	def test_cotizador_1(self):
		cotizado = src.cotizador.cotizar_seguro('Guayaquil',29,'mujer','soltero','infarto',0)
		self.assertEqual(cotizado,"El valor calculado de su cotización es de 40.00")

	#Hombre soltero, 55 años, Guayaquil con infarto y 3 dependientes.
	def test_cotizador_2(self):
		cotizado = src.cotizador.cotizar_seguro('Guayaquil',55,'hombre','soltero','infarto',3)
		self.assertEqual(cotizado,"El valor calculado de su cotización es de 150.00")

	#Hombre soltero, 23 años, Guayaquil con infarto y 1 dependiente.
	def test_cotizador_3(self):
		cotizado = src.cotizador.cotizar_seguro('Guayaquil',23,'hombre','soltero','infarto',1)
		self.assertEqual(cotizado,"El valor calculado de su cotización es de 100.00")

	#Mujer casada, 23 años, Guayaquil con infarto y 2 dependientes.
	def test_cotizador_4(self):
		cotizado = src.cotizador.cotizar_seguro('Guayaquil',23,'mujer','casado','infarto',2)
		self.assertEqual(cotizado,"El valor calculado de su cotización es de 110.00")

	#Mujer casada, 55 años, Guayaquil con osteoporosis y 4 dependientes.
	def test_cotizador_5(self):
		cotizado = src.cotizador.cotizar_seguro('Guayaquil',55,'mujer','casado','osteoporosis',4)
		self.assertEqual(cotizado,"El valor calculado de su cotización es de 155.00")

	#Mujer viuda, 70 años, Guayaquil con cancer y 0 dependientes.
	def test_cotizador_6(self):
		cotizado = src.cotizador.cotizar_seguro('Guayaquil',70,'mujer','viudo','cancer',0)
		self.assertEqual(cotizado,"El valor calculado de su cotización es de 90.00")

	#Hombre viudo, 70 años, Guayaquil con diabetes y 0 dependientes.
	def test_cotizador_7(self):
		cotizado = src.cotizador.cotizar_seguro('Guayaquil',70,'hombre','viudo','diabetes',0)
		self.assertEqual(cotizado,"El valor calculado de su cotización es de 80.00")

	#Ciudad no adecuada.
	def test_cotizador_8(self):
		cotizado = src.cotizador.cotizar_seguro('Manta',70,'hombre','viudo','diabetes',0)
		self.assertEqual(cotizado,"Saludcita no opera en la ciudad ingresada.")

	#Edad no adecuada.
	def test_cotizador_9(self):
		cotizado = src.cotizador.cotizar_seguro('Guayaquil',90,'hombre','viudo','diabetes',0)
		self.assertEqual(cotizado,"La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años.")

	#Dependientes entre 4 y 9.
	def test_cotizador_10(self):
		cotizado = src.cotizador.cotizar_seguro('Guayaquil',70,'hombre','viudo','diabetes',6)
		self.assertEqual(cotizado,"Solo se puede realizar la cotizacion para hasta 4 dependientes en linea. Por favor acerquese a la agencia y presente una solicitud.")

	#Dependientes mayor a 9.
	def test_cotizador_11(self):
		cotizado = src.cotizador.cotizar_seguro('Guayaquil',70,'hombre','viudo','diabetes',10)
		self.assertEqual(cotizado,"No se puede realizar una cotización para el valor ingresado de dependientes.")
		
if __name__ == '__main__':
	unittest.main()
