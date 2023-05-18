'''
import offer



oferta1 = offer.JobOffer(1, 'Programador Junior Python', 'ADECCO', 25000, 'remoto', 1)
oferta2 = offer.JobOffer(2, 'Analista Junior Datos', 'MAPFRE', 20000 - 30000, 'Hibrido', 3)
oferta3 = offer.JobOffer(3, 'Secretaria de dirección', 'MAHU', 1500, 'presencial', 'Practica con posiblidad de incorporarse', 0)


print(oferta1.company, oferta1.title, oferta1.workmode, oferta1.salary)
print(oferta2.title, oferta2.company, oferta2.exp_years, oferta2.salary)
print(oferta3.title, oferta3.company, oferta3.exp_years, oferta3.salary, oferta3.workmode)
'''

# pip install numpy
# pipi install numpy==1.24.3

import numpy
print(numpy.__version__)

