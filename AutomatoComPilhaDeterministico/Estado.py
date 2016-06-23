# -*- coding: utf-8 -*-
'''
Created on 23 de jun de 2016

@author: Raul
'''

class Estado(object):
    '''
     Classe respons�vel por modelar um estado de um autômato.
    '''
    #atributos
    nome=None
    ehFinal=None
    __transicoes=None
    

    def __init__(self, nome,ehFinal):
        self.nome=nome
        self.ehFinal = ehFinal
        self.__transicoes=[]
        
    def addTransicao(self,transicao):
        self.__transicoes.append(transicao)
        
    def getTransicoes(self):
        return self.__transicoes

        