# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 09:34:41 2022

@author: lab
"""

class Datos(object):
    def __init__(self, CI, edad, direccion):
        self.ci=CI
        self.edad=edad
        self.direccion=direccion

class Sistema(Datos):
    def __init__(self,CI, edad, direccion, ritmo, glucosa, saturacion,):
        Datos.__init__(self, CI, edad, direccion)
        self.ritmo=ritmo
        self.glucosa=glucosa
        self.saturacion=saturacion
        
    
    def get_Alert(self):
        return self.glucosa 
    
    def set_Alert(self, new_glucosa):
        if isinstance(new_glucosa, int) and new_glucosa >0 and new_glucosa < 299:
            print('La glucosa esta normal')
            self.glucosa = new_glucosa
            new_glucosa=e
            
        else:
            print('Indicios de Diabetes')
            
persona=[]
n=int(input('cuantos datos desea ingresar:' ))
for i in range(n):
    a=int(input('ingrese la cedula del paciente: '))
    b=int(input('ingrese la edad del paciente: '))
    c=str(input('ingrese la dirección donde vive el paciente: '))
    d=(input('ingrese el ritmo cardiaco del paciente: '))
    e=int(input('ingrese la glucosa que tiene el paciente: '))
    f=int(input('ingrese la saturacion con la que llego el paciente: '))
    
    persona.append(Sistema(a,b,c, d, e, f))

for i in persona:
    print('Paciente   N°    C.I.    Edad     Dirección    Ritmo  Glucosa  Saturacion' )
    print('Paciente: ', n, i.ci, '  ', i.edad,'     ',i.direccion, '     ',i.ritmo,'  ', i.glucosa,'   ', i.saturacion)
    print(i.set_Alert(e))