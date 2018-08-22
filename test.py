# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import src.cotizador as cotizador

# ciudad 'Guayaquil','Quito','Cuenca','Machala'
# edad 18,40 - 41,60 - 60
# estado_civil casado, soltero
# 

class Test(unittest.TestCase):
	#Incluya una pequeña descripción de lo que se prueba.
	def test_cotizador_IDCalcularCuota1(self):
		dependientes = 0
		cuota_basica = cotizador.calcular_cuota_basica(dependientes)
		self.assertEqual(cuota_basica,30)
	def test_cotizador_IDCalcularCuota2(self):
		dependientes = 1
		cuota_basica = cotizador.calcular_cuota_basica(dependientes)
		self.assertEqual(cuota_basica,60)
	def test_cotizador_IDCalcularCuota3(self):
		dependientes = 2
		cuota_basica = cotizador.calcular_cuota_basica(dependientes)
		self.assertEqual(cuota_basica,90)
	def test_cotizador_IDCalcularCuota4(self):
		dependientes = 3
		cuota_basica = cotizador.calcular_cuota_basica(dependientes)
		self.assertEqual(cuota_basica,100)
	def test_cotizador_IDCalcularCuota5(self):
		dependientes = 4
		cuota_basica = cotizador.calcular_cuota_basica(dependientes)
		self.assertEqual(cuota_basica,120)

	def test_cotizador_IDvaloresAdicionales1(self):
		edad = 18
		sexo = 'mujer'
		estado_civil = 'casado'
		especial = ''
		valor_adicional = cotizador.calcular_valores_adicionales(edad, sexo, estado_civil, especial)
		self.assertEqual(valor_adicional,20)

	def test_cotizador_IDvaloresAdicionales2(self):
		edad = 18
		sexo = 'mujer'
		estado_civil = ''
		especial = ''
		valor_adicional = cotizador.calcular_valores_adicionales(edad, sexo, estado_civil, especial)
		self.assertEqual(valor_adicional,10)

	def test_cotizador_IDvaloresAdicionales3(self):
		edad = 18
		sexo = 'hombre'
		estado_civil = 'soltero'
		especial = ''
		valor_adicional = cotizador.calcular_valores_adicionales(edad, sexo, estado_civil, especial)
		self.assertEqual(valor_adicional,40)

	def test_cotizador_IDvaloresAdicionales4(self):
		edad = 41
		sexo = 'mujer'
		estado_civil = ''
		especial = 'osteoporosis'
		valor_adicional = cotizador.calcular_valores_adicionales(edad, sexo, estado_civil, especial)
		self.assertEqual(valor_adicional,35)

	def test_cotizador_IDvaloresAdicionales5(self):
		edad = 41
		sexo = 'hombre'
		estado_civil = ''
		especial = 'infarto'
		valor_adicional = cotizador.calcular_valores_adicionales(edad, sexo, estado_civil, especial)
		self.assertEqual(valor_adicional,50)

	def test_cotizador_IDvaloresAdicionales6(self):
		edad = 61
		sexo = 'mujer'
		estado_civil = ''
		especial = 'cancer'
		valor_adicional = cotizador.calcular_valores_adicionales(edad, sexo, estado_civil, especial)
		self.assertEqual(valor_adicional,60)

	def test_cotizador_IDvaloresAdicionales7(self):
		edad = 61
		sexo = 'hombre'
		estado_civil = ''
		especial = 'cancer'
		valor_adicional = cotizador.calcular_valores_adicionales(edad, sexo, estado_civil, especial)
		self.assertEqual(valor_adicional,50)


	def test_cotizador_IDCotizador1(self):
		ciudad = 'Guayaquil'
		dependientes = 3
		edad = 18
		sexo = 'hombre'
		estado_civil = 'casado'
		especial = ''
		cotizado = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(cotizado, "El valor calculado de su cotización es de 100.00")

	def test_cotizador_IDCotizador2(self):
		ciudad = 'Guayaquil'
		dependientes = 5
		edad = 18
		sexo = 'hombre'
		estado_civil = 'casado'
		especial = ''
		cotizado = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(cotizado, "Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud.")

	def test_cotizador_IDCotizador3(self):
		ciudad = 'Guayaquil'
		dependientes = 10
		edad = 18
		sexo = 'hombre'
		estado_civil = 'casado'
		especial = ''
		cotizado = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(cotizado, "No se puede realizar una cotización para el valor ingresado de dependientes.")

	def test_cotizador_IDCotizador4(self):
		ciudad = ''
		dependientes = 10
		edad = 18
		sexo = 'hombre'
		estado_civil = 'casado'
		especial = ''
		cotizado = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(cotizado, "Saludcita no opera en la ciudad ingresada.")

	def test_cotizador_IDCotizador5(self):
		ciudad = 'Guayaquil'
		dependientes = 3
		edad = 76
		sexo = 'hombre'
		estado_civil = 'casado'
		especial = ''
		cotizado = cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(cotizado, "La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años.")
	# def test_cotizador_ID1(self):
	# 	self.assertEqual('','')
	# 	cotizado = cotizador.cotizar_seguro('Guayaquil', 18, 'homre', 'casado', '', 0)
	# 	print cotizado

if __name__ == '__main__':
	unittest.main()