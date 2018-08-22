# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import src.cotizador

class Test(unittest.TestCase):
	#Mujer, soltera, 18 años, Guayaquil
	def test_cotizador_1(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",18, "mujer","soltero","",0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 40.00")

	#Mujer, casada, 30 años, sin hijos, Cuenca
	def test_cotizador_2(self):
		resultado = src.cotizador.cotizar_seguro("Cuenca",30, "mujer","casado","",1)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 80.00")

	#Mujer, casada, 30 años, 1 hijos, Cuenca
	def test_cotizador_3(self):
		resultado = src.cotizador.cotizar_seguro("Cuenca",30, "mujer","casado","",2)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 110.00")
	
	#Mujer, casada, 30 años, 2 hijos, Cuenca
	def test_cotizador_4(self):
		resultado = src.cotizador.cotizar_seguro("Cuenca",30, "mujer","casado","",3)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 120.00")

	#Mujer, casada, 30 años, 3 hijos, Cuenca
	def test_cotizador_5(self):
		resultado = src.cotizador.cotizar_seguro("Cuenca",30, "mujer","casado","",4)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 140.00")

	#Mujer, soltera, 50 años, osteoporosis, Guayaquil
	def test_cotizador_6(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",50, "mujer","soltero","osteoporosis",0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 65.00")

	#Mujer, soltera, 70 años, cancer, Guayaquil
	def test_cotizador_7(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",70, "mujer","soltero","cancer",0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 90.00")

	#Mujer, casada, 50 años, sin hijos, osteoporosis, Machala
	def test_cotizador_8(self):
		resultado = src.cotizador.cotizar_seguro("Machala",50, "mujer","casado","osteoporosis",1)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 95.00")

	#Mujer, casada, 50 años, 1 hijos, osteoporosis, Machala
	def test_cotizador_9(self):
		resultado = src.cotizador.cotizar_seguro("Machala",50, "mujer","casado","osteoporosis",2)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 125.00")

	#Mujer, casada, 50 años, 2 hijos, osteoporosis, Machala
	def test_cotizador_10(self):
		resultado = src.cotizador.cotizar_seguro("Machala",50, "mujer","casado","osteoporosis",3)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 135.00")

	#Mujer, casada, 50 años, 3 hijos, osteoporosis, Machala
	def test_cotizador_11(self):
		resultado = src.cotizador.cotizar_seguro("Machala",50, "mujer","casado","osteoporosis",4)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 155.00")

	#Mujer, casada, 70 años, sin hijos, cancer, Guayaquil
	def test_cotizador_12(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",70, "mujer","casado","cancer",1)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 120.00")

	#Mujer, casada, 70 años, 1 hijos, cancer, Guayaquil
	def test_cotizador_13(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",70, "mujer","casado","cancer",2)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 150.00")

	#Mujer, casada, 70 años, 2 hijos, cancer, Guayaquil
	def test_cotizador_14(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",70, "mujer","casado","cancer",3)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 160.00")

	#Mujer, casada, 70 años, 3 hijos, cancer, Guayaquil
	def test_cotizador_15(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",70, "mujer","casado","cancer",4)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 180.00")



	#Hombre, soltero, 18 años, Guayaquil
	def test_cotizador_16(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",18, "hombre","soltero","",0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 70.00")
	
	#Hombre, casado, 30 años, sin hijos, Guayaquil
	def test_cotizador_16(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "hombre","casado","",1)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 60.00")

	#Hombre, casado, 30 años, 1 hijos, Guayaquil
	def test_cotizador_17(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "hombre","casado","",2)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 90.00")
	
	#Hombre, casado, 30 años, 2 hijos, Guayaquil
	def test_cotizador_18(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "hombre","casado","",3)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 100.00")

	#Hombre, casado, 30 años, 3 hijos, Guayaquil
	def test_cotizador_19(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "hombre","casado","",4)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 120.00")

	#Hombre, casado, 50 años, sin hijos, infarto, Guayaquil
	def test_cotizador_20(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",50, "hombre","casado","infarto",1)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 110.00")


	#Hombre, casado, 50 años, 1 hijos, infarto, Guayaquil
	def test_cotizador_21(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",50, "hombre","casado","infarto",2)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 140.00")

	#Hombre, casado, 50 años, 2 hijos, infarto, Guayaquil
	def test_cotizador_22(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",50, "hombre","casado","infarto",3)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 150.00")

	#Hombre, casado, 50 años, 3 hijos, infarto, Guayaquil
	def test_cotizador_23(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",50, "hombre","casado","infarto",4)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 170.00")

	#Hombre, soltero, 50 años, infarto, Guayaquil
	def test_cotizador_24(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",50, "hombre","soltero","infarto",0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 80.00")

	#Hombre, soltero, 70 años, cancer, Guayaquil
	def test_cotizador_25(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",70, "hombre","soltero","cancer",0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 80.00")

	#Hombre, casado, 70 años, sin hijos, cancer, Guayaquil
	def test_cotizador_26(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",70, "hombre","casado","cancer",1)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 110.00")

	#Hombre, casado, 70 años, 1 hijos, cancer, Guayaquil
	def test_cotizador_27(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",70, "hombre","casado","cancer",2)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 140.00")

	#Hombre, casado, 70 años, 2 hijos, cancer, Guayaquil
	def test_cotizador_28(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",70, "hombre","casado","cancer",3)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 150.00")

	#Hombre, casado, 70 años, 3 hijos, cancer, Guayaquil
	def test_cotizador_29(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",70, "hombre","casado","cancer",4)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 170.00")

	#Mujer, viuda, 30 años, sin hijos, Guayaquil
	def test_cotizador_30(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "mujer","viudo","",0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 40.00")

	#Mujer, divorciada, 30 años, sin hijos, Guayaquil
	def test_cotizador_31(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "mujer","divorciado","",0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 40.00")

	#Hombre, viudo, 30 años, sin hijos, Guayaquil
	def test_cotizador_32(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "hombre","viudo","",0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 30.00")

	#Hombre, divorciado, 30 años, sin hijos, Guayaquil
	def test_cotizador_33(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "hombre","divorciado","",0)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 30.00")

	#Mujer, viuda, 30 años, 1 hijos, Guayaquil
	def test_cotizador_34(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "mujer","viudo","",1)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 70.00")

	#Mujer, viuda, 30 años, 2 hijos, Guayaquil
	def test_cotizador_35(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "mujer","viudo","",2)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 100.00")

	#Mujer, viuda, 30 años, 3 hijos, Guayaquil
	def test_cotizador_36(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "mujer","viudo","",3)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 110.00")

	#Mujer, viuda, 30 años, 4 hijos, Guayaquil
	def test_cotizador_37(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "mujer","viudo","",4)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 130.00")

	#Mujer, divorciada, 30 años, 1 hijos, Guayaquil
	def test_cotizador_38(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "mujer","divorciado","",1)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 70.00")

	#Mujer, divorciada, 30 años, 2 hijos, Guayaquil
	def test_cotizador_39(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "mujer","divorciado","",2)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 100.00")

	#Mujer, divorciada, 30 años, 3 hijos, Guayaquil
	def test_cotizador_40(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "mujer","divorciado","",3)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 110.00")

	#Mujer, divorciada, 30 años, 4 hijos, Guayaquil
	def test_cotizador_41(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "mujer","divorciado","",4)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 130.00")

	#Hombre, viudo, 30 años, 1 hijos, Guayaquil
	def test_cotizador_42(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "hombre","viudo","",1)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 60.00")

	#Hombre, viudo, 30 años, 2 hijos, Guayaquil
	def test_cotizador_43(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "hombre","viudo","",2)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 90.00")

	#Hombre, viudo, 30 años, 3 hijos, Guayaquil
	def test_cotizador_44(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "hombre","viudo","",3)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 100.00")

	#Hombre, viudo, 30 años, 4 hijos, Guayaquil
	def test_cotizador_45(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "hombre","viudo","",4)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 120.00")

	#Hombre, divorciado, 30 años, 1 hijos, Guayaquil
	def test_cotizador_46(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "hombre","divorciado","",1)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 60.00")

	#Hombre, divorciado, 30 años, 2 hijos, Guayaquil
	def test_cotizador_47(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "hombre","divorciado","",2)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 90.00")

	#Hombre, divorciado, 30 años, 3 hijos, Guayaquil
	def test_cotizador_48(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "hombre","divorciado","",3)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 100.00")

	#Hombre, divorciado, 30 años, 4 hijos, Guayaquil
	def test_cotizador_49(self):
		resultado = src.cotizador.cotizar_seguro("Guayaquil",30, "hombre","divorciado","",4)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 120.00")

	#Hombre, divorciado, 30 años, 1 hijos, Quito
	def test_cotizador_50(self):
		resultado = src.cotizador.cotizar_seguro("Quito",30, "hombre","divorciado","",1)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 60.00")

	#Hombre, divorciado, 30 años, 2 hijos, Quito
	def test_cotizador_51(self):
		resultado = src.cotizador.cotizar_seguro("Quito",30, "hombre","divorciado","",2)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 90.00")

	#Hombre, divorciado, 30 años, 3 hijos, Quito
	def test_cotizador_52(self):
		resultado = src.cotizador.cotizar_seguro("Quito",30, "hombre","divorciado","",3)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 100.00")

	#Hombre, divorciado, 30 años, 4 hijos, Quito
	def test_cotizador_53(self):
		resultado = src.cotizador.cotizar_seguro("Quito",30, "hombre","divorciado","",4)
		self.assertEqual(resultado, "El valor calculado de su cotización es de 120.00")


if __name__ == '__main__':
	unittest.main()