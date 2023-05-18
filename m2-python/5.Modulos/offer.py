
# Crear un aclase offer que represente oferta trabajo
# title, company, salaryx, workmode, prev_exp_year

import offer
'''
class Offer:
    def __init__(self, title, company, salary, workmode, exp_years):
        self.title = title
        self.company = company
        self.salary = salary
        self.workmode = workmode
        self.exp_years = exp_years

oferta1 = offer('data analist', 'Mapfre', '20000 - 30000', 'hibrid', 3)
'''
class JobOffer:
    def __init__(self, id, title, company, salary, workmode, exp_years):
        self.id = id
        self.title = title
        self.company = company
        self.salary = salary
        self.workmode = workmode
        self.exp_years = exp_years
    def __str__(self):
        return f"{self.id} {self.title} {self.company}{self.salary}{self.workmode}{self.exp_years}"
    

