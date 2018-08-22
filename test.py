# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from src.cotizador import *

class Test(unittest.TestCase):

	#Verifica el valor de la cuota básica cuando no tiene dependientes(Soltero).
	def test_calcula_cuotabasica_0dep(self):
		self.assertEqual(30,calcular_cuota_basica(0))

	#Verifica el valor de la cuota básica cuando tiene 1 dependiente.
	def test_calcula_cuotabasica_1dep(self):
		self.assertEqual(60,calcular_cuota_basica(1))

	#Verifica el valor de la cuota básica cuando tiene 2 dependientes.
	def test_calcula_cuotabasica_2dep(self):
		self.assertEqual(90,calcular_cuota_basica(2))	

	#Verifica el valor de la cuota básica cuando tiene 3 dependientes.
	def test_calcula_cuotabasica_3dep(self):
		self.assertEqual(100,calcular_cuota_basica(3))	

	#Verifica el valor de la cuota básica cuando tiene 4 dependientes.
	def test_calcula_cuotabasica_4dep(self):
		self.assertEqual(120,calcular_cuota_basica(4))

	"""Verifica el valor adicional del asegurado cuando tiene 
	entre 18 y 40 años, es mujer y casada.
	"""
	def test_calcula_adicionales_1(self):
		self.assertEqual(20,calcular_valores_adicionales(21,"mujer","casado",""))

	"""Verifica el valor adicional del asegurado cuando tiene 
	entre 18 y 40 años, es mujer y soltera.
	"""
	def test_calcula_adicionales_2(self):
		self.assertEqual(10,calcular_valores_adicionales(21,"mujer","soltera",""))

	"""Verifica el valor adicional del asegurado cuando tiene 
	entre 18 y 40 años, es hombre y soltero.
	"""
	def test_calcula_adicionales_3(self):
		self.assertEqual(40,calcular_valores_adicionales(21,"hombre","soltero",""))

	"""Verifica el valor adicional del asegurado cuando tiene 
	entre 41 y 60 años, es mujer y tiene osteoporosis.
	"""
	def test_calcula_adicionales_4(self):
		self.assertEqual(35,calcular_valores_adicionales(45,"mujer","soltera","osteoporosis"))

	"""Verifica el valor adicional del asegurado cuando tiene 
	entre 41 y 60 años, es hombre y ha sufrido un infarto.
	"""
	def test_calcula_adicionales_5(self):
		self.assertEqual(50,calcular_valores_adicionales(45,"hombre","soltero","infarto"))

	"""Verifica el valor adicional del asegurado cuando es 
	mayor a 60 años, es hombre y tiene cancer.
	"""
	def test_calcula_adicionales_6(self):
		self.assertEqual(50,calcular_valores_adicionales(65,"hombre","soltero","cancer"))

	"""Verifica el valor adicional del asegurado cuando es 
	mayor a 60 años, es mujer y tiene diabetes.
	"""
	def test_calcula_adicionales_7(self):
		self.assertEqual(60,calcular_valores_adicionales(65,"mujer","soltero","diabetes"))


		"""Verifica el valor del seguro  cuando es 
	mayor a 60 años, es mujer, tiene diabetes, vive en Guayaquil y tres dependientes.
	"""
	def test_calcula_seguro_caso_0(self):
		self.assertEqual("El valor calculado de su cotización es de 160.00",cotizar_seguro("Guayaquil",65,"mujer","soltero","diabetes",3))
	
	"""Verifica el valor del seguro cuando es 
	mayor a 75 años.
	"""
	def test_calcula_seguro_caso_1(self):
		self.assertEqual("La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años.",cotizar_seguro("Guayaquil",80,"mujer","soltero","diabetes",3))
	
	"""Verifica el valor del seguro cuandos 
	tiene más de 4 dependientes.
	"""
	def test_calcula_seguro_caso_2(self):
		self.assertEqual("Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud.",cotizar_seguro("Guayaquil",65,"mujer","soltero","diabetes",5))
	
	"""Verifica el valor del seguro cuando 
	tiene más de 9 dependientes.
	"""
	def test_calcula_seguro_caso_3(self):
		self.assertEqual("No se puede realizar una cotización para el valor ingresado de dependientes.",cotizar_seguro("Guayaquil",65,"mujer","soltero","diabetes",10))
	
	"""Verifica el valor del seguro cuando 
	vive en Ambato.
	"""
	def test_calcula_seguro_caso_4(self):
		self.assertEqual("Saludcita no opera en la ciudad ingresada.",cotizar_seguro("Ambato",65,"mujer","soltero","diabetes",3))

if __name__ == '__main__':
	unittest.main()