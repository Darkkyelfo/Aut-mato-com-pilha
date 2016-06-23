# -*- coding: utf-8 -*-
'''
Created on 23 de jun de 2016

@author: Raul
'''

class Transicao(object):
    '''
    Essa classe modela as transições do autômato. 
    São as 'setas' do autômato
    '''
    
    caracter=None
    __estadoDeChegada = None
    caracterPilhaLer = None
    caracterPilhaAdd = None

    def __init__(self,caracter,caracterPilhaLer,caracterPilhaAdd,estadoDeChegada):
        self.caracter=caracter
        self.__estadoDeChegada=estadoDeChegada
        self.caracterPilhaLer = caracterPilhaLer
        self.caracterPilhaAdd = caracterPilhaAdd
    
    def temTrasicao(self,caracter,pilha):
        if (caracter ==self.caracter):
            if((len(pilha)>=0 and self.caracterPilhaLer=="")):
                return True
            elif(len(pilha)>0 and pilha[-1]==self.caracterPilhaLer):
                return True
            else:
                return False
        else:
            return False
    
    def getEstadoChegada(self):
        return self.__estadoDeChegada
    
        