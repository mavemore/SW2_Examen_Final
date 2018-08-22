# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from random import randint

from src.cotizador import cotizar_seguro


class Test(unittest.TestCase):
    #Incluya una pequeña descripción de lo que se prueba.

    def setUp(self):
        # Valores permitidos
        self.ciudades_permitidas = ['Guayaquil', 'Quito', 'Cuenca', 'Machala']
        self.sexo = ['hombre', 'mujer']
        self.estado_civil_permitido = ['casado', 'soltero', 'divorciado', 'viudo']
        self.enfermedades_permitidas = ['osteoporosis', 'infarto', 'diabetes', 'cancer']


    def get_edad_permitida(self, min, max):
        return randint(min, max)

    def test_cotizador_cp001(self):
        # Cotizador para una persona que vive en las ciudades permitidas, 
        # rango de edad entre (18-40), sexo (mujer), estado civil 
        # (soltera, divorciada o viuda) y sin pre-existencias ni casos especiales
        resultado = cotizar_seguro(
            self.ciudades_permitidas[randint(0, 3)],
            randint(18, 40),
            self.sexo[1],
            self.estado_civil_permitido[randint(1, 3)],
            '', 
            0)
        self.assertEqual(resultado, "El valor calculado de su cotización es de 40.00")

    def test_cotizador_cp002(self):
        # Cotizador para una persona que vive en las ciudades permitidas, 
        # rango de edad entre (18-40), sexo (mujer), estado civil 
        # (soltera, divorciada o viuda), sin pre-existencias ni casos especiales
        # y con 1 dependiente
        resultado = cotizar_seguro(
            self.ciudades_permitidas[randint(0, 3)],
            randint(18, 40),
            self.sexo[1],
            self.estado_civil_permitido[1],
            '', 
            1)
        self.assertEqual(resultado, "El valor calculado de su cotización es de 70.00")

    def test_cotizador_cp003(self):
        # Cotizador para una persona que vive en las ciudades permitidas, 
        # rango de edad entre (18-40), sexo (mujer), estado civil 
        # (casada), sin pre-existencias ni casos especiales
        # y con 2 dependientes
        resultado = cotizar_seguro(
            self.ciudades_permitidas[randint(0, 3)],
            randint(18, 40),
            self.sexo[1],
            self.estado_civil_permitido[0],
            '', 
            2)
        self.assertEqual(resultado, "El valor calculado de su cotización es de 110.00")

    def test_cotizador_cp004(self):
        # Cotizador para una persona que vive en las ciudades permitidas, 
        # rango de edad entre (18-40), sexo (mujer), estado civil 
        # (casada), sin pre-existencias ni casos especiales
        # y con 3 dependientes
        resultado = cotizar_seguro(
            self.ciudades_permitidas[randint(0, 3)],
            randint(18, 40),
            self.sexo[1],
            self.estado_civil_permitido[0],
            '', 
            3)
        self.assertEqual(resultado, "El valor calculado de su cotización es de 120.00")


    def test_cotizador_cp005(self):
        # Cotizador para una persona que vive en las ciudades permitidas, 
        # rango de edad entre (18-40), sexo (mujer), estado civil 
        # (casada), sin pre-existencias ni casos especiales
        # y con 4 dependientes
        resultado = cotizar_seguro(
            self.ciudades_permitidas[randint(0, 3)],
            randint(18, 40),
            self.sexo[1],
            self.estado_civil_permitido[0],
            '', 
            4)
        self.assertEqual(resultado, "El valor calculado de su cotización es de 140.00")

    def test_cotizador_cp006(self):
          # Cotizador para una persona que vive en las ciudades permitidas, 
        # rango de edad entre (41-60), sexo (mujer), estado civil permitido
        # y con osteoporosis
        resultado = cotizar_seguro(
            self.ciudades_permitidas[randint(0, 3)],
            randint(41, 60),
            self.sexo[1],
            self.estado_civil_permitido[randint(0, 3)],
            self.enfermedades_permitidas[0], 
            0)
        self.assertEqual(resultado, "El valor calculado de su cotización es de 65.00")


    def test_cotizador_cp007(self):
        # Cotizador para una persona que vive en las ciudades permitidas, 
        # rango de edad entre (18-40), sexo (mujer), estado civil 
        # (casada) y no padece de ninguna enfermedad.
        resultado = cotizar_seguro(
            self.ciudades_permitidas[randint(0, 3)],
            randint(18, 40),
            self.sexo[1],
            self.estado_civil_permitido[0],
            '',
            0)
        self.assertEqual(resultado, "El valor calculado de su cotización es de 50.00")

    def test_cotizador_cp008(self):
        # Cotizador para una persona que vive en las ciudades permitidas, 
        # rango de edad entre (18-40), sexo (mujer), estado civil 
        # (casada), no padece de ninguna enfermedad y tiene 5 dependientes
        resultado = cotizar_seguro(
            self.ciudades_permitidas[randint(0, 3)],
            randint(18, 40),
            self.sexo[1],
            self.estado_civil_permitido[0],
            '',
            5)
        self.assertEqual(resultado, "Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud.")

    def test_cotizador_cp009(self):
        # Cotizador para una persona que vive en las ciudades permitidas, 
        # rango de edad entre (18-40), sexo (mujer), estado civil 
        # (casada), padece de diabetes y tiene 5 dependientes
        resultado = cotizar_seguro(
            self.ciudades_permitidas[randint(0, 3)],
            randint(18, 40),
            self.sexo[1],
            self.estado_civil_permitido[0],
            self.enfermedades_permitidas[2],
            5)
        self.assertEqual(resultado, "Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud.")

    def test_cotizador_cp010(self):
        # Cotizador para una persona que vive en las ciudades permitidas, 
        # rango de edad entre (18-40), sexo (hombre), estado civil 
        # (soltero), sin pre-existencias ni casos especiales y sin dependientes
        resultado = cotizar_seguro(
            self.ciudades_permitidas[randint(0, 3)],
            randint(18, 40),
            self.sexo[0],
            self.estado_civil_permitido[1],
            '', 
            0)
        self.assertEqual(resultado, "El valor calculado de su cotización es de 70.00")

    def test_cotizador_cp011(self):
        # Cotizador para una persona que vive en las ciudades permitidas, 
        # rango de edad entre (18-40), sexo (hombre), estado civil 
        # (soltero), con cancer y sin dependientes
        resultado = cotizar_seguro(
            self.ciudades_permitidas[randint(0, 3)],
            randint(18, 40),
            self.sexo[0],
            self.estado_civil_permitido[1],
            self.enfermedades_permitidas[3], 
            0)
        self.assertEqual(resultado, "El valor calculado de su cotización es de 70.00")

    def test_cotizador_cp012(self):
        # Cotizador para una persona que vive en las ciudades permitidas, 
        # rango de edad entre (18-40), sexo (mujer), estado civil 
        # (casada), sin pre-existencias ni casos especiales
        # y con 1 dependiente
        resultado = cotizar_seguro(
            self.ciudades_permitidas[randint(0, 3)],
            randint(18, 40),
            self.sexo[1],
            self.estado_civil_permitido[0],
            '', 
            1)
        self.assertEqual(resultado, "El valor calculado de su cotización es de 80.00")

    def test_cotizador_cp013(self):
        # Cotizador para una persona que vive en las ciudades no permitidas, 
        # rango de edad entre (18-40), sexo (mujer), estado civil 
        # (solero), padece de cancer y sin dependientes
        resultado = cotizar_seguro(
            'Ibarra',
            randint(18, 40),
            self.sexo[1],
            self.estado_civil_permitido[1],
            self.enfermedades_permitidas[3], 
            0)
        self.assertEqual(resultado, "Saludcita no opera en la ciudad ingresada.")

if __name__ == '__main__':
	unittest.main()
