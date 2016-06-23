# -*- coding: utf-8 -*-
'''
Created on 23 de jun de 2016

@author: Raul
'''
from AutomatoPilhaDet import AutomatoPilhaDet
from Estado import Estado
from Transicao import Transicao

if __name__ == '__main__':
    entrada = "aabb"
    #Criação dos estados
    q0 = Estado("q0",True)
    q1 = Estado("q1",False)
    qf = Estado("qf",True)
    #Criação das transições
    t0 = Transicao("a","","A",q0)
    t1 =  Transicao("b","A","",q1)
    t2 = Transicao("?","","",qf)
    #Adiciona as transições ao estado q0
    q0.addTransicao(t0)
    q0.addTransicao(t1)
    #Adiciona as transições ao estado q1
    q1.addTransicao(t1)
    q1.addTransicao(t2)
    #Cria o automato
    auto = AutomatoPilhaDet()
    auto.addEstado(q0)
    auto.addEstado(q1)
    auto.addEstado(qf)
    auto.alfabeto=["a","b"]
    auto.setInicial(0)
    #verifica se a entrada é aceita ou não
    auto.ehAceita(entrada)
    
    
    