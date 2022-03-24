#Faça um algoritmo que calcule a área de uma esfera, sendo que o comprimento do raio é informado pelo usuário. A área da esfera é calculada multiplicando-se 4 vezes Pi ao raio ao quadrado.
import math

comprimentoRaio = float(input("Insira o comprimento do raio: "))
areaEsfera = comprimentoRaio*(math.pi*4)
print("A área da esfera é:", round(areaEsfera, 2))