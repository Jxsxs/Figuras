# -*- coding: utf-8 -*-
from lettuce import *
import sys 
sys.path.append('../')
from Figura import Figura

@step(u'Given: que la figura es un "([^"]*)" y el lado es "([^"]*)"')
def given_que_la_figura_es_un_cuadrado_y_el_lado_es_6(step,figura,lado):
    world.parametros=[figura,int(lado)]

@step(u'When: realizo el calculo')
def when_realizo_el_calculo(step):
   fig = Figura(world.parametros)
   world.area=fig.getArea()

@step(u'Then: obtengo el resultado "([^"]*)"')
def then_obtengo_el_resultado_36(step,area):
    assert world.area == int(area),'Area calculada {0}, Area esperada {1}'.format(world.area,area)

@step(u'Then: obtengo el resultado con decimales es "([^"]*)"')
def then_obtengo_el_resultado_con_decimales_es_group1(step, area):
    assert float(world.area) == float(area),'Area calculada {0}, Area esperada {1}'.format(world.area,area)

@step(u'Given: que la figura es un "([^"]*)" su base es "([^"]*)" y su altura "([^"]*)"')
def given_que_la_figura_es_un_group1_su_base_es_group2_y_su_altura_group3(step, figura, base, altura):
    world.parametros=[figura,int(base),int(altura)]
    
@step(u'Then: obtengo el resultado es "([^"]*)"')
def then_obtengo_el_resultado_es_group1(step, area):
     assert world.area == int(area),'Area calculada {0}, Area esperada {1}'.format(world.area,area)
