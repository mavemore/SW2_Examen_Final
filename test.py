# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from src.cotizador import *

class Test(unittest.TestCase):
	#Incluya una pequeña descripción de lo que se prueba.
	def test_cotizador_ID(self):
		self.assertEqual('','')

	def test_calcular_cuota_0(self):
		"""Calcula la cuota basica del asegurado, 
	sin dependientes. 
	"""
		dependientes = 0
		cuota = calcular_cuota_basica(dependientes)
		self.assertEqual(cuota,30)

	def test_calcular_cuota_1(self):
		"""Calcula la cuota basica del asegurado, 
	con 1 dependiente. 
	"""
		dependientes = 1
		cuota = calcular_cuota_basica(dependientes)
		self.assertEqual(cuota,60)

	def test_calcular_cuota_2(self):
		"""Calcula la cuota basica del asegurado, 
	con 2 dependientes. 
	"""
		dependientes = 2
		cuota = calcular_cuota_basica(dependientes)
		self.assertEqual(cuota,90)

	def test_calcular_cuota_3(self):
		"""Calcula la cuota basica del asegurado, 
	con 3 dependientes. 
	"""
		dependientes = 3
		cuota = calcular_cuota_basica(dependientes)
		self.assertEqual(cuota,100)

	def test_calcular_cuota_4(self):
		"""Calcula la cuota basica del asegurado, 
	con 4 dependientes. 
	"""
		dependientes = 4
		cuota = calcular_cuota_basica(dependientes)
		self.assertEqual(cuota,120)

	def test_calcular_vals_adicionales_mujer_casada(self):
		"""Calcula los valores adicionales del asegurado, 
	si tiene 18 años, es mujer y está casada. 
	"""
		sexo = 'mujer'
		edad = 18
		estado_civil = 'casado'
		especial = None
		valor_adicional = calcular_valores_adicionales(edad,sexo,estado_civil,especial)
		self.assertEqual(valor_adicional,20)

	def test_calcular_vals_adicionales_mujer_soltera(self):
		"""Calcula los valores adicionales del asegurado, 
	si tiene 18 años, es mujer y soltera. 
	"""
		sexo = 'mujer'
		edad = 18
		estado_civil = 'soltero'
		especial = None
		valor_adicional = calcular_valores_adicionales(edad,sexo,estado_civil,especial)
		self.assertEqual(valor_adicional,10)

	def test_calcular_vals_adicionales_hombre_soltero(self):
		"""Calcula los valores adicionales del asegurado, 
	si tiene 18 años, es hombre y soltero. 
	"""
		sexo = 'hombre'
		edad = 18
		estado_civil = 'soltero'
		especial = None
		valor_adicional = calcular_valores_adicionales(edad,sexo,estado_civil,especial)
		self.assertEqual(valor_adicional,40)

	def test_calcular_vals_adicionales_mujer_especial(self):
		"""Calcula los valores adicionales del asegurado, 
	si tiene 41 años, es mujer y tiene osteoporosis. 
	"""
		sexo = 'mujer'
		edad = 41
		estado_civil = 'soltero'
		especial = 'osteoporosis'
		valor_adicional = calcular_valores_adicionales(edad,sexo,estado_civil,especial)
		self.assertEqual(valor_adicional,35)

	def test_calcular_vals_adicionales_hombre_especial(self):
		"""Calcula los valores adicionales del asegurado, 
	si tiene 41 años, es hombre y sufrio un infarto. 
	"""
		sexo = 'hombre'
		edad = 41
		estado_civil = 'soltero'
		especial = 'infarto'
		valor_adicional = calcular_valores_adicionales(edad,sexo,estado_civil,especial)
		self.assertEqual(valor_adicional,50)

	def test_calcular_vals_adicionales_anciana_cancer(self):
		"""Calcula los valores adicionales del asegurado, 
	si tiene + de 60 años, es mujer y tiene cancer. 
	"""
		sexo = 'mujer'
		edad = 61
		estado_civil = 'soltero'
		especial = 'cancer'
		valor_adicional = calcular_valores_adicionales(edad,sexo,estado_civil,especial)
		self.assertEqual(valor_adicional,60)

	def test_calcular_vals_adicionales_hombre_especial(self):
		"""Calcula los valores adicionales del asegurado, 
	si tiene + de 60 años, es hombre y tiene diabetes. 
	"""
		sexo = 'hombre'
		edad = 61
		estado_civil = 'soltero'
		especial = 'diabetes'
		valor_adicional = calcular_valores_adicionales(edad,sexo,estado_civil,especial)
		self.assertEqual(valor_adicional,50)


if __name__ == '__main__':
	unittest.main()