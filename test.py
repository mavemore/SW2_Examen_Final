# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import src.cotizador as cotizador

class Test(unittest.TestCase):
	#Incluya una pequeña descripción de lo que se prueba.
	def test_cotizador_ID1(self):
		self.assertEqual(cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "casado", "cancer", 1),"El valor calculado de su cotización es de %.2f"%80.00)
	def test_cotizador_ID(self):
		self.assertEqual('','')
	#Numero de dependientes 0

	def test_calcular_cuota_basica_1(self):
		valor = cotizador.calcular_cuota_basica(0)
		self.assertEqual(valor,30)

	#Numero de dependientes 1
	def test_calcular_cuota_basica_2(self):
		valor = cotizador.calcular_cuota_basica(1)
		self.assertEqual(valor,60)

	#Numero de dependientes 2
	def test_calcular_cuota_basica_3(self):
		valor = cotizador.calcular_cuota_basica(2)
		self.assertEqual(valor,90)

	#Numero de dependientes 3
	def test_calcular_cuota_basica_4(self):
		valor = cotizador.calcular_cuota_basica(3)
		self.assertEqual(valor,100)

	#Numero de dependientes 4
	def test_calcular_cuota_basica_4(self):
		valor = cotizador.calcular_cuota_basica(4)
		self.assertEqual(valor,120)

	#Mujer casada de 35 años sin preexistencias
	def test_calcular_valores_adicionales_1(self):
		adicional =  cotizador.calcular_valores_adicionales(35, 'mujer', 'casado', '')
		self.assertEqual(adicional,20)

	#Mujer soltera de 32 años sin preexistencias
	def test_calcular_valores_adicionales_2(self):
		adicional =  cotizador.calcular_valores_adicionales(32, 'mujer', 'soltero', '')
		self.assertEqual(adicional,10)

	#Hombre soltero de 32 años sin preexistencias
	def test_calcular_valores_adicionales_3(self):
		adicional =  cotizador.calcular_valores_adicionales(32, 'hombre', 'soltero', '')
		self.assertEqual(adicional,40)

	#Mujer soltera de 50 años con preexistencias
	def test_calcular_valores_adicionales_4(self):
		adicional =  cotizador.calcular_valores_adicionales(50, 'mujer', 'soltero', 'osteoporosis')
		self.assertEqual(adicional,35)

	#Hombre soltera de 50 años con preexistencias
	def test_calcular_valores_adicionales_5(self):
		adicional =  cotizador.calcular_valores_adicionales(50, 'hombre', 'soltero', 'infarto')
		self.assertEqual(adicional,50)


	def test_calcular_valores_adicionales_6(self):
		adicional =  cotizador.calcular_valores_adicionales(70, 'mujer', 'soltero', 'diabetes')
		self.assertEqual(adicional,60)


	def test_calcular_valores_adicionales_7(self):
		adicional =  cotizador.calcular_valores_adicionales(70, 'mujer', 'soltero', 'cancer')
		self.assertEqual(adicional,60)


	def test_calcular_valores_adicionales_8(self):
		adicional =  cotizador.calcular_valores_adicionales(70, 'hombre', 'soltero', 'cancer')
		self.assertEqual(adicional,50)

	
	def test_calcular_valores_adicionales_9(self):
		adicional =  cotizador.calcular_valores_adicionales(70, 'hombre', 'soltero', 'diabetes')
		self.assertEqual(adicional,50)



	def test_cotizar_1(self):
		resultado =  cotizador.cotizar_seguro('Guayaquil', 35, 'mujer', 'casado', '', 4)
		self.assertEqual(resultado,"El valor calculado de su cotización es de %.2f"%140)


	def test_cotizar_2(self):
		resultado =  cotizador.cotizar_seguro('Guayaquil', 80, 'mujer', 'casado', '', 4)
		self.assertEqual(resultado,"La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años.")
	

	def test_cotizar_3(self):
		resultado =  cotizador.cotizar_seguro('Guayaquil', 60, 'mujer', 'casado', '', 7)
		self.assertEqual(resultado,"Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud.")
	

	def test_cotizar_4(self):
		resultado =  cotizador.cotizar_seguro('Guayaquil', 60, 'mujer', 'casado', '', 12)
		self.assertEqual(resultado,"No se puede realizar una cotización para el valor ingresado de dependientes.")
	

	def test_cotizar_5(self):
		resultado =  cotizador.cotizar_seguro('Manta', 60, 'mujer', 'casado', '', 2)
		self.assertEqual(resultado,"Saludcita no opera en la ciudad ingresada.")


	def test_cotizar_6(self):
		resultado =  cotizador.cotizar_seguro('Quito', 35, 'hombre', 'soltero', '', 4)
		self.assertEqual(resultado,"El valor calculado de su cotización es de %.2f"%160)

if __name__ == '__main__':
	unittest.main()