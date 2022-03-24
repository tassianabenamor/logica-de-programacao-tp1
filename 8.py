#Faça um algoritmo que calcule a área de um círculo, sendo que o comprimento do raio é informado pelo usuário. A área do círculo é calculada multiplicando-se Pi ao raio ao quadrado.
import math

raio_circulo = float(input("Insira o comprimento do raio:"))
area_circulo = math.pi * (raio_circulo**2)
print("A área do cículo é:", area_circulo)