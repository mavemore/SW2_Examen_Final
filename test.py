# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import src.cotizador as cotizador

class Test(unittest.TestCase):
	#Incluya una pequeña descripción de lo que se prueba.
	def test_cotizador_111(self):
		edad = 20
		sexo = "mujer"
		estado_civil = "casado"
		especial = ""
		dependientes = 0
		ciudad = "Guayaquil"

		total = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		expect = "El valor calculado de su cotización es de 50.00"

		self.assertEqual(total,expect)

	def test_cotizador_112(self):
		edad = 20
		sexo = "mujer"
		estado_civil = "soltero"
		especial = ""
		dependientes = 0
		ciudad = "Guayaquil"

		total = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		expect = "El valor calculado de su cotización es de 40.00"

		self.assertEqual(total,expect)

	def test_cotizador_12(self):
		edad = 20
		sexo = "hombre"
		estado_civil = "soltero"
		especial = ""
		dependientes = 0
		ciudad = "Guayaquil"

		total = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		expect = "El valor calculado de su cotización es de 70.00"

		self.assertEqual(total,expect)

	def test_cotizador_21(self):
		edad = 45
		sexo = "mujer"
		estado_civil = "casado"
		especial = "osteoporosis"
		dependientes = 1
		ciudad = "Guayaquil"

		total = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		expect = "El valor calculado de su cotización es de 95.00"

		self.assertEqual(total,expect)

	def test_cotizador_22(self):
		edad = 45
		sexo = "hombre"
		estado_civil = "casado"
		especial = "infarto"
		dependientes = 1
		ciudad = "Guayaquil"

		total = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		expect = "El valor calculado de su cotización es de 110.00"
		
		self.assertEqual(total,expect)

	def test_cotizador_31(self):
		edad = 65
		sexo = "mujer"
		estado_civil = "soltero"
		especial = "cancer"
		dependientes = 2
		ciudad = "Guayaquil"

		total = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		expect = "El valor calculado de su cotización es de 150.00"

		self.assertEqual(total,expect)

	def test_cotizador_32(self):
		edad = 65
		sexo = "hombre"
		estado_civil = "soltero"
		especial = "diabetes"
		dependientes = 2
		ciudad = "Guayaquil"

		total = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		expect = "El valor calculado de su cotización es de 140.00"

		self.assertEqual(total,expect)

	def test_cotizador_4(self):
		edad = 20
		sexo = "mujer"
		estado_civil = "casado"
		especial = "cancer"
		dependientes = 3
		ciudad = "Guayaquil"

		total = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		expect = "El valor calculado de su cotización es de 120.00"

		self.assertEqual(total,expect)

	def test_cotizador_5(self):
		edad = 20
		sexo = "mujer"
		estado_civil = "casado"
		especial = "cancer"
		dependientes = 4
		ciudad = "Guayaquil"

		total = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		expect = "El valor calculado de su cotización es de 140.00"

		self.assertEqual(total,expect)

	def test_cotizador_6(self):
		edad = 15
		sexo = "mujer"
		estado_civil = "casado"
		especial = "cancer"
		dependientes = 4
		ciudad = "Guayaquil"

		total = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		expect = "La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años."

		self.assertEqual(total,expect)

	def test_cotizador_7(self):
		edad = 15
		sexo = "mujer"
		estado_civil = "casado"
		especial = "cancer"
		dependientes = 6
		ciudad = "Guayaquil"

		total = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		expect = "Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud."

		self.assertEqual(total,expect)

	def test_cotizador_8(self):
		edad = 15
		sexo = "mujer"
		estado_civil = "casado"
		especial = "cancer"
		dependientes = 666
		ciudad = "Guayaquil"

		total = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		expect = "No se puede realizar una cotización para el valor ingresado de dependientes."

		self.assertEqual(total,expect)

	def test_cotizador_9(self):
		edad = 15
		sexo = "mujer"
		estado_civil = "casado"
		especial = "cancer"
		dependientes = 666
		ciudad = "Charapotó"

		total = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		expect = "Saludcita no opera en la ciudad ingresada."

		self.assertEqual(total,expect)

if __name__ == '__main__':
	unittest.main()