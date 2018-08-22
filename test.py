# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import src.cotizador

class Test(unittest.TestCase):

	def test_cotizador_01(self):
		'''
        	Prueba que una mujer que vive en Guayaquil, de 30 años y está casada =>
		'''
		ciudad = 'Guayaquil'
		edad = 30
		sexo = 'mujer'
		estado_civil = 'casado'
		especial = 'cancer'
		dependientes = 1
		valor = src.cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(valor, 'El valor calculado de su cotización es de 80.00')


	def test_cotizador_02(self):
		'''
        	Prueba que una mujer que vive en Guayaquil, de 30 años y es soltera => 
		'''
		ciudad = 'Guayaquil'
		edad = 30
		sexo = 'mujer'
		estado_civil = 'soltero'
		especial = 'cancer'
		dependientes = 1
		valor = src.cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(valor, 'El valor calculado de su cotización es de 70.00')


	def test_cotizador_03(self):
		'''
       		Prueba que una hombre que vive en Guayaquil, de 30 años y es soltero =>
		'''
		ciudad = 'Guayaquil'
		edad = 30
		sexo = 'hombre'
		estado_civil = 'soltero'
		especial = 'cancer'
		dependientes = 0
		valor = src.cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(valor, 'El valor calculado de su cotización es de 70.00')


	def test_cotizador_04(self):
		'''
        	Prueba que una mujer que vive en Guayaquil, de 50 años y padece osteoporosis =>
		'''
		ciudad = 'Guayaquil'
		edad = 50
		sexo = 'mujer'
		estado_civil = 'soltero'
		especial = 'osteoporosis'
		dependientes = 2
		valor = src.cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(valor, 'El valor calculado de su cotización es de 125.00')


	def test_cotizador_05(self):
		'''
        	Prueba que un hombre que vive en Guayaquil, de 50 años y padeció un infarto =>
		'''
		ciudad = 'Guayaquil'
		edad = 50
		sexo = 'hombre'
		estado_civil = 'soltero'
		especial = 'infarto'
		dependientes = 3
		valor = src.cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(valor, 'El valor calculado de su cotización es de 150.00')


	def test_cotizador_06(self):
		'''
        	Prueba que una mujer que vive en Guayaquil, de 70 años y padece diabetes =>
		'''
		ciudad = 'Guayaquil'
		edad = 70
		sexo = 'mujer'
		estado_civil = 'casado'
		especial = 'diabetes'
		dependientes = 4
		valor = src.cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(valor, 'El valor calculado de su cotización es de 180.00')


	def test_cotizador_07(self):
		'''
        	Prueba que un hombre que vive en Guayaquil, de 70 años y padece diabetes =>
		'''
		ciudad = 'Guayaquil'
		edad = 70
		sexo = 'hombre'
		estado_civil = 'casado'
		especial = 'diabetes'
		dependientes = 4
		valor = src.cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(valor, 'El valor calculado de su cotización es de 170.00')


	def test_cotizador_08(self):
		'''
        	Prueba que un hombre que vive en Guayaquil, de 15 años => edad no es válida
		'''
		ciudad = 'Guayaquil'
		edad = 15
		sexo = 'hombre'
		estado_civil = 'soltero'
		especial = ''
		dependientes = 0
		valor = src.cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(valor, 'La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años.')


	def test_cotizador_09(self):
		'''
        	Prueba que un hombre que vive en Guayaquil, de 70 años y padece diabetes
        	con más de 4 dependientes => Mensaje para que presente solicitud.
		'''
		ciudad = 'Guayaquil'
		edad = 70
		sexo = 'hombre'
		estado_civil = 'casado'
		especial = 'diabetes'
		dependientes = 5
		valor = src.cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(valor, 'Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud.')


	def test_cotizador_10(self):
		'''
        	Prueba que un hombre que vive en Guayaquil, de 70 años y padece diabetes
        	con más de 9 dependientes => No se puede realizar cotizacion.
		'''
		ciudad = 'Guayaquil'
		edad = 70
		sexo = 'hombre'
		estado_civil = 'casado'
		especial = 'diabetes'
		dependientes = 10
		valor = src.cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(valor, 'No se puede realizar una cotización para el valor ingresado de dependientes.')


	def test_cotizador_11(self):
		'''
		Prueba que un hombre que vive en Ambato => Ciudad no admitida 
		'''
		ciudad = 'Ambato'
		edad = 30
		sexo = 'mujer'
		estado_civil = 'soltero'
		especial = 'cancer'
		dependientes = 0
		valor = src.cotizador.cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes)
		self.assertEqual(valor, 'Saludcita no opera en la ciudad ingresada.')

if __name__ == '__main__':
	unittest.main()
