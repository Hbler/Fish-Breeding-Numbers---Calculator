# -*- coding: utf-8 -*-
# Números para a Criação de Peixes

# Calcula valores seguros para a criação de peixes em tanques equipados com filtros de mídia flutuante.

# 1. Solicita o peso do total de peixes no tanque.

fWeigh = input ('Digite o peso total dos peixes no tanque em Kg (quilos): >> ')


# 2. Calcula a taxa de alimentação 

feedRate = fWeigh * 0.015


# 3. Calcula o tamanho do tanque.

tSize = feedRate * 757


# 4. Calcula o volume necessários de "beads" no filtro.

bVolume = feedRate * 0.018


# 5. Calcula a circulação adequada de água no tanque.

flowRate = feedRate * 1698

# 6. Apresenta os resultados de uma maneira que o usuário pode identificar facilmente.

print
print 'A partir do peso digitado, estes são os valores atuais recomendados para a criação:'
print 'A taxa de alimentação nesse estágio é de: {: .2f}g por dia;'.format(feedRate)
print 'O tanque deve ter pelo menos: {: .2f} litros;'.format(tSize)
print 'O filtro deve ter pelo menos: {: .4f}mˆ3 de mídia flutuante;'.format(bVolume)
print 'A circulação de água deve ser de: {: .2f} L/H.'.format(flowRate)
print
print 'Todos os valores tem um fator de segurança e são calculados para um tanque equipado com um filtro com mídia flutuante.'
