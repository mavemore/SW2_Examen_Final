# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import src.cotizador

class Test(unittest.TestCase):
	#Probar cotizacion para hombres solteros entre 18 y 40 
	def test_cotizador_1(self):
		valor = src.cotizador.cotizar_seguro('Guayaquil','25', 'hombre','soltero','','0')
		self.assertEqual(valor,70)

    #Probar que no acepte edad menor a 18 anios
	def test_cotizador_2(self):
		valor = src.cotizador.cotizar_seguro('Guayaquil','15', 'hombre','soltero','','0')
		self.assertEqual(valor,30)

	#Probar cotizacion para mujer fertil etre 18 y 40 anios y soltera
	def test_cotizador_3(self):
		valor = src.cotizador.cotizar_seguro('Guayaquil','25', 'mujer','soltero','','0')
		self.assertEqual(valor,40)

	#Probar cotizacion para mujer fertil etre 18 y 40 anios y casada
	def test_cotizador_4(self):
		valor = src.cotizador.cotizar_seguro('Guayaquil','25', 'mujer','casado','','0')
		self.assertEqual(valor,50)

	#Probar cotizacion para mujer mayor a 40 anios menor a 60 con osteoporosis
	def test_cotizador_5(self):
		valor = src.cotizador.cotizar_seguro('Guayaquil','50', 'mujer','soltero','osteoporosis','0')
		self.assertEqual(valor,65)

	#Probar cotizacion para mujer mayor a 40 anios menor a 60 sin osteoporosis y con 2 hijos
	def test_cotizador_6(self):
		valor = src.cotizador.cotizar_seguro('Guayaquil','45', 'mujer','soltero','','2')
		self.assertEqual(valor,90)

	#Probar cotizacion para hombre mayor a 40 anios menor a 60 con infarto
	def test_cotizador_7(self):
		valor = src.cotizador.cotizar_seguro('Guayaquil','45', 'hombre','viudo','infarto','2')
		self.assertEqual(valor,140)

	#Probar cotizacion para hombre mayor a 40 anios menor a 60 sin infarto
	def test_cotizador_8(self):
		valor = src.cotizador.cotizar_seguro('Guayaquil','45', 'hombre','viudo','','2')
		self.assertEqual(valor,90)

	#Probar cotizacion para hombre mayor a 60 anios con cancer
	def test_cotizador_9(self):
		valor = src.cotizador.cotizar_seguro('Guayaquil','65', 'hombre','viudo','cancer','2')
		self.assertEqual(valor,140)

	#Probar cotizacion para mujer mayor a 60 anios con cancer
	def test_cotizador_10(self):
		valor = src.cotizador.cotizar_seguro('Guayaquil','45', 'mujer','viudo','cancer','2')
		self.assertEqual(valor,150)

	#Probar cotizacion para hombre o mujer conmayor a 60 aniosmayor a 40 anios sin cancer o deabetis
	def test_cotizador_11(self):
		valor = src.cotizador.cotizar_seguro('Guayaquil','65', 'hombre','viudo','infarto','0')
		self.assertEqual(valor,30)

if __name__ == '__main__':
	unittest.main()