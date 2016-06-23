# -*- coding: utf-8 -*-
'''
Created on 23 de jun de 2016

@author: Raul
'''
from Estado import Estado
from Transicao import Transicao

class AutomatoPilhaDet(object):
    "Classe que modela um automato com pilha deterministico"
    #atributos
    alfabeto=[]
    estados=[]
    __inicial=None
    ativo=None
    __pilha=[]
    
    '''
        Método responsavel por testar a entrada, verificando se
        é válida ou não.
    '''
    def __simularEntrada(self,entrada):
        if(self.entradaValida(entrada)==False):
            return False
        entrada = entrada+"?"#a interrogação marca o final da entrada
        houveTransicao=True#flag para determinar se houve transição.
        if len(self.estados)==0:
            return -1
        elif self.__inicial==None:
            return -1
        else:
            for x in entrada:
                if(houveTransicao==False):#Se não houve transições o autômato ficou "estagnado" então pare
                    return False
                houveTransicao=False
                for i in self.ativo.getTransicoes():
                    if (i.temTrasicao(x,self.__pilha)):
                        self.ativo=i.getEstadoChegada()
                        self.remPilha(i.caracterPilhaLer)
                        self.addPilha(i.caracterPilhaAdd)
                        houveTransicao=True
                        break
            if(self.ativo.ehFinal and len(self.__pilha)==0):
                return True
            return False
                              
    def addEstado(self,estado):
        self.estados.append(estado)
    
    def setInicial(self,indice):
            self.__inicial=self.estados[indice]
            self.ativo=self.estados[indice]
    
    def addPilha(self,caracter):
        if caracter != "":# "" representa a palavra vazia E.
            self.__pilha.append(caracter)
    
    def remPilha(self,caracter):
        if len(self.__pilha)>0 and self.__pilha[-1]==caracter:
            self.__pilha.pop()
     
    #Testa se a entrada possui caracteres que não pertencem ao alfabeto
    def entradaValida(self,entrada):
        for i in entrada:
            if(i not in self.alfabeto):
                print(u"Possui caracteres que não pertencem ao alfabeto")
                return False
        return True
    
    
    def ehAceita(self,entrada):
        resultado=self.__simularEntrada(entrada)
        if(resultado==True):
            print(u"a cadeia:%s é aceita pela linguagem"%entrada)
        else:
            print(u"a cadeia:%s não é aceita pela linguagem"%entrada)
        
    
        
        
        