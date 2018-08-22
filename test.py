# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import src.cotizador as cotizador

class Test(unittest.TestCase):
	#Guayaquil, 0 hijos, de 30 años, hombre, soltero. no sufre nada especial
	def test_cotizador_1(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "hombre", "soltero", " ", 0)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 70.00')
	#Guayaquil, 1 hijos, de 30 años, hombre, soltero. no sufre nada especial
	def test_cotizador_2(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "hombre", "soltero", " ", 1)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 100.00')
	#Guayaquil, 2 hijos, de 30 años, hombre, soltero. no sufre nada especial
	def test_cotizador_3(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "hombre", "soltero", " ", 2)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 130.00')
	#Guayaquil, 3 hijos, de 30 años, hombre, soltero. no sufre nada especial
	def test_cotizador_4(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "hombre", "soltero", " ", 3)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 140.00')
	#Guayaquil, 4 hijos, de 30 años, hombre, soltero. no sufre nada especial
	def test_cotizador_4(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "hombre", "soltero", " ", 4)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 160.00')
	#Guayaquil, 5 hijos, de 30 años, hombre, soltero. no sufre nada especial
	def test_cotizador_5(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "hombre", "soltero", " ", 5)
		self.assertEqual(resultado, 'Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud.')
	#Guayaquil, 12 hijos, de 30 años, hombre, soltero. no sufre nada especial
	def test_cotizador_6(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "hombre", "soltero", " ", 12)
		self.assertEqual(resultado, 'No se puede realizar una cotización para el valor ingresado de dependientes.')
	#Guayaquil, 0 hijos, de 45 años, hombre, soltero. sufre de infarto
	def test_cotizador_7(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 45, "hombre", "soltero", "infarto", 0)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 80.00')
	#Guayaquil, 1 hijos, de 45 años, hombre, soltero. sufre de infarto
	def test_cotizador_8(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 45, "hombre", "soltero", "infarto", 1)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 110.00')
	#Guayaquil, 2 hijos, de 45 años, hombre, soltero. sufre de infarto
	def test_cotizador_9(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 45, "hombre", "soltero", "infarto", 2)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 140.00')
	#Guayaquil, 3 hijos, de 45 años, hombre, soltero. sufre de infarto
	def test_cotizador_10(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 45, "hombre", "soltero", "infarto", 3)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 150.00')
	#Guayaquil, 4 hijos, de 45 años, hombre, soltero. sufre de infarto
	def test_cotizador_11(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 45, "hombre", "soltero", "infarto", 4)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 170.00')
	#Guayaquil, 0 hijos, de 65 años, hombre, soltero. tiene cáncer
	def test_cotizador_12(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 65, "hombre", "soltero", "cancer", 0)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 80.00')
	#Guayaquil, 1 hijos, de 65 años, hombre, soltero. tiene cáncer
	def test_cotizador_13(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 65, "hombre", "soltero", "cancer", 1)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 110.00')
	#Guayaquil, 2 hijos, de 65 años, hombre, soltero. tiene cáncer
	def test_cotizador_14(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 65, "hombre", "soltero", "cancer", 2)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 140.00')
	#Guayaquil, 3 hijos, de 65 años, hombre, soltero. tiene cáncer
	def test_cotizador_15(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 65, "hombre", "soltero", "cancer", 3)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 150.00')
	#Guayaquil, 4 hijos, de 65 años, hombre, soltero. tiene cáncer
	def test_cotizador_16(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 65, "hombre", "soltero", "cancer", 4)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 170.00')

	#Mujer...
	#Guayaquil, 0 hijos, de 30 años, mujer, soltero. no sufre nada especial
	def test_cotizador_17(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "soltero", " ", 0)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 40.00')
	#Guayaquil, 1 hijos, de 30 años, mujer, soltero. no sufre nada especial
	def test_cotizador_18(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "soltero", " ", 1)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 70.00')
	#Guayaquil, 2 hijos, de 30 años, mujer, soltero. no sufre nada especial
	def test_cotizador_19(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "soltero", " ", 2)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 100.00')
	#Guayaquil, 3 hijos, de 30 años, mujer, soltero. no sufre nada especial
	def test_cotizador_20(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "soltero", " ", 3)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 110.00')
	#Guayaquil, 4 hijos, de 30 años, mujer, soltero. no sufre nada especial
	def test_cotizador_21(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "soltero", " ", 4)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 130.00')
	#Guayaquil, 5 hijos, de 30 años, mujer, soltero. no sufre nada especial
	def test_cotizador_22(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "soltero", " ", 5)
		self.assertEqual(resultado, 'Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud.')
	#Guayaquil, 12 hijos, de 30 años, mujer, soltero. no sufre nada especial
	def test_cotizador_23(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "soltero", " ", 12)
		self.assertEqual(resultado, 'No se puede realizar una cotización para el valor ingresado de dependientes.')
	#Guayaquil, 0 hijos, de 45 años, mujer, soltero. sufre de osteoporosis
	def test_cotizador_24(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 45, "mujer", "soltero", "osteoporosis", 0)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 65.00')
	#Guayaquil, 1 hijos, de 45 años, mujer, soltero. sufre de osteoporosis
	def test_cotizador_25(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 45, "mujer", "soltero", "osteoporosis", 1)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 95.00')
	#Guayaquil, 2 hijos, de 45 años, mujer, soltero. sufre de osteoporosis
	def test_cotizador_26(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 45, "mujer", "soltero", "osteoporosis", 2)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 125.00')
	#Guayaquil, 3 hijos, de 45 años, mujer, soltero. sufre de osteoporosis
	def test_cotizador_27(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 45, "mujer", "soltero", "osteoporosis", 3)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 135.00')
	#Guayaquil, 4 hijos, de 45 años, mujer, soltero. sufre de osteoporosis
	def test_cotizador_28(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 45, "mujer", "soltero", "osteoporosis", 4)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 155.00')
	#Guayaquil, 0 hijos, de 65 años, mujer, soltero. tiene cáncer
	def test_cotizador_29(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 65, "mujer", "soltero", "cancer", 0)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 90.00')
	#Guayaquil, 1 hijos, de 65 años, mujer, soltero. tiene cáncer
	def test_cotizador_30(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 65, "mujer", "soltero", "cancer", 1)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 120.00')
	#Guayaquil, 2 hijos, de 65 años, mujer, soltero. tiene cáncer
	def test_cotizador_31(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 65, "mujer", "soltero", "cancer", 2)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 150.00')
	#Guayaquil, 3 hijos, de 65 años, mujer, soltero. tiene cáncer
	def test_cotizador_32(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 65, "mujer", "soltero", "cancer", 3)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 160.00')
	#Guayaquil, 4 hijos, de 65 años, mujer, soltero. tiene cáncer
	def test_cotizador_33(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 65, "mujer", "soltero", "cancer", 4)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 180.00')

	#Mujer entre 18 y 40, casada.

	#Guayaquil, 0 hijos, de 30 años, mujer, casado. no sufre nada especial
	def test_cotizador_34(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "casado", " ", 0)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 50.00')
	#Guayaquil, 1 hijos, de 30 años, mujer, casado. no sufre nada especial
	def test_cotizador_35(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "casado", " ", 1)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 80.00')
	#Guayaquil, 2 hijos, de 30 años, mujer, casado. no sufre nada especial
	def test_cotizador_36(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "casado", " ", 2)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 110.00')
	#Guayaquil, 3 hijos, de 30 años, mujer, casado. no sufre nada especial
	def test_cotizador_37(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "casado", " ", 3)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 120.00')
	#Guayaquil, 4 hijos, de 30 años, mujer, casado. no sufre nada especial
	def test_cotizador_38(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "casado", " ", 4)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 140.00')

	#Hombre, entre 18 y 40, casado.

	#Guayaquil, 0 hijos, de 30 años, hombre, casado. no sufre nada especial
	def test_cotizador_39(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "hombre", "casado", " ", 0)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 30.00')
	#Guayaquil, 1 hijos, de 30 años, hombre, casado. no sufre nada especial
	def test_cotizador_40(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "hombre", "casado", " ", 1)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 60.00')
	#Guayaquil, 2 hijos, de 30 años, hombre, casado. no sufre nada especial
	def test_cotizador_41(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "hombre", "casado", " ", 2)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 90.00')
	#Guayaquil, 3 hijos, de 30 años, hombre, casado. no sufre nada especial
	def test_cotizador_42(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "hombre", "casado", " ", 3)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 100.00')
	#Guayaquil, 4 hijos, de 30 años, hombre, casado. no sufre nada especial
	def test_cotizador_43(self):
		resultado = cotizador.cotizar_seguro("Guayaquil", 30, "hombre", "casado", " ", 4)
		self.assertEqual(resultado, 'El valor calculado de su cotización es de 120.00')
if __name__ == '__main__':
	unittest.main()