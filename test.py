# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import src.cotizador

class Test(unittest.TestCase):
	#Incluya una pequeña descripción de lo que se prueba.
	def test_cotizador_ID_1(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 20, "mujer", "soltero", "", 0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 40.00")

	def test_cotizador_ID_2(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "divorciado", "", 0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 40.00")

	def test_cotizador_ID_3(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "viudo", "", 0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 40.00")





	def test_cotizador_ID_4(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "divorciado", "", 1)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 70.00")		

	def test_cotizador_ID_5(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "divorciado", "", 2)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 100.00")		

	def test_cotizador_ID_6(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "divorciado", "", 3)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 110.00")		

	def test_cotizador_ID_7(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "divorciado", "", 4)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 130.00")		



	def test_cotizador_ID_8(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "viudo", "", 1)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 70.00")		

	def test_cotizador_ID_9(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "viudo", "", 2)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 100.00")		

	def test_cotizador_ID_10(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "viudo", "", 3)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 110.00")		

	def test_cotizador_ID_11(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 30, "mujer", "viudo", "", 4)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 130.00")	




	def test_cotizador_ID_12(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 25, "mujer", "casado", "", 1)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 80.00")

	def test_cotizador_ID_13(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 25, "mujer", "casado", "", 2)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 110.00")

	def test_cotizador_ID_14(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 25, "mujer", "casado", "", 3)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 120.00")		


	def test_cotizador_ID_15(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 25, "mujer", "casado", "", 4)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 140.00")



	def test_cotizador_ID_16(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 20, "hombre", "soltero", "", 0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 70.00")










	def test_cotizador_ID_17(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 50, "mujer", "soltero", "osteoporosis", 0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 65.00")

	def test_cotizador_ID_18(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 50, "mujer", "divorciado", "osteoporosis", 0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 65.00")

	def test_cotizador_ID_19(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 50, "mujer", "viudo", "osteoporosis", 0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 65.00")



	def test_cotizador_ID_17(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 50, "hombre", "soltero", "infarto", 0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 80.00")

	def test_cotizador_ID_18(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 50, "hombre", "divorciado", "infarto", 0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 80.00")

	def test_cotizador_ID_19(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 50, "hombre", "viudo", "infarto", 0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 80.00")



	def test_cotizador_ID_20(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 50, "mujer", "divorciado", "osteoporosis", 1)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 95.00")		

	def test_cotizador_ID_21(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 50, "mujer", "divorciado", "osteoporosis", 2)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 125.00")		

	def test_cotizador_ID_22(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 50, "mujer", "divorciado", "osteoporosis", 3)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 135.00")		

	def test_cotizador_ID_23(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 50, "mujer", "divorciado", "osteoporosis", 4)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 155.00")		


	def test_cotizador_ID_24(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 50, "mujer", "casado", "osteoporosis", 1)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 95.00")

	def test_cotizador_ID_25(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 50, "mujer", "casado", "osteoporosis", 2)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 125.00")

	def test_cotizador_ID_26(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 50, "mujer", "casado", "osteoporosis", 3)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 135.00")		


	def test_cotizador_ID_27(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 50, "mujer", "casado", "osteoporosis", 4)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 155.00")




	def test_cotizador_ID_28(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 50, "hombre", "casado", "infarto", 1)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 110.00")


	def test_cotizador_ID_29(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 50, "hombre", "casado", "infarto", 2)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 140.00")

	def test_cotizador_ID_30(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 50, "hombre", "casado", "infarto", 3)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 150.00")		


	def test_cotizador_ID_31(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil", 50, "hombre", "casado", "infarto", 4)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 170.00")




	def test_cotizador_ID_32(self):
		resultado = src.cotizador.calcular_cuota_basica(0);
		self.assertEqual(resultado, 30)

	def test_cotizador_ID_33(self):
		resultado = src.cotizador.calcular_cuota_basica(1);
		self.assertEqual(resultado, 60)

	def test_cotizador_ID_34(self):
		resultado = src.cotizador.calcular_cuota_basica(2);
		self.assertEqual(resultado, 90)

	def test_cotizador_ID_35(self):
		resultado = src.cotizador.calcular_cuota_basica(3);
		self.assertEqual(resultado, 100)


	def test_cotizador_ID_35(self):
		resultado = src.cotizador.calcular_cuota_basica(4);
		self.assertEqual(resultado, 120)






if __name__ == '__main__':
	resultado = src.c
	unittest.main()
