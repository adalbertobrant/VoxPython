#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Script idealizado por Adalberto Caldeira
## Distribuído por licença Apache 2.0, leia a mesma para saber como utilizar corretamente
## Aceitamos contribuições para o código, simplesmente mande o seu pull request.



## O objetivo do script é automatizar o processo da lista de nomes de pacientes utilizado no consultório , para que o paciente
## receba um audio individualizado e personalizado para o seu tratamento em campanhas de Marketing Neuromental Pica das Galáxias.
## Usando a metodologia T.P.G e T.A.B.C


## O programa foi testado na versão linux para Ubuntu, utilizando o python 2.7 e a biblioteca Google Text To Speach

## para instalar a biblioteca gtts , utilize o pip install 

## Dúvidas abra um issue, terei o maior prazer em lhe ajudar.

## Importa a biblioteca do google para síntese de voz feminina, tem como personalizar para vozes masculinas , velocidade, etc.
from gtts import gTTS

i = int(1)

arquivo = file("nomesComuns.txt","r")
for linha in arquivo:
    voz = gTTS(linha,"pt")
    voz.save(str(i)+"voz.mp3")
    i = i + 1


