#!/usr/bin/python
# -*- coding: utf-8 -*-


from unicodedata import normalize
# sistema
import os
#regex
import re

import random
import string


def remover_acentos(txt,codif='iso-8859-1'):
	return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')

def pass_generator(size=8, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

texto_pronto = ''
texto_auxiliar = ''
linha_pronta = ''
cont_linha = 0
#abre o arquivo
arq = open('emails.txt', 'r')

#lê como lista
texto = arq.readlines()

#Remove nova linha no padrão windows(\r\n)
texto = [x.rstrip() for x in texto]


#remove duplicados
texto = set(texto)

#Ordena
texto = sorted(texto)

#Tem que ter o seguinte formato
#Login Username, Password, optional Login Email
for linha in texto :
	#remove acentos
	linha = remover_acentos(linha)
	#Transforma em minusculas
	linha = linha.lower()
	#Remove espaço anterior
	linha = linha.strip()

	if cont_linha > 0 :
		linha_anterior = str(texto[cont_linha-1])
	else :
		linha_anterior = ''
	
	login = linha.split("@")[0]

	if linha_anterior.find(login) > -1:
		provedor = linha.split("@")[1]
		provedor = provedor.split(".")[0]
		login = login + "-" + provedor
		# print login

	# email = linha.strip()

	linha_pronta += login
	linha_pronta +=','

	#gera senha
	senha = pass_generator()
	linha_pronta += senha
	linha_pronta +=','
	linha_pronta += linha
	linha_pronta += "\n"
# 	print linha
	
	cont_linha += 1
# print texto_pronto
arq.close()

#imprime texto auxiliar
arq_novo = open("auxiliar.txt","w")
arq_novo.write(linha_pronta)
arq_novo.close()


# Exporta para o novo aquivo
# arq_novo = open("CTBIL109.TXT","w")
# arq_novo.write(texto_pronto)
# arq_novo.close()
# print 'Exportação terminada.'
