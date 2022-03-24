#Faça um algoritmo que calcule o volume de uma caixa de água cilíndrica, sendo que os comprimentos do raio e a altura são informados pelo usuário. O volume é calculado multiplicando-se Pi, ao raio ao quadrado, a altura.
import math

raio = float(input("Insira o raio:"))
altura = float(input("Insira a altura:"))
volume = math.pi * (raio**2) * altura
print("O volume da caixa de água é:", volume)